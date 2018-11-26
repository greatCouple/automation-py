# -- coding: utf-8 --
import sys
from src.utils.constant import const
from src.utils.LogUtil import LogUtil
from src.steps.TrainingState import TrainingState
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddWirelessUser import AddWirelessUser
from src.utils.LogPath import Path
from src.utils.ButtonManger import ButtonManger


def transferArgv():
    if len(sys.argv) < 3:
        print("Invalid parameters,please enter 2 parameters!")
        exit()

    number1 = sys.argv[1]
    number2 = sys.argv[2]
    return [number1, number2]


class WireModeDoExercise:
    def __init__(self):
        self.Log_file = Path().getLogPath('WireModeExercise')
        LogUtil.log(self.Log_file, "Start WireModeDoExercise test !!!")
        LoginAndLogout().loginTrainer()
        AddWirelessUser().addWireUser()
        ButtonManger.clickButton(const.btn_start)
        ButtonManger.clickButton(const.btn_MuscleDevelopment)

    def startAndPause(self, number1):
        for m in range(int(number1)):
            LogUtil.log(self.Log_file, "pause counter: " + str(m))
            TrainingState().Start()
            TrainingState().Pause()

    def startAndStop(self, number2):
        for n in range(int(number2)):
            LogUtil.log(self.Log_file, "stop counter: " + str(n))
            TrainingState().Stop()
            TrainingState().Start()

    def run(self, number1, number2):
        self.startAndPause(number1)
        self.startAndStop(number2)


if __name__ == "__main__":
    WireModeDoExercise().run(1, 1)
