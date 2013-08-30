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
    myDevice = networkobject.NetworkObject("192.168.1.1")
    if myDevice.ping():
        print "%s is up (replied to an ICMP request)" % myDevice.ip
    else:
        print "%s is down (no response to ICMP request)" % myDevice.ip

if __name__ == "__main__":
    main(sys.argv)
