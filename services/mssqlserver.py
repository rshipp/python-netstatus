"""
services.mssqlserver.MSSQLServer
This class provides functionality to check the availability of
Microsoft SQL servers.
"""

from netstatus.services.sqlserver import SQLServer
import pymssql

class MSSQLServer(SQLServer):
    def __init__(self, host, port=1433, user=None, password=None,
            database=None):
        super(MSSQLServer, self).__init__(host, port, user, password)
        self.database = database

    def getStatus(self, **kwargs):
        """
        Returns a boolean value depending on whather a successful login
        can be performed on the server.
        """
        super(MSSQLServer, self).getStatus()
        
        try:
            conn = pymssql.connect(host=self.host, user=self.user,
                    password=self.password, database=self.database)
            cur = conn.cursor()
            conn.close()
        except:
            return False

        return True
