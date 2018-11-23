import xlrd,os
from src.utils.ProjectPath import work_path
#from src.stress.LoginAndLogoutTrainer import LoginAndLogoutTrainer
#from src.stress.AccountSetting import AccountSetting

class ReadExcel:
    file_path = work_path + "\\testcase\\"
    xlrd.Book.encoding = "utf8"
    file_name = file_path + 'TestCase.xls'

    def __init__(self):
        if os.path.exists(self.file_name):
            pass
        else:
            raise FileNotFoundError('测试用例不存在')
        self._data = []

    def readExcel(self, sheetname):
        self.file = xlrd.open_workbook(self.file_name)
        self.sheet = self.file.sheet_by_name(sheetname)
        self.rows_num = self.sheet.nrows  # 读取总行数
        self.cols_num = self.sheet.ncols  # 读取列列数
        for i in range(1,self.rows_num):
            case = self.sheet.cell(i, 0).value
            for j in range(1, self.rows_num):
                times = self.sheet.cell(j, 1).value
                times = int(times)
                self._data.append(dict(case, times))
        print(self._data)
        return self._data

 #   def runCase(self, caseList):
  #      map = {"LoginAndLogoutTrainer.py": LoginAndLogoutTrainer()}
  #      for case in caseList:
   #         if case[2] != 0:
   #             map.get(case[0]).run(case[1])


if __name__ == "__main__":
    ReadExcel().readExcel('StressTest')

