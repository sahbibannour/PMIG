

class OraExtractor():
    columns=None
    table=None
    processes_number=None
    oracle_hint=None
    threads=None
    query=None
    dbconn = None

    def __init__(self,columns,table,processes_number,oracle_hint,threads,query,con):
        self.columns=columns
        self.table=table
        self.processes_number=processes_number
        self.oracle_hint=oracle_hint
        self.threads=threads
        self.query=query
        self.dbconn = con

    def run(self):
        print("starting extraction data")


    def run(self):
        print("stoping extraction data")