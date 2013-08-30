"""
Network status
Obtain and report information about the availability of network
devices and services, in a portable and extensible way.
"""

import sys

import config
import networkobject
import objects

def main(args):
    """Run the module as a script."""
    print "Running as a script - this is just an example..."
    airuh2 = networkobject.NetworkObject("192.168.1.62")
    if airuh2.ping():
        print "airuh2 is up (replied to an ICMP request)"
    else:
        print "airuh2 is down (no response to ICMP request)"

if __name__ == "__main__":
    main(sys.argv)
