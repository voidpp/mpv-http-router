import logging
import os
import select
from select import kevent, kqueue
from threading import Thread

from .base import DirectoryWatcherBase

logger = logging.getLogger(__name__)

class DirectoryWatcherKevent(DirectoryWatcherBase, Thread):

    def start_watch(self):
        self.start()

    def run(self):
        logger.info("Start watch %s", self._directory)

        fd = os.open(self._directory, os.O_DIRECTORY)
        kq = kqueue()
        event = [
            kevent(fd, select.KQ_FILTER_VNODE, select.KQ_EV_ADD | select.KQ_EV_CLEAR, select.KQ_NOTE_WRITE),
        ]
        events = kq.control(event, 0, 0)

        while True:
            r_events = kq.control(None, 5)
            for event in r_events:
                self._on_change()
