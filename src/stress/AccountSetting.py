# -- coding: utf-8 --
import sys

from src.utils.constant import const
from src.utils.LogUtil import LogUtil
from src.utils.ButtonManger import ButtonManger
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AccountManagement import AccountManagement
from src.utils.LogPath import Path
from src.utils.YamlUtil import YamlUtil


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
        ButtonManger.clickButton(const.btn_AccountSetting)  # 点击账户设置
        self.logFile = Path().getLogPath('AccountSetting')

    def addTrainer(self, trainerTimes):
        for m in range(int(trainerTimes)):
            LogUtil.log(self.logFile, "counter: " + str(m))
            AccountManagement().deleteAll()
            LogUtil.log(self.logFile, "Delete all the trainers!")
            trainers = YamlUtil.read('trainer')
            for key in trainers.keys():
                AccountManagement().createAccount(key, trainers.get(key))

    def addUser(self, userTimes):
        ButtonManger.clickButton(const.btn_tab_user)  # 切换到学员添加界面
        for n in range(int(userTimes)):
            LogUtil.log(self.logFile, "counter: " + str(n))
            AccountManagement().deleteAll()
            LogUtil.log(self.logFile, "Delete all the users!")
            users = YamlUtil.read('user')
            for key in users.keys():
                AccountManagement().createAccount(key, users.get(key))

    def run(self, trainerTimes, userTimes):
        LogUtil.log(self.logFile, "Start AccountSetting test !!!")
        self.addTrainer(trainerTimes)
        self.addUser(userTimes)


if __name__ == "__main__":
    AccountSetting().run(1, 1)
