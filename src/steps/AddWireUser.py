from src.utils.ButtonManger import ButtonManger
from src.utils.constant import const
import time


class AddWireUser:
    def clickAdd(self):
        try:
            ButtonManger.clickButton(const.btn_add_user)
        except:
            ButtonManger.clickButton(const.btn_tab_add)
        try:
            while ButtonManger.getButton(const.btn_manual_add):
                ButtonManger.getButton(const.btn_manual_add).click()
        except Exception as e:
            pass
        ButtonManger.clickButton(const.btn_user_save)

    # 教练添加有线模式学员
    def addWireUser(self):
        self.clickAdd()
        ButtonManger.clickButton(const.btn_wire_mode)  # 选择有线模式
        time.sleep(8)
