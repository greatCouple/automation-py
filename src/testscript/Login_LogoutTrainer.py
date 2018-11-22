# -- coding: utf-8 --
import datetime,os


from src.utils.Log import GetLog
from src.functionTest.Login_Logout import Login_Logout
from src.functionTest.AddUser import AddUser
from src.utils.ProjectPath import work_path

#if (len(sys.argv) < 2):
#    print ("Invalid parameters,please enter 1 parameters!")
#   exit()

#times = sys.argv[1]

Log_path = work_path + "/output/"
Log_file = Log_path + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + "_Login_LogoutTrainer.txt"

if not os.path.exists(Log_path):
    os.mkdir(Log_path)


if __name__=="__main__":
    for x in range(int(10000)):
        Login_Logout().loginTrainer()
        AddUser().clickAdd()
        AddUser().addWireUser()
        Login_Logout().logoutTrainer()
        GetLog().log(Log_file,"Times " + str(x))