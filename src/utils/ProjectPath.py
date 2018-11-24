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
        self.logFile = self.logPath + testModule + '_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".log"
        return self.logFile

    def nfcLogPath(self, testModule):
        self.logFile = self.nfcLogPath + testModule + '_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".log"
        return self.logFile