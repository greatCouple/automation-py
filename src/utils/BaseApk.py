import time,re,os
from appium import webdriver
from src.utils.YamlUtil import YamlUtil


class Init:
    @staticmethod
    def startApp():
        readDeviceId = list(os.popen('adb devices').readlines())
        device_id = re.findall(r'^\w*\b', readDeviceId[1])[0]
        driverConfig = YamlUtil.read('driverConfig')
        print(driverConfig.get('url'))
        desired_caps = driverConfig.get('desired_caps')
        desired_caps['deviceName'] = device_id
        driver = webdriver.Remote(driverConfig.get('url'), desired_caps)  # 启动app
        time.sleep(20)


if __name__ == '__main__':
    Init.startApp()
