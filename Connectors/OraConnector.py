import cx_Oracle as cx
import json

class OraConnector():
    OBJECT_SRC=None
    UID_SRC = None
    PWD_SRC = None
    URI_SRC = None
    PRT_SRC = None
    SID_SRC = None
    DSN=None
    dbconn = None

    def __init__(self,name, ip, dbname, port, user, password):
        self.OBJECT_SRC=name
        self.UID_SRC = user
        self.PWD_SRC = password
        self.URI_SRC = ip
        self.PRT_SRC = port
        self.SID_SRC = dbname
        self.DSN=None
        self.dbconn = None
        self.JSON_CON=None
        self.create_connection()

    # creats new connection
    def create_connection(self):
         self.DSN = cx.makedsn(self.URI_SRC, self.PRT_SRC, self.SID_SRC)
         self.dbconn=cx.connect(user=self.UID_SRC, password=self.PWD_SRC, dsn=self.DSN, encoding='UTF-8')
         self.JSON_CON = {
                            "OBJECT_SRC": "{}".format(self.OBJECT_SRC),
                            "UID_SRC": "{}".format(self.UID_SRC),
                            "PWD_SRC": "{}".format(self.PWD_SRC),
                            "URI_SRC": "{}".format(self.URI_SRC),
                            "PRT_SRC": "{}".format(self.PRT_SRC),
                            "SID_SRC": "{}".format(self.SID_SRC),
                            "x":"pointx",
                            "y":"pointy"
                        }
         self.save()
         return (self.dbconn)

    # For explicitly opening database connection
    def __enter__(self):
        return self.dbconn

    def __exit__(self):
        self.dbconn.close()

    def save(self):
        json_object = json.dumps(self.JSON_CON, indent=4)
        with open("Config/Components/{}.json".format(self.OBJECT_SRC), "w") as outfile:
            outfile.write(json_object)