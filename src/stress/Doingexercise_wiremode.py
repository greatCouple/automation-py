# -- coding: utf-8 --
import sys

from src.utils.Log import GetLog
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

    def Start_Pause(self, number1):
        TrainingState().Start()
        for m in range(int(number1)):
            GetLog().log(self.Log_file, "pause counter: " + str(m))
            TrainingState().Pause()
            TrainingState().Start()

    def Start_Stop(self, number2):
        for n in range(int(number2)):
            GetLog().log(self.Log_file, "stop counter: " + str(n))
            TrainingState().Stop()
            TrainingState().Start()

    def run(self, number1, number2):
        self.Start_Pause(number1)
        self.Start_Pause(number2)


if __name__ == "__main__":
    WireModeDoExercise().Start_Pause(3)
    WireModeDoExercise().Start_Stop(3)