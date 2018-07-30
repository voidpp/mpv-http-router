import logging
import os
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class DirectoryWatcherBase(ABC):
    """
    Args:
        directory: the directory to watch
        on_change: call when a file in the directory is created or removed
    """

    def __init__(self, directory: str, on_change: callable):
        super().__init__()
        self._directory = directory
        self._on_change = on_change

    @abstractmethod
    def start_watch(self):
        pass

