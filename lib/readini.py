import configparser as cparser
from config import setting


class ReadIni():
    def __init__(self):
        self.cf = cparser.ConfigParser()
        self.cf.read(setting.TEST_CONFIG, encoding='UTF-8')

