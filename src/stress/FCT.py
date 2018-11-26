import sys

from src.utils.LogUtil import LogUtil
from src.steps.TrainingState import TrainingState
from src.steps.LoginAndLogout import LoginAndLogout
#from src.steps.AddWirelessUser import AddWirelessUser
from src.steps.AddWireUser import AddWireUser
from src.utils.ButtonManger import ButtonManger
from src.utils.constant import const
from src.steps.ChangeWifi import ChangeWifi
from src.steps.SystemSetting import SystemSetting
from src.utils.LogPath import Path
from src.steps.AccountManagement import AccountManagement


def transferArgv():
    if len(sys.argv) < 2:
        print("Invalid parameters,please enter 1 parameter!")
        exit()
    return sys.argv[1]


class FunctionTest:
    def __init__(self):
        self.Log_file = Path().getLogPath('FCT')

    def doExercise(self):
        ButtonManger.clickButton(const.btn_start)
        for x in range(1, 6):
            if x == 1:
                LogUtil.log(self.Log_file, "Muscle Development mode!")
                ButtonManger.clickButton(const.btn_MuscleDevelopment)
            if x == 2:
                LogUtil.log(self.Log_file, "Cardiovascular mode!")
                ButtonManger.clickButton(const.btn_Cardiovascular)
            if x == 3:
                LogUtil.log(self.Log_file, "Relax mode!")
                ButtonManger.clickButton(const.btn_Relax)
            if x == 4:
                LogUtil.log(self.Log_file, "Manual Setting mode!")
                ButtonManger.clickButton(const.btn_ManualSetting)
            if x == 5:
                LogUtil.log(self.Log_file, "Professional mode!")
                ButtonManger.clickButton(const.btn_Professional)
            TrainingState().Start()
            ChangeWifi().changeWifi()
            # AddWirelessUser().addWirelessUser()
            # TrainingState().Start()
            TrainingState().Pause()
            TrainingState().Stop()
            ButtonManger.clickButton(const.btn_back)

    def run(self, times, times2):
        LogUtil.log(self.Log_file, "Start Function test !!!")
        for n in range(int(times)):
            LogUtil.log(self.Log_file, "Funtion test times: " + str(n))
            LogUtil.log(self.Log_file, "Login admin !!!")
            LoginAndLogout().loginAdmin()
            LogUtil.log(self.Log_file, "Create Trainer and User !!!")
            AccountManagement().createTrainer_User()
            LogUtil.log(self.Log_file, "Enter the system interface !!!")
            SystemSetting().systemSetting()
            LogUtil.log(self.Log_file, "Admin back to home page !!!")
            LoginAndLogout().logOut()
            LogUtil.log(self.Log_file, "Login trainer !!!")
            LoginAndLogout().loginTrainer()
            LogUtil.log(self.Log_file, "Add wire mode user !!!")
            AddWireUser().addWireUser()
            # LogUtil.log(self.Log_file, "Add wireless mode user !!!")
            # AddWirelessUser().addWirelessUser()
            LogUtil.log(self.Log_file, "Let's do exercise !!!")
            self.doExercise()
            LogUtil.log(self.Log_file, "Trainer back to home page !!!")
            LoginAndLogout().logOut()


if __name__ == "__main__":
    # times1 = transferArgv()
    FunctionTest().run(10000, 0)
