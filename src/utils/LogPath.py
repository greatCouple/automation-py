import os, datetime
from ProjectPath import work_path


class Path:
    def __init__(self):
        self.logPath = work_path + "/output/"
        self.NFCLogPath = work_path + "/NFCLog/"
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)

        if not os.path.exists(self.NFCLogPath):
            os.mkdir(self.NFCLogPath)

    def getLogPath(self, testModule):
        return self.logPath + testModule + '_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".log"

    def getNFCLogPath(self, testModule):
        return self.NFCLogPath + testModule + '_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".log"


if __name__ == "__main__":
    print(Path().getLogPath("AccountSetting"))
    print(Path().getNFCLogPath("AccountSetting"))
