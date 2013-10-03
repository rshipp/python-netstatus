"""
services.httpsserver.HTTPSServer
This class provides functionality for checking the availability of HTTP
web services with SSL, including certificate verification.
"""

from services.httpserver import HTTPServer

class HTTPSServer(HTTPServer):
    def __init__(self, host, port=httplib.HTTPS_PORT, hostname=None):
        super(HTTPSServer, self).__init__(host, port)
        self.httpstring = "https://"
