import xlrd,os
from src.utils.ProjectPath import work_path

class ReadExcel:
    file_path = work_path + "\\testcase\\"
    xlrd.Book.encoding = "utf8"
    file_name = file_path + 'TestCase.xls'
    file = xlrd.open_workbook(file_name)

    def readExcel(self, sheetname):
        global file
        list = []
        self.sheet = file.sheet_by_name(sheetname)
        self.rows_num = self.sheet.nrows  # 读取总行数
        list.append(self.rows_num)
        self.cols_num = self.sheet.ncols  # 读取列列数
        list.append(self.cols_num)
        print (list)
        return list

if __name__ == "__main__":
    file_path = work_path + "\\testcase\\"
    xlrd.Book.encoding = "utf8"
    file_name = file_path + 'TestCase.xls'
    file = xlrd.open_workbook(file_name)
    sheet = file.sheet_by_name('StressTest')
    list = ReadExcel().readExcel('StressTest')
    rows_num = list[0]
    cols_num = list[1]
    for i in range(1, rows_num):
        name = sheet.cell(i, 0).value
        name1 = sheet.cell(i, 1).value
        name1 = int(name1)
        Script_name = name + '\t' + str(name1)
        print(Script_name)
        os.system(Script_name)
