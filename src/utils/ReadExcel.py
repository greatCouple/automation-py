import xlrd, os
from ProjectPath import work_path


class ReadExcel:
    def __init__(self):
        self.file_path = work_path + "\\testcase\\"
        xlrd.Book.encoding = "utf8"
        self.file_name = self.file_path + 'TestCase.xls'
        if os.path.exists(self.file_name):
            pass
        else:
            raise FileNotFoundError('测试用例不存在')
        self._data = []

    def readExcel(self, sheetName):
        self.file = xlrd.open_workbook(self.file_name)
        self.sheet = self.file.sheet_by_name(sheetName)
        self.rows_num = self.sheet.nrows  # 读取总行数
        self.cols_num = self.sheet.ncols  # 读取列列数
        for i in range(1, self.rows_num):
            self.case = self.sheet.cell(i, 0).value
            self.firstArg = self.sheet.cell(i, 1).value
            self.secondArg = self.sheet.cell(i, 1).value
            self.firstArg = int(self.firstArg)
            self.secondArg = int(self.secondArg)
            self._data.append([self.case, self.firstArg, self.secondArg])
        return self._data



