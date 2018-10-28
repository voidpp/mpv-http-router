import logging
from typing import List

from geventwebsocket.websocket import WebSocket

from .message import Message
from .mpv.listener_base import ListenerBase

logger = logging.getLogger(__name__)

class WebsocketListener(ListenerBase):

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
