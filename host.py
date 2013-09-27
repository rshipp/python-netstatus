"""
Defines the Host class.
This is the base class from which all service classes defined by the
user should descend.
"""

from ping.ping import Ping

class Host():
   
    def __init__(self, ip):
        self._pingResponse = None
        self.ip = ip

    def getStatus(self):
        """
        Send a single ICMP echo request.

        Returns True if an ICMP response is recieved from the
        pinged host, and False otherwise.

        This function also sets/changes the value of self.pingResponse
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

    def getResponse():
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
        return _pingResponse
