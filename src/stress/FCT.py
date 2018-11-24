import sys

from src.utils.LogUtil import LogUtil
from src.steps.TrainingState import TrainingState
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.utils.ButtonUtil import ButtonUtils
from src.utils.constant import const
from src.steps.ChangeWifi import ChangeWifi
from src.steps.SystemSetting import SystemSetting
from src.utils.ProjectPath import Path
from src.steps.AccountManagement import AccountManagement


def transferArgv():
    if len(sys.argv) < 2:
        print("Invalid parameters,please enter 1 parameter!")
        exit()
    times = sys.argv[1]
    return times


class FunctionTest:
    def __init__(self):
        self.Log_file = Path().logPath('FCT')

    def doExercise(self):
        ButtonUtils.clickButton(const.btn_start)
        for x in range(1, 6):
            if x == 1:
                LogUtil.log(self.Log_file, "Muscle Development mode!")
                ButtonUtils.clickButton(const.btn_MuscleDevelopment)
            if x == 2:
                LogUtil.log(self.Log_file, "Cardiovascular mode!")
                ButtonUtils.clickButton(const.btn_Cardiovascular)
            if x == 3:
                LogUtil.log(self.Log_file, "Relax mode!")
                ButtonUtils.clickButton(const.btn_Relax)
            if x == 4:
                LogUtil.log(self.Log_file, "Manual Setting mode!")
                ButtonUtils.clickButton(const.btn_ManualSetting)
            if x == 5:
                LogUtil.log(self.Log_file, "Professional mode!")
                ButtonUtils.clickButton(const.btn_Professional)
            TrainingState().Start()
            ChangeWifi().changeWifi()
            AddUser().addWirelessUser()
            TrainingState().Start()
            TrainingState().Pause()
            TrainingState().Stop()
            ButtonUtils.clickButton(const.btn_back)

    def run(self, times):
        for n in range(int(times)):
            LogUtil.log(self.Log_file, "Funtion test times: " + str(n))
            LoginAndLogout().loginAdmin()
            # AccountManagement().createTrainer_User()
            SystemSetting().systemSetting()
            LoginAndLogout().logOut()
            LoginAndLogout().loginTrainer()
            AddUser().addWireUser()
            AddUser().addWirelessUser()
            self.doExercise()
            LoginAndLogout().logOut()


if __name__ == "__main__":
    FunctionTest().run(2)





