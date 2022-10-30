import psycopg2
from pandas import DataFrame

__all__ = ['Hook']
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
          instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

# Here is a class to excute queries on postgres
@singleton
class Hook():
    def __init__(self,db_param={},schema = "pg_catalog"):
        self.__conn_param = db_param
        self.con = psycopg2.connect(**self.__conn_param)
        self.schema = schema
        
    def getConn(self):
        return self.con       
    
    def cur(self,q):
        """
        This function run a query!
        """
        try:
            cur = self.con.cursor()
            cur.execute("rollback")
        except:
            self.con = psycopg2.connect(**self.__conn_param)
            cur = self.con.cursor()
        cur.execute("set search_path to '{}';".format(self.schema))
        cur.execute(q)
        self.con.commit()
        return cur
    
    def run(self,q):
        try:
          dt = self.cur(q).fetchall()
        except:
          dt = []
        return dt
    
    def value(self,q):
        return self.run(q)[0][0]
    
    def get(self,q):
        resoverall = self.cur(q)
        df = DataFrame(resoverall.fetchall())
        df.columns = [desc[0] for desc in resoverall.description]
        return df