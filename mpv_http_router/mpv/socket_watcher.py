import hashlib
import logging
import os
import re
import socket
from typing import Dict

from mpv_http_router.directory_watcher import DirectoryWatcher
from mpv_http_router.message import Message

from .socket_handler import SocketHandler
from .listener_base import ListenerList

logger = logging.getLogger(__name__)

def md5(data: str) -> str:
    m = hashlib.md5()
    m.update(data.encode())
    return m.hexdigest()

class SocketWatcher():

    def __init__(self, pattern: str, listeners: ListenerList):
        super().__init__()
        self._sockets: Dict[str, SocketHandler] = {}
        self._pattern = re.compile(pattern)
        self._base_path = os.path.dirname(pattern)
        self._listeners = listeners
        self._watcher = DirectoryWatcher(self._base_path, self._on_change)
        self._search()
        self._watcher.start()

    @property
    def id_list(self) -> list:
        return list(self._sockets.keys())

    def _on_change(self):
        self._clean()
        self._search()

    def __contains__(self, id: str):
        return id in self._sockets

    def _create_socket_handler(self, path: str):
        id = md5(path)

        if id in self._sockets:
            handler = self._sockets[id]
        else:
            handler = SocketHandler(id, path, self._listeners)
            self._sockets[id] = handler

        if not handler.connected:
            if handler.connect():
                handler.start()
            else:
                handler.destroy()

    def _search(self):
        logger.info("Searching for sockets in %s", self._base_path)
        for filename in os.listdir(self._base_path):
            file_path = os.path.join(self._base_path, filename)

            if self._pattern.match(file_path):
                self._create_socket_handler(file_path)

    def _clean(self):
        handlers_to_remove = []
        for id, handler in self._sockets.items():
            if not os.path.exists(handler.filename):
                handlers_to_remove.append(id)

        logger.info("Cleaning up socket handlers (%s)", len(handlers_to_remove))

        # somebody deleted the unix socket
        for id in handlers_to_remove:
            self._sockets[id].destroy()
            del self._sockets[id]

    def send(self, message: Message, wait_for_response = False):
        return self._sockets[message.id].send(message.data, wait_for_response)
