"""
services.pgsqlserver.PGSQLServer
This class provides functionality to check the availability of
PostgreSQL servers.
"""

from netstatus.services.sqlserver import SQLServer
import psycopg2

class PGSQLServer(SQLServer):
    def __init__(self, host, port=5432, user=None, password=None,
            database=None):
        super(PGSQLServer, self).__init__(host, port, user, password)
        self.database = database

    def getStatus(self, **kwargs):
        """
        Returns a boolean value depending on whether a successful login
        can be performed on the server.
        """
        super(PGSQLServer, self).getStatus()

        try:
            conn = psycopg2.connect(host=self,host, port=self.port,
                    user=self.user, password=self.password,
                    database=self.database)
            cur = conn.cursor()
            conn.close()
        except:
            return False

        return True
