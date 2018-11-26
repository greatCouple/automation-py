# -- coding: utf-8 --
import threading, time

from src.steps.LoginAndLogout import LoginAndLogout
from src.steps.AddUser import AddUser
from src.utils.serport import SerialPort
from src.utils.LogUtil import LogUtil
from src.utils.constant import const
from src.utils.ButtonManger import ButtonManger
from src.utils.LogPath import Path


class NFCPair3:
    def __init__(self):
        self.Log_file = Path().getLogPath('NFCPair3')
        self.NFClog_file = Path().getNFCLogPath('NFC')
        # 教练登陆
        LoginAndLogout().loginTrainer()

    def SaveLog(self):
        SerialPort.serport.write('\r$EMD9\r')
        time.sleep(1)
        SerialPort.serport.write('\r$EMD4\r')
        time.sleep(1)
        while True:
            #		if str_towrite is not None:
            #			serport.write(str_towrite)
            #			str_towrite = None
            data = SerialPort.serport.readline()
            LogUtil.log(self.NFClog_file, repr(data))

    def NFCPairing(self, pairTimes):
        t1 = threading.Thread(target=self.SaveLog)
        t1.start()
        n = 0
        AddUser().addWireUser()
        ButtonManger.clickButton(const.btn_start)
        ButtonManger.clickButton(const.btn_MuscleDevelopment)
        for x in range(int(pairTimes)):
            AddUser().clickAdd()
            while AddUser().chooseWirelessMode():
                n += 1
                LogUtil.log(self.Log_file, "NFC Pairing failed !!! Failed counter: " + str(n))
            LogUtil.log(self.Log_file, "NFC Pairing succeed !!! Succeed counter: " + str(x))

    def thread(self, pairTimes):
        t2 = threading.Thread(target=self.NFCPairing(pairTimes))
        t2.setDaemon(True)
        t2.start()
        t2.join()

    def run(self, pairTimes, times):
        LogUtil.log(self.Log_file, "Start NFCPair3 test !!!")
        self.thread(pairTimes)


if __name__ == "__main__":
    NFCPair3().run(1, 0)
#	driver.quit()
