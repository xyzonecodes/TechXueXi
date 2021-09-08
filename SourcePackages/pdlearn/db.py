import pdlearn.globalvar as gl
from pdlearn.utils.easy_sqlite import EasySqlite

 #设置数据量
db ="" #数据库
username="" #用户名
password="" #密码


class MySqlLiteDB:

    def __init__(self, db,username="",password=""):
        self.db = EasySqlite(db)
        self.username = username
        self.password=password

    def selectQuestion(self,questionstr):        
        cursor=self.db.execute("select * from question where body='"+questionstr+"'", result_dict=False)
        print("根据题目查询记录:"+len(list(cursor)))
        return None

xuexiDB=MySqlLiteDB('db/xuexi.db')