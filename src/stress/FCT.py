import sys

from src.utils.Log import GetLog
from src.steps.TrainingState import TrainingState
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.utils.ConductButton import ConductButton
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
        ConductButton().clickButton(const.btn_start)
        for x in range(1, 6):
            if x == 1:
                GetLog().log(self.Log_file, "Muscle Development mode!")
                ConductButton().clickButton(const.btn_MuscleDevelopment)
            if x == 2:
                GetLog().log(self.Log_file, "Cardiovascular mode!")
                ConductButton().clickButton(const.btn_Cardiovascular)
            if x == 3:
                GetLog().log(self.Log_file, "Relax mode!")
                ConductButton().clickButton(const.btn_Relax)
            if x == 4:
                GetLog().log(self.Log_file, "Manual Setting mode!")
                ConductButton().clickButton(const.btn_ManualSetting)
            if x == 5:
                GetLog().log(self.Log_file, "Professional mode!")
                ConductButton().clickButton(const.btn_Professional)
            TrainingState().Start()
            ChangeWifi().changeWifi()
            AddUser().addWirelessUser()
            TrainingState().Start()
            TrainingState().Pause()
            TrainingState().Stop()
            ConductButton().clickButton(const.btn_back)

    def run(self, times):
        for n in range(int(times)):
            GetLog().log(self.Log_file, "Funtion test times: " + str(n))
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





