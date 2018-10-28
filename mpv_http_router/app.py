
import json
import logging
import logging.config

from flask import Flask, Response, abort, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sockets import Sockets
from geventwebsocket.websocket import WebSocket
from werkzeug.serving import is_running_from_reloader

from .config import load
from .exc import SocketSendError
from .message import Message
from .mpv.socket_watcher import SocketWatcher
from .websocket_listener import WebsocketListener, WebsocketListenerList
from .property_observer_manager import PropertyObserverManager

config = load()

if config is None:
    print("Config cannot be loaded!")
    exit(42)

logging.config.dictConfig(config.logger)

logger = logging.getLogger(__name__)

logger.info("App start")

app = Flask('mpv-http-router')
CORS(app)

listeners = [] # type: WebsocketListenerList

sockets = Sockets(app)

socket_watcher = SocketWatcher(config.mpv_socket_pattern, listeners)

property_observer_manager = PropertyObserverManager(socket_watcher)

listeners.append(property_observer_manager)

@app.route('/list', methods = ['GET'])
def list_():
    return jsonify(socket_watcher.id_list)

@app.route('/send/<id>', methods = ['POST'])
def send(id):
    if id not in socket_watcher:
        abort(404)
    data = request.get_json()
    return jsonify(socket_watcher.send(Message(id, data), wait_for_response = True))

@app.route('/observe_properties/<id>', methods = ['POST'])
def observe_properties(id):
    if id not in socket_watcher:
        abort(404)

    return jsonify(property_observer_manager.observe(id, request.get_json()))

@app.route('/batch/<id>', methods = ['POST'])
def batch(id):
    if id not in socket_watcher:
        abort(404, 'unknown id')
    res = []
    data = request.get_json()
    if data is None:
        return jsonify({})

    for msg in data:
        res.append(socket_watcher.send(Message(id, msg), wait_for_response = True))
    return jsonify(res)

@sockets.route('/listen')
def listen(ws: WebSocket):
    listener = WebsocketListener(ws)
    listeners.append(listener)
    logger.info("websocket client from %s has been connected", listener.remote_addr)
    while not ws.closed:
        raw_msg = ws.receive()
        if not raw_msg:
            break
        message = Message.create(raw_msg)

        logger.debug("Message %s received from %s", message, listener.remote_addr)

        if message.id not in socket_watcher:
            listener.send(Message(message.id, {}, 'unknown id'))
            continue

        try:
            socket_watcher.send(message)
        except SocketSendError as e:
            logger.exception("cannot send message: %s", e)
            listener.send(Message(message.id, {}, 'unknown id'))
            continue

    listeners.remove(listener)

    logger.info("websocket client from %s has been disconnected. Remaining listeners: %s", listener.remote_addr, len(listeners))
