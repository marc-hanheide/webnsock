#!/usr/bin/env python

import webnsock
import web
from signal import signal, SIGINT
from os import path


class SimpleUIServer(webnsock.WebServer):

    def __init__(self):

        webnsock.WebServer.__init__(
            self,
            path.join(
                path.dirname(__file__),
                'www/test'
            )
        )

        self._renderer = web.template.render(
            path.realpath(
                path.join(
                    path.dirname(__file__),
                    'www'
                )
            ),
            base=None, globals=globals())

        self_app = self

        class Index(self.page):
            path = '/'

            def GET(self):
                return self_app._renderer.index()


class SimpleProtocol(webnsock.JsonWSProtocol):

    def __init__(self):
        super(SimpleProtocol, self).__init__()

    def onOpen(self):
        pass

    def on_ping(self, payload):
        return {'result': True}


def main():
    webserver = webnsock.Webserver(SimpleUIServer())
    backend = webnsock.WSBackend(SimpleProtocol)
    signal(SIGINT,
           lambda s, f: webnsock.signal_handler(webserver, backend, s, f))
    webserver.start()
    backend.talker()


if __name__ == "__main__":
    main()
