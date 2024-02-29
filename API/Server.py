from flask import Flask, make_response
from Connectors import OraConnector
from Connectors import OraBuilder
app = Flask(__name__)


@app.route("/Connectors" )
def home():
    builder= OraBuilder.BuilderConnectors("C:\instantclient_19_20")
    x=OraConnector.OraConnector("p1", "192.168.10.90", "RTXBCC", "1521", "SYSADM", "SYSADM")
    x1=OraConnector.OraConnector("p2", "192.168.10.90", "RTXBCC", "1521", "SYSADM", "SYSADM")
    builder.add_connection( "ora_one" ,x.dbconn)
    builder.add_connection( "ora_two" ,x1.dbconn)
    print(builder.list_connection_name())
    print(builder.list_connection_object())
    print("connected")
    return "hello there"
   

def start_server():
    app.run(host='0.0.0.0', port=81)