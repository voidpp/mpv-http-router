import logging
from abc import ABC, abstractmethod
from typing import List

from mpv_http_router.message import Message

class ListenerBase(ABC):

    @abstractmethod
    def send(self, message: Message):
        pass

ListenerList = List[ListenerBase]
