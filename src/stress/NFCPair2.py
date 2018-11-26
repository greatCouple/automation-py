# -- coding: utf-8 --
import threading, time, sys

from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddWirelessUser import AddWirelessUser
from src.utils.serport import serport
from src.utils.LogUtil import LogUtil
from src.utils.LogPath import Path


class NFCPair2:
    def __init__(self):
        self.Log_file = Path().getLogPath('NFCPair2')
        self.NFClog_file = Path().getNFCLogPath('NFC')
        LogUtil.log(self.Log_file, "Start NFCPair2 test !!!")
        # 教练登陆
        LoginAndLogout().loginTrainer()

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
            AddWirelessUser().clickAdd()
            while AddWirelessUser().chooseWirelessMode():
                n += 1
                LogUtil.log(self.Log_file, "NFC Pairing failed !!! Failed counter: " + str(n))
            LogUtil.log(self.Log_file, "NFC Pairing succeed !!! Succeed counter: " + str(x))
        serport.close()

    def thread(self, pairTimes):
        t2 = threading.Thread(target=self.NFCPairing(pairTimes))
        t1 = threading.Thread(target=self.SaveLog)
        t1.start()
        t2.start()

    def run(self, pairTimes, times):
        self.thread(pairTimes)


if __name__ == "__main__":
    NFCPair2().run(1, 0)
