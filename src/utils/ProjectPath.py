import os, datetime


class Path:
    def __init__(self):
        self.work_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        self.logPath = self.work_path + "/output/"
        self.nfcLogPath = self.work_path + "/NFCLog/"
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)

        if not os.path.exists(self.nfcLogPath):
            os.mkdir(self.nfcLogPath)

    def logPath(self, testModule):
        return self.logPath + testModule + '_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".log"

    def nfcLogPath(self, testModule):
        return self.nfcLogPath + testModule + '_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".log"
