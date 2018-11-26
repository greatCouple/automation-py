# -- coding: utf-8 --
import threading, time, sys

from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.steps.ChangeWifi import ChangeWifi
from src.utils.serport import serport
from src.utils.LogUtil import LogUtil
from src.utils.LogPath import Path


def transferArgv():
    if len(sys.argv) < 2:
        print("Invalid parameters,please enter 1 parameter!")
        exit()
    PairTimes = sys.argv[1]
    return PairTimes


class NFCPair1:
    def __init__(self):
        self.Log_file = Path().getLogPath('NFCPair1')
        self.NFClog_file = Path().getNFCLogPath('NFC')
        # 教练登陆
        LoginAndLogout().loginTrainer()

        self.match_state = None

    def SaveLog(self):
        while serport.is_open:
            serport.write(b'\r$EMD9\r')
            time.sleep(1)
            serport.write(b'\r$EMD4\r')
            time.sleep(1)
            data = serport.readline()
            LogUtil.nfcLog(self.NFClog_file, repr(data))

    def NFCPairing(self, pairTimes):
        n = 0
        for x in range(int(pairTimes)):
            AddUser().clickAdd()
            while AddUser().chooseWirelessMode():
                n += 1
                LogUtil.log(self.Log_file, "NFC Pairing failed !!! Failed counter: " + str(n))
            LogUtil.log(self.Log_file, "NFC Pairing succeed !!! Succeed counter: " + str(x))
            LogUtil.log(self.Log_file, "Change wifi id :" + str(x))
            ChangeWifi().changeWifi()
        serport.close()

    def thread(self, pairTimes):
        t1 = threading.Thread(target=self.SaveLog)
        t1.start()
        t2 = threading.Thread(target=self.NFCPairing(pairTimes))
        t2.start()
        t2.join()

    def run(self, pairTimes, times):
        LogUtil.log(self.Log_file, "Start NFCPair1 test !!!")
        self.thread(pairTimes)


if __name__ == "__main__":
    NFCPair1().run(1, 0)
#	driver.quit()
