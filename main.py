# -- coding: utf-8 --

from src.stress.LoginAndLogoutTrainer import LoginAndLogoutTrainer


def runCase(self, sheetName):
    self.caseList = self.readExcel(sheetName)
    map = {"LoginAndLogoutTrainer.py": LoginAndLogoutTrainer()}
    for case in self.caseList:
        if case[1] != 0 & case[2] != 0:
            map.get(case[0]).run(case[1], case[2])
        if case[1] == 0 & case[2] != 0:
            map.get(case[0]).run(case[2])
        if case[1] != 0 & case[2] == 0:
            map.get(case[0]).run(case[1])