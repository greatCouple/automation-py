# -- coding: utf-8 --
from src.utils.ButtonManger import ButtonManger
from src.utils.constant import const
import time

class SystemSetting:
    # 系统设置
    def systemSetting(self):
        ButtonManger.clickButton(const.btn_SystemSetting)
        time.sleep(3)
        try:
            self.display_btn = ButtonManger.getButton(const.btn_name).text
            if self.display_btn == "Display":
                ButtonManger.clickButton(const.btn_display)
        except Exception as e:
            print(u"系统设置界面异常")
            ButtonManger.clickButton(const.btn_back)
            ButtonManger.clickButton(const.btn_SystemSetting)
        finally:
            ButtonManger.clickButton(const.btn_display)
            print("Enter the display interface")
            ButtonManger.clickButton(const.btn_back)
            ButtonManger.clickButton(const.btn_restore)
            print("Enter the restore interface")
            ButtonManger.clickButton(const.btn_confirm_cancel)
            ButtonManger.clickButton(const.btn_DateTime)
            print("Enter the datetime interface")
            ButtonManger.clickButton(const.btn_back)
            ButtonManger.clickButton(const.btn_Language)
            time.sleep(2)
            print("Enter the language interface")
            ButtonManger.clickButton(const.btn_confirm_cancel)