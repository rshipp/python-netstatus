"""
services.pgsqlserver.PGSQLServer
This class provides functionality to check the availability of
PostgreSQL servers.
"""

from services.sqlserver import SQLServer

class PGSQLServer(SQLServer):
    def __init__(self, host, port=5432, user=None, password=None):
        super(PGSQLServer, self).__init__(host, port, user, password)

    def getStatus(self, **kwargs):
        """
        Returns a boolean value depending on
        """
        super(PGSQLServer, self).getStatus()
        return None
