"""
services.server.Server

A simple base (abstract) class to outline how services should be
implemented.
"""

class Server(object):
    def __init__(self, host, port):
        """
        init must be passed a host object as its first parameter,
        because it needs the IP (more information from the host object
        may be used depending on the specific service in question.)
        TODO: Is there some way we can avoid this?
        """
        self.ip = host.ip
        self.port = port
        self._Response = None

    def getStatus(self):
        """
        Attempts to determine the status of the service in some way, and
        returns a boolean value.

        Note that getStatus() only accepts kwargs, meaning all getStatus
        implementations should have reasonable defaults and accept only
        optional arguments. When implementing getStatus, always be sure
        to keep the signature the same, so the method is properly
        overridden. If other information is needed to check the status
        of a server (username, password, etc), use arguments in the
        constructor, not in getStatus(). (Optional arguments to
        getStatus should be to help you check the status of a certain
        resource, not the server itself.)

        The last case in which this function should return False is if a
        network error occurs (for example, the server is down, the
        client is not on the network, or there was a timeout). In this
        situation, getResponse() should return None.

        This function should also set/change the value of an instance
        variable to include information about the response. Response
        information will be accessed publicly in the form of a getter
        member function (self.getResponse()) that returns a dictionary
        of useful information.
        """
        self._Response = None
        # To avoid confusion, this method returns None, as it is not
        # implemented. All implementations of getStatus should have a
        # boolean return type.
        return None

    def getResponse():
        """
        A 'getter' method that returns a dictionary of (possibly) useful
        information about the server's last response. Note that only the
        most recent response is available. As long as the _Response
        variable is used, this function should not need to be
        overwritten.
        """
        return  self._Response
