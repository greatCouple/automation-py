# -- coding: utf-8 --
from src.utils.BaseApk import driver
import time


class ButtonUtils:
    @staticmethod
    def getButton(buttonName):
        if "id/" in buttonName:
            return driver.find_element_by_id(buttonName)
        elif "new UiSelector()" in buttonName:
            return driver.find_element_by_android_uiautomator(buttonName)
        else:
            return driver.find_element_by_class_name(buttonName)

    @staticmethod
    def clickButton(buttonName):
        button = ButtonUtils.getButton(buttonName)
        if button:
            button.click()
            time.sleep(2)
