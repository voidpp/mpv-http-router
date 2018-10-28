import json
import logging
import os
import socket
from enum import Enum
from threading import Event, Thread
from typing import Dict

from mpv_http_router.exc import SocketSendError
from mpv_http_router.message import Message

from .listener_base import ListenerList

logger = logging.getLogger(__name__)

class RouterEventType(Enum):

    MPV_INSTANCE_CREATED = 'mpv-instance-created'
    MPV_INSTANCE_REMOVED = 'mpv-instance-removed'

class RouterEvent(Message):

    def __init__(self, id: str, type: RouterEventType):
        super().__init__(id, {"routerevent": type.value})

class SocketHandler(Thread):
    """Represent an mpv instance
    """

    def __init__(self, id: str, filename: str, listeners: ListenerList):
        super().__init__()
        self._id = id
        self._filename = filename
        self._connected = False
        self._socket: socket.socket
        self._listeners = listeners
        self._last_not_mpv_event_data = {}
        self._sync_send_event = Event()

    @property
    def connected(self):
        return self._connected

    @property
    def filename(self):
        return self._filename

    def connect(self) -> bool:
        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        try:
            self._socket.connect(self._filename)
            self._connected = True

            logger.info('Connected to %s' % self._filename)

            for listener in self._listeners:
                listener.send(RouterEvent(self._id, RouterEventType.MPV_INSTANCE_CREATED))

            return True
        except socket.error as e:
            logger.error("Exception when try to connect to %s: %s", self._filename, e)
            return False

    def destroy(self):
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
        logger.info("Destroy the socket %s", self.filename)
        for listener in self._listeners:
            listener.send(RouterEvent(self._id, RouterEventType.MPV_INSTANCE_REMOVED))

    def close(self):
        if self.connected:
            self._socket.close()
            self._connected = False

    def _notify(self, raw_messages: str):

        for raw_msg in raw_messages.split('\n'):
            data = json.loads(raw_msg)
            if not self._sync_send_event.is_set() and 'error' in data:
                self._last_not_mpv_event_data = data
                self._sync_send_event.set()
            msg = Message(self._id, data)

            if len(self._listeners):
                logger.debug("Message send to %s listeners", len(self._listeners))

            for listener in self._listeners:
                listener.send(msg)

    def run(self):
        response = b''
        while 1:
            chunk = self._socket.recv(256)
            if not chunk:
                break

            response += chunk

            if response.endswith(b'\n'):
                self._notify(response.decode().strip())
                response = b''

        # connection closed, removing
        self.destroy()

    def send(self, data: dict, wait_for_response: bool):
        if not self.connected:
            raise SocketSendError("Socket is not connected")

        msg = json.dumps(data)

        logger.debug("Send data: %s to %s", msg, self._filename)

        msg += '\n'

        try:
            self._sync_send_event.clear()
            self._socket.sendall(msg.encode())
            if wait_for_response:
                self._sync_send_event.wait(30)
                return self._last_not_mpv_event_data
        except BrokenPipeError as e:
            logger.error("Cannot send data because: %s", e)
            raise SocketSendError("Cannot send data because: %s" % e)

    def __repr__(self):
        return "<SocketHandler filename: '%s', connected: %s>" % (self._filename, self.connected)
