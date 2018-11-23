# -- coding: utf-8 --
from src.utils.Log import GetLog
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.utils.ProjectPath import Path


class LoginAndLogoutTrainer:
    def __init__(self):
        self.logFile = Path().logPath('LoginAndLogoutTrainer')
        print(self.logFile)

    def loginAndLogoutTrainer(self, times):
        for x in range(int(times)):
            LoginAndLogout().loginTrainer()
            AddUser().clickAdd()
            AddUser().addWireUser()
            LoginAndLogout().logoutTrainer()
            GetLog().log(self.logFile, "Times " + str(x))

    def run(self, times):
        self.loginAndLogoutTrainer(times)


if __name__ == "__main__":
    LoginAndLogoutTrainer().run(2)