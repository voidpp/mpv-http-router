
from watchdog.events import FileSystemEventHandler, FileCreatedEvent, FileDeletedEvent
from watchdog.observers import Observer

import logging
import os

from .base import DirectoryWatcherBase

logger = logging.getLogger(__name__)

class DirectoryWatcherWatchdog(DirectoryWatcherBase, FileSystemEventHandler):

    def start_watch(self):
        observer = Observer()
        observer.schedule(self, self._directory)
        observer.start()

    def on_created(self, ev):
        self._on_change()

    def on_deleted(self, ev):
        self._on_change()
