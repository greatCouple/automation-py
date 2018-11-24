# -- coding: utf-8 --
import threading, time, sys

from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.steps.ChangeWifi import ChangeWifi
from src.utils.serport import SerialPort
from src.utils.LogUtil import LogUtil
from src.utils.ProjectPath import Path


def transferArgv():
    if len(sys.argv) < 2:
        print("Invalid parameters,please enter 1 parameter!")
        exit()
    PairTimes = sys.argv[1]
    return PairTimes


class NFCPair1:
    def __init__(self):
        self.Log_file = Path().logPath('NFCpairing')
        self.NFClog_file = Path().nfcLogPath('NFC')
        # 教练登陆
        LoginAndLogout().loginTrainer()

        self.match_state = None

    def SaveLog(self):
        SerialPort.serport.write(b'\r$EMD9\r')
        time.sleep(1)
        SerialPort.serport.write(b'\r$EMD4\r')
        time.sleep(1)
        while True:
            data = SerialPort.serport.readline()
            LogUtil.log(self.NFClog_file, repr(data))

    def NFCPairing(self, pairTimes):
        t1 = threading.Thread(target=self.SaveLog)
        t1.start()
        n = 0
        for x in range(int(pairTimes)):
            AddUser().clickAdd()
            while AddUser().chooseWirelessMode():
                n += 1
                LogUtil.log(self.Log_file, "NFC Pairing failed !!! Failed counter: " + str(n))
            LogUtil.log(self.Log_file, "NFC Pairing succeed !!! Succeed counter: " + str(x))
            LogUtil.log(self.Log_file, "Change wifi id :" + str(x))
            ChangeWifi().changeWifi()

    def thread(self, pairTimes):
        t2 = threading.Thread(target=self.NFCPairing(pairTimes))
        t2.setDaemon(True)
        t2.start()
        t2.join()

    def run(self, pairTimes):
        self.thread(pairTimes)


if __name__ == "__main__":
    NFCPair1().thread(3)
#	driver.quit()
