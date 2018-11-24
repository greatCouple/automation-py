# -- coding: utf-8 --
import sys

from src.utils.constant import const
from src.utils.Log import GetLog
from src.utils.ConductButton import ConductButton
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AccountManagement import AccountManagement
from src.utils.ProjectPath import Path


def transferArgv():
    if len(sys.argv) < 3:
        print("Invalid parameters,please enter 2 parameters!")
        exit()

    number1 = sys.argv[1]
    number2 = sys.argv[2]
    return [number1, number2]


class AccountSetting:
    def __init__(self):
        # 管理员登陆
        LoginAndLogout().loginAdmin()
        ConductButton().clickButton(const.btn_AccountSetting)  # 点击账户设置
        self.logFile = Path().logPath('AccountSetting')

    def addTrainer(self, trainerTimes, trainerConfig):
        for m in range(int(trainerTimes)):
            GetLog().log(self.logFile, "counter: " + str(m))
            AccountManagement().deleteAll()
            GetLog().log(self.logFile, "Delete all the trainers!")
            AccountManagement().createAccount("Maggie", "13652456845")
            AccountManagement().createAccount("Kitty", "18245623578")
            AccountManagement().createAccount("Cici", "15254623548")
            AccountManagement().createAccount("Tom", "13145684615")

    def addUser(self, userTimes):
        ConductButton().clickButton(const.btn_tab_user)  # 切换到学员添加界面
        for n in range(int(userTimes)):
            GetLog().log(self.logFile, "counter: " + str(n))
            AccountManagement().deleteAll()
            GetLog().log(self.logFile, "Delete all the users!")
            AccountManagement().createAccount("Jeff", "15245879523")
            AccountManagement().createAccount("Jimi", "18245796583")
            AccountManagement().createAccount("Tomas", "15212548565")
            AccountManagement().createAccount("Jane", "15245898745")

    def run(self, trainerTimes, userTimes):
        self.addTrainer(trainerTimes)
        self.addUser(userTimes)


if __name__ == "__main__":
    AccountSetting().manageAccount(2, 2)
