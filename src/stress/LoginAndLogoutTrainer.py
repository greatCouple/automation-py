# -- coding: utf-8 --
from src.utils.LogUtil import LogUtil
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.utils.LogPath import Path


class LoginAndLogoutTrainer:
    def __init__(self):
        self.logFile = Path().getLogPath('LoginAndLogoutTrainer')
        print(self.logFile)

    def loginAndLogoutTrainer(self, times):
        for x in range(int(times)):
            LoginAndLogout().loginTrainer()
            AddUser().clickAdd()
            AddUser().addWireUser()
            LoginAndLogout().logoutTrainer()
            LogUtil.log(self.logFile, "Times " + str(x))

    def run(self, times, times2):
        LogUtil.log(self.logFile, "Start LoginAndLogout test !!!")
        self.loginAndLogoutTrainer(times)


if __name__ == "__main__":
    LoginAndLogoutTrainer().run(1, 0)
