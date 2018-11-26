from src.stress.LoginAndLogoutTrainer import LoginAndLogoutTrainer
from src.stress.AccountSetting import AccountSetting
from src.stress.WireModeDoExercise import WireModeDoExercise
from src.stress.FCT import FunctionTest
from src.stress.NFCPair1 import NFCPair1
from src.stress.NFCPair2 import NFCPair2
from src.stress.NFCPair3 import NFCPair3
from src.utils.ReadExcel import ReadExcel


def runCase(sheetName):
    caseList = ReadExcel().readExcel(sheetName)
    map = {"AccountSetting": AccountSetting, "WireModeDoExercise": WireModeDoExercise, "FCT": FunctionTest,"LoginAndLogoutTrainer": LoginAndLogoutTrainer, "NFCPair1": NFCPair1, "NFCPair2": NFCPair2, "NFCPair3": NFCPair3}
    for case in caseList:
        if case[1] != 0 or case[2] != 0:
            map.get(case[0])().run(case[1], case[2])


if __name__ == "__main__":
    runCase('StressTest')
