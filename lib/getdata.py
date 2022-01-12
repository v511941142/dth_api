import configparser as cparser
from lib.readexcel import ReadExcel
from config import setting
from db_fixture.mysql_db import DB

cf = cparser.ConfigParser()
cf.read(setting.TEST_CONFIG, encoding='UTF-8')

# SIT/UAT测试,切换此参数即可
environment = cf.get('environment', 'sit')
id = int(cf.get('index', 'id'))
case = int(cf.get('index', 'case'))
url = int(cf.get('index', 'url'))
method = int(cf.get('index', 'method'))
headers = int(cf.get('index', 'headers'))
data = int(cf.get('index', 'data'))
expect = int(cf.get('index', 'expect'))
isRun = int(cf.get('index', 'isRun'))


class GetData():
    def __init__(self):
        self.re = ReadExcel(setting.TARGET_FILE)
        self.db = DB()

    def getIsRun(self, row):
        return self.re.read_data(row)[isRun]

    def getId(self, row):
        return self.re.read_data(row)[id]

    def getCase(self, row):
        return self.re.read_data(row)[case]

    def getUrl(self, row):
        return environment + self.re.read_data(row)[url]

    def getMethod(self, row):
        return self.re.read_data(row)[method]

    def getHeaders(self, row):
        h = self.re.read_data(row)[headers]
        if h:
            # h = ''
            # if self.re.read_data(row)[headers]:
            sql = 'SELECT headers FROM test_data WHERE id = "%s";' % self.getId(row)
            h = eval(self.db.select(sql, 'headers'))
        return h

    def getData(self, row):
        d = self.re.read_data(row)[data]
        if d:
            sql = 'SELECT data FROM test_data WHERE id = "%s";' % self.getId(row)
            d = eval(self.db.select(sql, 'data'))
        return d

    def getExpect(self, row):
        sql = 'SELECT expect_result FROM test_data WHERE id = "%s";' % self.getId(row)
        return eval(self.db.select(sql, 'expect_result'))

    def getRows(self):
        return self.re.nrows


if __name__ == '__main__':
    g = GetData()
    # print(g.getIsRun(2))
    # print(g.getId(2))
    # print(g.getCase(2))
    # print(g.getUrl(2))
    # print(g.getMethod(2))
    # print(g.getHeaders(2))
    # print(g.getData(1))
    print(g.getExpect(2))
    # print(g.getRows())
