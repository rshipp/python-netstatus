"""
services.sqlserver.SQLServer
This abstract class provides a base framework for checking the
availability of SQL servers.
"""

from netstatus.services.server import Server

class SQLServer(Server):
    def __init__(self, host, port, user, password):
        super(SQLServer, self).__init__(host, port)
        self.user = user
        self.password = password

    def getStatus(self):
        """
        Returns a boolean value depending on whether some command can be
        executed on the server (and therefore that a successful login
        can be made). Each different SQL server will use whatever
        command makes the most sense for that server type. Note that
        least privilege is assumed, so (eg.) write access is never
        tested.

        THIS IS AN ABSTRACT METHOD! Be sure you are returning either
        True or False in your implementation.
        """
        super(SQLServer, self).getStatus()
        return None
