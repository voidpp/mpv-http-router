import socket
import logging
from zeroconf import ServiceInfo, Zeroconf

logger = logging.getLogger(__name__)

class ZeroconfService():

    def register(self, port: int):

        self._zeroconf = Zeroconf()

        hostname = socket.gethostname()

        host = socket.gethostbyname(hostname)

        desc = {
            'host': host,
            'port': str(port),
            'hostname': hostname,
        }

        self._info = ServiceInfo("_mpv-http-router._tcp.local.",
                                 "MPV HTTP Router._mpv-http-router._tcp.local.",
                                 socket.inet_aton(host), port, 0, 0, desc)

        self._zeroconf.register_service(self._info)

        self._registered = True

        logger.info("MPV HTTP Router has been registered in the network on %s", port)


    def unregister(self):
        if self._zeroconf is None:
            return
        self._zeroconf.unregister_service(self._info)
        self._zeroconf.close()
        self._registered = False
        logger.info("MPV HTTP Router has been unregistered")
