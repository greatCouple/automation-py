import xlrd,os
from src.utils.ProjectPath import work_path

file_path = work_path + "\\testcase\\"
print (file_path)

file1 = xlrd.open_workbook('F:\\Appium_python3\\tescase\\TestCase.xls')
sheet = file1.sheet_by_name('StressTest')
scriptName1 = sheet.cell(1,2).value
print (int(scriptName1))

file_name = file_path + 'TestCase.xls'
print (file_name)
file = xlrd.open_workbook(file_name)
sheet = file.sheet_by_name('StressTest')
scriptName = sheet.cell(1,2).value
print (scriptName)


