from Connectors import OraConnector
from Connectors import OraBuilder
if __name__ == "__main__":
     x=OraConnector.OraConnector("C:\instantclient_19_20","p1", "192.168.10.90", "RTXBCC", "1521", "SYSADM", "SYSADM")
     builder= OraBuilder.BuilderConnectors()
     builder.add_connection( "ora_one" ,x.dbconn)
     print(builder.list_connection_name())
     print(builder.list_connection_object())
     print("connected")