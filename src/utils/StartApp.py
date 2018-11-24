import time,re,os
from appium import webdriver
from src.utils.YamlUtil import YamlUtil


def startApp():
    readDeviceId = list(os.popen('adb devices').readlines())
    device_id = re.findall(r'^\w*\b', readDeviceId[1])[0]
    driverConfig = YamlUtil.read('driverConfig')
    print(driverConfig.get('url'))
    desired_caps = driverConfig.get('desired_caps')
    desired_caps['deviceName'] = device_id
    webDriver = webdriver.Remote(driverConfig.get('url'), desired_caps)  # 启动app
    time.sleep(20)
    return webDriver


driver = startApp()
