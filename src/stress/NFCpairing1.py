# -- coding: utf-8 --
import threading, time, sys

from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.steps.ChangeWifi import ChangeWifi
from src.utils.serport import SerialPort
from src.utils.Log import GetLog
from src.utils.ProjectPath import Path

if (len(sys.argv) < 2):
    print("Invalid parameters,please enter 1 parameter!")
    exit()

PairTimes = sys.argv[1]
Log_file = Path().logPath('NFCpairing')
NFClog_file = Path().nfcLogPath('NFC')

# 教练登陆
LoginAndLogout().loginTrainer()

match_state = None


def SaveLog():
    global match_state
    SerialPort.serport.write(b'\r$EMD9\r')
    time.sleep(1)
    SerialPort.serport.write(b'\r$EMD4\r')
    time.sleep(1)
    while True:
        data = SerialPort.serport.readline()
        GetLog().log(NFClog_file, repr(data))
        if match_state == True:
            break


def NFCPairing():
    n = 0
    for x in range(int(PairTimes)):
        AddUser().clickAdd()
        while AddUser().chooseWirelessMode():
            n += 1
            GetLog().log(Log_file, "NFC Pairing failed !!! Failed counter: " + str(n))
        GetLog().log(Log_file, "NFC Pairing succeed !!! Succeed counter: " + str(x))
        GetLog().log(Log_file, "Change wifi id :" + str(x))
        ChangeWifi().changeWifi()


def thread():
    global match_state
    t1 = threading.Thread(target=SaveLog)
    t2 = threading.Thread(target=NFCPairing)
    t1.start()
    t2.start()
    t2.join()
    match_state = True
    return match_state


if __name__ == "__main__":
    thread()
#	driver.quit()
