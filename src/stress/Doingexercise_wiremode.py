# -- coding: utf-8 --
import sys

from src.utils.Log import GetLog
from src.steps.TrainingState import TrainingState
from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.utils.ProjectPath import Path

if len(sys.argv) < 3:
    print("Invalid parameters,please enter 3 parameters!")
    exit()

number1 = sys.argv[1]
number2 = sys.argv[2]
Log_file = Path().logPath('WiremodeExercise')

LoginAndLogout().loginTrainer()
AddUser().addWireUser()


def Start_Pause():
    TrainingState().Start()
    for m in range(int(number1)):
        GetLog().log(Log_file, "pause counter: " + str(m))
        TrainingState().Pause()
        TrainingState().Start()


def Start_Stop():
    for n in range(int(number2)):
        GetLog().log(Log_file, "stop counter: " + str(n))
        TrainingState().Stop()
        TrainingState().Start()

if __name__ == "__main__":
    Start_Pause()
    Start_Stop()