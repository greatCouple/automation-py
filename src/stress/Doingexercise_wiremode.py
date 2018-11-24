# -- coding: utf-8 --
import sys

from src.utils.LogUtil import LogUtil
from src.steps.TrainingState import TrainingState
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.utils.ProjectPath import Path


def transferArgv():
    if len(sys.argv) < 3:
        print("Invalid parameters,please enter 2 parameters!")
        exit()

    number1 = sys.argv[1]
    number2 = sys.argv[2]
    return [number1, number2]


class WireModeDoExercise:
    def __init__(self):
        self.Log_file = Path().logPath('WireModeExercise')
        LoginAndLogout().loginTrainer()
        AddUser().addWireUser()

    def startAndPause(self, number1):
        TrainingState().Start()
        for m in range(int(number1)):
            LogUtil.log(self.Log_file, "pause counter: " + str(m))
            TrainingState().Pause()
            TrainingState().Start()

    def startAndStop(self, number2):
        for n in range(int(number2)):
            LogUtil.log(self.Log_file, "stop counter: " + str(n))
            TrainingState().Stop()
            TrainingState().Start()

    def run(self, number1, number2):
        self.startAndPause(number1)
        self.startAndPause(number2)


if __name__ == "__main__":
    WireModeDoExercise().startAndPause(3)
    WireModeDoExercise().startAndStop(3)
