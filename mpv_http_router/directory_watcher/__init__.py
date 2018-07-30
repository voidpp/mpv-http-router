"""
Holy mother of god.

There is a custom implementation of directory watching for MacOS here because of:

    - fsevents does not detect unix socket file creation
    - watchdog's kevent (kqueue) implementation is bad

"""
import platform

system = platform.system()

if system == 'Darwin':
    from .kevent import DirectoryWatcherKevent as DirectoryWatcher
else:
    from .watchdog import DirectoryWatcherWatchdog as DirectoryWatcher
