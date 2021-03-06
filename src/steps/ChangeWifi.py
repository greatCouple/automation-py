# -- coding: utf-8 --
from src.utils.ButtonManger import ButtonManger
from src.utils.constant import const
import time


class ChangeWifi:
    def changeWifi(self):
        ButtonManger.clickButton(const.btn_top_wifi)
        try:
            self.wifi_id = ButtonManger.getButton(const.btn_wifi_input).text
            ButtonManger.clickButton(const.btn_input_clear)
            if self.wifi_id == "SFBVB-PSXR3-SFB2X-OOGGA":
                print("Connect S3000000")
                ButtonManger.getButton(const.btn_wifi_input).send_keys("SFVUI-HCXR3-SFB2X-OOGGA")
                ButtonManger.clickButton(const.btn_Network_ID)
            else:
                print("Connect S1000000")
                ButtonManger.getButton(const.btn_wifi_input).send_keys("SFBVB-PSXR3-SFB2X-OOGGA")
                ButtonManger.clickButton(const.btn_Network_ID)
            time.sleep(5)
        except:
            pass
        try:
            self.wifi_state = ButtonManger.getButton(const.btn_wifi_Connected)
            if self.wifi_state:
                self.wifi_state.click()
                time.sleep(1)
                ButtonManger.clickButton(const.btn_confirm_ok)
        except:
            pass
        ButtonManger.clickButton(const.btn_wifi_Connect)
        time.sleep(30)
        try:
            self.wifi_state2 = ButtonManger.getButton(const.btn_wifi_Connected)
            if self.wifi_state2:
                ButtonManger.clickButton(const.btn_back)
            else:
                ButtonManger.clickButton(const.btn_wifi_Connect)
                time.sleep(30)
                ButtonManger.clickButton(const.btn_back)
        except:
            pass