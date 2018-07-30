from typing import List
import logging
from geventwebsocket.websocket import WebSocket

from mpv_http_router.message import Message

logger = logging.getLogger(__name__)

class WebsocketListener(object):

    def __init__(self, websocket: WebSocket):
        self._websocket = websocket
        self._remote_addr = websocket.environ.get('REMOTE_ADDR')

    @property
    def remote_addr(self) -> str:
        return self._remote_addr

    def send(self, message: Message):
        logger.debug("Send message: %s to %s", message, self.remote_addr)
        self._websocket.send(str(message))

WebsocketListenerList = List[WebsocketListener]
