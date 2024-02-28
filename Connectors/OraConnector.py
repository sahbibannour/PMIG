import cx_Oracle as cx

class OraConnector():
    OBJECT_SRC=None
    LOCALDRIVER=None
    UID_SRC = None
    PWD_SRC = None
    URI_SRC = None
    PRT_SRC = None
    SID_SRC = None
    DSN=None
    dbconn = None

    def __init__(self,oraclient,name, ip, dbname, port, user, password):
        self.OBJECT_SRC=name
        self.LOCALDRIVER=oraclient
        self.UID_SRC = user
        self.PWD_SRC = password
        self.URI_SRC = ip
        self.PRT_SRC = port
        self.SID_SRC = dbname
        self.DSN=None
        self.dbconn = None
        self.create_connection()

    # creats new connection
    def create_connection(self):
         cx.init_oracle_client(lib_dir=self.LOCALDRIVER)
         self.DSN = cx.makedsn(self.URI_SRC, self.PRT_SRC, self.SID_SRC)
         self.dbconn=cx.connect(user=self.UID_SRC, password=self.PWD_SRC, dsn=self.DSN, encoding='UTF-8')
         return (self.dbconn)

    # For explicitly opening database connection
    def __enter__(self):
        return self.dbconn

    def __exit__(self):
        self.dbconn.close()