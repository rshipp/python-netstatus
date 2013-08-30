"""
Defines the NetworkObject class.
This is the base class from which all network objects defined by the
user should descend.
"""

class NetworkObject():
   
    def __init__():
        # Constructor
        pass

    def ping(self):
        """
        Send a single ICMP echo request (8).
        Returns True if an ICMP response (4) is recieved from the
        pinged host, and False otherwise.

        NOTE: Pinging in Python will open a raw socket, and requires
        root/Administrator permissions. The Ping class will raise
        socket.error if you don't have the proper permissions.
        """

