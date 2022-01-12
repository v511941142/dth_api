from config import setting
from pymysql import connect, cursors
from pymysql.err import OperationalError
import configparser as cparser

cf = cparser.ConfigParser()
cf.read(setting.TEST_CONFIG, encoding='UTF-8')
host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')
db = cf.get('mysqlconf', 'db_name')


class DB:
    def __init__(self):
        try:
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)

        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def close(self):
        self.conn.close()

    def select(self, sql, key):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchone()[key]

    def __del__(self):
        self.close()


if __name__ == '__main__':
    d = DB()
    print(d.select('SELECT headers FROM test_data WHERE id = "login_001";', 'headers'))
