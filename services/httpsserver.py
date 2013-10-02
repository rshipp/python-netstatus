"""
services.httpserver.HTTPServer
This class provides functionality for checking the availability of HTTP
web services.

The optional 'host' argument can be set to change the HTTP Host header.
By default, it will be set to self.ip.
"""

import sys, httplib
from services.httpserver import HTTPServer

class HTTPSServer(HTTPServer):
    def __init__(self, host, port=httplib.HTTPS_PORT, hostname=None):
        """
        We are only overriding init to provide a better default
        port.
        """
        super(HTTPSServer, self).__init__(host, port, hostname)

    def getStatus(self, path="/", strict=True):
        """
        See HTTPServer.getStatus() for documentation.
        """
        try:
            http = httplib.HTTPSConnection(self.ip, self.port)
            http.request("GET", path, headers={"Host": self.host})
            response = http.getresponse()
        except:
            # Probably a network error.
            return False

        self._HTTPResponse = response

        if response != None and response.status >= 100 and response.status <= 399:
            return True
        else:
            return False


    def getResponse():
        """
        A 'getter' method that returns an HTTPResponse object containing
        (possibly) useful information about the HTTP server's last
        response. Note that only the most recent response is available.

        For information about HTTPResponse objects, refer to the Python
        httplib documentation, available online as:
        http://docs.python.org/2/library/httplib.html?highlight=httplib#httpresponse-objects

        The most useful information will probably be:
        HTTPResponse.status        Status code returned by server
        HTTPResponse.read()        Reads and returns the response body
        HTTPResponse.getheader()   Returns a list of (header, value) tuples
        """
        return  self._HTTPResponse
