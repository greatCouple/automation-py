# -- coding: utf-8 --
import datetime


class LogUtil:
    @staticmethod
    def log(file, msg):
        doc = open(file, 'a')
        if doc:
            log_msg = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': ' + msg + '\n'
            doc.write(log_msg)
            doc.close()
