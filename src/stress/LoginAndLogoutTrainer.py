# -- coding: utf-8 --
import datetime, os, sys


from src.utils.Log import GetLog
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.utils.ProjectPath import work_path

if len(sys.argv) < 2:
    print('Invalid parameters,please enter 1 parameters!')
    exit()

times = sys.argv[1]

Log_path = work_path + "/output/"
Log_file = Log_path + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + "_LoginAndLogoutTrainer.txt"

if not os.path.exists(Log_path):
    os.mkdir(Log_path)


class LoginAndLogoutTrainer:
    def loginAndLogoutTrainer(self, times):
        for x in range(int(times)):
            LoginAndLogout().loginTrainer()
            AddUser().clickAdd()
            AddUser().addWireUser()
            LoginAndLogout().logoutTrainer()
            GetLog().log(Log_file, "Times " + str(x))

    def run(self, times):
        self.loginAndLogoutTrainer(times)


if __name__ == "__main__":
    LoginAndLogoutTrainer().run(times)