import cx_Oracle as cx

class BuilderConnectors():
    NAME_LIST_CONNECTION=None
    LIST_CONNECTION=None
    LOCALDRIVER=None
    def __init__(self,x):
         self.LOCALDRIVER=x
         cx.init_oracle_client(lib_dir=self.LOCALDRIVER)
         self.NAME_LIST_CONNECTION =[]
         self.LIST_CONNECTION =[]

    # creats new connection
    def add_connection(self,name, con):
        self.NAME_LIST_CONNECTION.append(name)
        self.LIST_CONNECTION.append(con)

    def list_connection_name(self):
        return self.NAME_LIST_CONNECTION 
    
    def list_connection_object(self):
        return self.LIST_CONNECTION 

    # For explicitly opening database connection
    def free_connection(self):
        return self.dbconn

    