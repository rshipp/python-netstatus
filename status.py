"""
Network status
Obtain and report information about the availability of network
devices and services, in a portable and extensible way.
"""

import sys

import config
#import objects
from objects import networkobject, httpserver

def main(args):
    """Run the module as a script."""
    try:
        host = args[1]
    except:
        host = "192.168.1.1"

    print "Running as a script - this is just an example..."
    myDevice = networkobject.NetworkObject(host)
    if myDevice.ping():
        print "%s is up via ICMP" % myDevice.ip
    else:
        print "%s is down via ICMP" % myDevice.ip

    myHTTPDevice = httpserver.HTTPServer(host)
    if myHTTPDevice.HTTPRequest():
        print "%s is up via HTTP" % myHTTPDevice.ip
    else:
        print "%s is down via HTTP" % myHTTPDevice.ip
            
        
if __name__ == "__main__":
    main(sys.argv)
