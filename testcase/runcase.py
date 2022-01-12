from lib.getdata import GetData
from lib.sendrequest import SendRequest
from lib.assertresult import AssertResult
from lib.writeexcel import WriteExcel

class RunCase():
    def __init__(self):
        self.g = GetData()
        self.s = SendRequest()
        self.a = AssertResult()
        self.w = WriteExcel()

    def runCase(self):
        for i in range(1, self.g.getRows()):
            isRun = self.g.getIsRun(i)
            if isRun.upper() == 'N':
                continue
            id = self.g.getId(i)
            case = self.g.getCase(i)
            url = self.g.getUrl(i)
            method = self.g.getMethod(i)
            headers = self.g.getHeaders(i)
            data = self.g.getData(i)
            expect = self.g.getExpect(i)
            result = self.s.sendRequest(method, url, data, headers)
            res = self.a.assertEqual(result,expect)
            self.w.write_data(i,res)


if __name__ == '__main__':
    r = RunCase()
    r.runCase()
