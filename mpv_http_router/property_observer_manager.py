import logging
from collections import defaultdict

from .mpv.listener_base import ListenerBase, Message
from .mpv.socket_watcher import SocketWatcher
from .mpv.socket_handler import RouterEventType

logger = logging.getLogger(__name__)

class PropertyObserverManager(ListenerBase):

    def __init__(self, socket_watcher: SocketWatcher):
        self._socket_watcher = socket_watcher
        self._observed_props = defaultdict(list)

    def observe(self, id, properties) -> list:
        new_props = []

        for prop in properties:
            if prop not in self._observed_props[id]:
                new_props.append(prop)

        if new_props:
            logger.info("Observe properties at %s: %s", id, new_props)
            self._observed_props[id] += new_props
            for prop in new_props:
                oidx = self._observed_props[id].index(prop)
                self._socket_watcher.send(Message(id, {"command": ["observe_property", oidx, prop]}))

        return new_props

    def send(self, message: Message):
        if isinstance(message.data, dict) and \
           message.data.get('routerevent') == RouterEventType.MPV_INSTANCE_REMOVED.value and \
           message.id in self._observed_props:
            del self._observed_props[message.id]
