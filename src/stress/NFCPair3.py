# -- coding: utf-8 --
import threading, time

from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddWirelessUser import AddWirelessUser
from src.steps.AddWireUser import AddWireUser
from src.utils.serport import serport
from src.utils.LogUtil import LogUtil
from src.utils.constant import const
from src.utils.ButtonManger import ButtonManger
from src.utils.LogPath import Path


class NFCPair3:
    def __init__(self):
        self.Log_file = Path().getLogPath('NFCPair3')
        self.NFClog_file = Path().getNFCLogPath('NFC')
        LogUtil.log(self.Log_file, "Start NFCPair3 test !!!")
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
        AddWireUser().addWireUser()
        ButtonManger.clickButton(const.btn_start)
        ButtonManger.clickButton(const.btn_MuscleDevelopment)
        for x in range(int(pairTimes)):
            AddWirelessUser().clickAdd()
            while AddWirelessUser().chooseWirelessMode():
                n += 1
                LogUtil.log(self.Log_file, "NFC Pairing failed !!! Failed counter: " + str(n))
            LogUtil.log(self.Log_file, "NFC Pairing succeed !!! Succeed counter: " + str(x))
        serport.close()

    def thread(self, pairTimes):
        t1 = threading.Thread(target=self.SaveLog)
        t1.start()
        t2 = threading.Thread(target=self.NFCPairing(pairTimes))
        t2.start()
        t2.join()

    def run(self, pairTimes, times):
        self.thread(pairTimes)


if __name__ == "__main__":
    NFCPair3().run(1, 0)
