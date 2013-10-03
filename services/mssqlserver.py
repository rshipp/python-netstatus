"""
services.mssqlserver.MSSQLServer
This class provides functionality to check the availability of
Microsoft SQL servers.
"""

from services.sqlserver import SQLServer

class MSSQLServer(SQLServer):
    def __init__(self, host, port=1433, user=None, password=None):
        super(MSSQLServer, self).__init__(host, port, user, password)

    def getStatus(self, **kwargs):
        """
        Returns a boolean value depending on
        """
        super(MSSQLServer, self).getStatus()
        return None
