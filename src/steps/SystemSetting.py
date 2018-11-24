# -- coding: utf-8 --
from src.utils.ButtonUtils import ButtonUtils
from src.utils.constant import const
import time

class SystemSetting:
    # 系统设置
    def systemSetting(self):
        ButtonUtils.clickButton(const.btn_SystemSetting)
        time.sleep(3)
        try:
            self.display_btn = ButtonUtils.getButton(const.btn_name).text
            if self.display_btn == "Display":
                ButtonUtils.clickButton(const.btn_display)
        except Exception as e:
            print(u"系统设置界面异常")
            ButtonUtils.clickButton(const.btn_back)
            ButtonUtils.clickButton(const.btn_SystemSetting)
        finally:
            ButtonUtils.clickButton(const.btn_display)
            print("Enter the display interface")
            ButtonUtils.clickButton(const.btn_back)
            ButtonUtils.clickButton(const.btn_restore)
            print("Enter the restore interface")
            ButtonUtils.clickButton(const.btn_confirm_cancel)
            ButtonUtils.clickButton(const.btn_DateTime)
            print("Enter the datetime interface")
            ButtonUtils.clickButton(const.btn_back)
            ButtonUtils.clickButton(const.btn_Language)
            time.sleep(2)
            print("Enter the language interface")
            ButtonUtils.clickButton(const.btn_confirm_cancel)