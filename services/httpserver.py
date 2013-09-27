"""
services.httpserver.HTTPServer
This class provides functionality for checking the availability of HTTP
web services.

The optional 'host' argument can be set to change the HTTP Host header.
By default, it will be set to self.ip.
"""

import sys, httplib

class HTTPServer(object):
    def __init__(self, ip, port=httplib.HTTP_PORT, host=None):
        networkobject.NetworkObject.__init__(self, ip)
        self.port = port
        if host == None:
            self.host = self.ip
        else:
            self.host = host
        self._HTTPResponse = None

    def getStatus(self, path="/", strict=True):
        """
        Returns a boolean value depending on the HTTP error code
        reported by the server. HTTP status responses from 100-399 will
        result in a return value of True, while status codes greater
        than 400 (error) or less than 100 (not defined by HTTP
        standards) will result in a return value of False.

        By default, responses that cannot be parsed as valid HTTP/1.0 or
        1.1 will also cause this function to return False. To change
        this behavior, call this function with strict=False. Eg:

        >>> h = myhttpserverobject.HTTPRequest("/", False)

        The last case in which this function will return False is if a
        network error occurs (for example, the server is down, or the
        client is not on the network). In this situation, the value of
        the HTTP response instance variable (see below) will NOT be
        changed.

        This function also sets/changes the value of an
        instance variable to include information about the HTTP
        response. This information can be accessed publicly in the form
        of a getter member function that returns an HTTPResponse object.
        See getHTTPResponse().
        """
        try:
            http = httplib.HTTPConnection(self.ip, self.port)
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
