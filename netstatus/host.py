"""
Defines the Host class.
"""

from ping import Ping


class NameConflictError(Exception):
    pass


class Host(object):
    def __init__(self, ip):
        self._pingResponse = None
        self._Services = []
        self.ip = ip

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except KeyError as e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def getStatus(self):
        """
        Send a single ICMP echo request.

        Returns True if an ICMP response is recieved from the
        pinged host, and False otherwise.

        This function also sets/changes the value of self._pingResponse
        to include information about the ICMP response packet. This
        information can be accessed publicly in the form of a getter
        member function that returns a dictionary. See
        getResponse().

        NOTE: Pinging in Python will open a raw socket, and requires
        root/Administrator permissions. The Ping class will raise
        socket.error if you don't have the proper permissions.
        """
        ping = Ping(self.ip)
        self._pingResponse = ping.do()
        
        if self._pingResponse == None:
            return False
        else:
            return True

    def getResponse(self):
        """
        A 'getter' method that returns a dictionary of (possibly) useful
        information about the last ping response. Note that only
        information about the most recent response is stored. If
        self.getStatus() has not already been called, this function will
        return the default value of the object used to store ping
        response information, None.

        >>> myHost.getResponse()
        >>> myHost.getStatus()
        True
        >>> myHost.getResponse()
        {'delay': delay, 'ip': ip, 'packet_size': packet_size, 'ip_header': ip_header, 'icmp_header': icmp_header}
        >>> myHost.getResponse()['delay']
        delay
        """
        return self._pingResponse

    def addService(self, name, service):
        """Add a service object to your host, with the specified name.
           Example:

           >>> myHost = host.Host('127.0.0.1')
           >>> myHTTPService = services.httpserver.HTTPServer(myHost)
           >>> myHost.addService("http", myHTTPService)
           >>> myHost.http.getStatus()
           True
           >>> myHost.http.getResponse()
           {'foo': 'bar'}

           Raises host.NameConflictError if a 'name' attribute already
           exists in the host object.

           >>> myHost.addService("http", myOtherHTTPService)
           Traceback (most recent call last):
               ...
           host.NameConflictError: Member variable self.http cannot be assigned because that name is taken.

           Note: 'name' MUST be a string, or be able to be converted to
           a string with str(name).
        """
        # self.__getattr__() raises AttributeError if it cannot find
        # 'self.name', but since we just want to make sure 'self.name'
        # doesn't exist, we will throw our own exception if __getattr__
        # succeeds. If __getattr__ fails, then we know self.name does
        # not exist, so we catch AttributeError and create self.name.
        # This just helps stop the user from overwriting member
        # variables we need, like self._pingResponse.
        try:
            self.__getattr__(str(name))
            raise NameConflictError("Member variable self.%s cannot be assigned because that name is taken." %
                    (name))
        except AttributeError:
            self.__setattr__(str(name), service)
            self._Services += [str(name)]

    def getServices(self):
        """Returns a list of services added to the host."""
        return self._Services

    def getService(self, serviceName):
        """Return the service object with the specified name."""
        if serviceName in self._Services:
            return self.__getattr__(serviceName)
        else:
            raise AttributeError("No such service: %s." % serviceName)
