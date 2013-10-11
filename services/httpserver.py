"""
services.httpserver.HTTPServer
This class provides functionality for checking the availability of HTTP
web services.

The optional 'hostname' argument can be set to change the HTTP Host
header. By default, it will be set to self.ip.
"""

import requests
from netstatus.services.server import Server

class HTTPServer(Server):
    def __init__(self, host, port=80, path="/", hostname=None):
        super(HTTPServer, self).__init__(host, port)
        self.path = path
        if hostname == None:
            self.hostname = host.ip
        else:
            self.hostname = hostname
        self.httpstring = "http://"

    def getStatus(self):
        """
        Returns a boolean value depending on the HTTP error code
        reported by the server. HTTP status responses from 100-399 will
        result in a return value of True, while status codes greater
        than 400 (error) or less than 100 (not defined by HTTP
        standards) will result in a return value of False.
        """
        super(HTTPServer, self).getStatus()

        # Construct the request data
        url = self.httpstring + self.ip + ":" + str(self.port) + self.path
        headers = {'Host': self.hostname}

        try:
            response = requests.get(url, headers=headers)
        except:
            # Probably a network error.
            return False

        self._Response = response.headers
        self._Response['status'] = response.status_code
        self._Response['text'] = response.text

        if response.status_code != None and response.status_code >= 100 and response.status_code <= 399:
            return True
        else:
            return False
