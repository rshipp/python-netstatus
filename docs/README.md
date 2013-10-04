Auto-generated plain text documentation files for humans. 

python-netstatus
================

The general class structure of this project is:

    Host (class netstatus.host.Host)
    |
    | boolean getStatus()
    |
    | dict getResponse()
    |
    | void addService(name, serviceObject)

    Services (package netstatus.services)
    |
    | Server (abstract class netstatus.services.server.Server)
    | | 
    | | boolean getResponse()
    | |
    | | dict getResponse()
    | |
    | | HTTPServer (class netstatus.services.httpserver.HTTPServer)
    | | |
    | | | HTTPSServer (class netstatus.services.httpsserver.HTTPSServer)
    | |
    | | SQLServer (abstract class netstatus.services.sqlserver.SQLServer)
    | | |
    | | | MSSQLServer (class netstatus.services.mssqlserver.MSSQLServer)
    | | |
    | | | PGSQLServer (class netstatus.services.pgsqlserver.PGSQLServer)
