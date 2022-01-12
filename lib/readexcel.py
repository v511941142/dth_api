import xlrd


class ReadExcel():
    def __init__(self, fileName, SheetName='Sheet1'):
        self.data = xlrd.open_workbook(fileName)
        self.table = self.data.sheet_by_name(SheetName)
        self.nrows = self.table.nrows

    def read_data(self, row):
        try:
            return self.table.row_values(row)
        except:
            print('获取excel数据失败')


if __name__ == '__main__':
    r = ReadExcel(r'D:\1dth\Project\dth_api\report\excelReport\APITestCase.xlsx')
    r.read_data(1)
