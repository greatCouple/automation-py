# -- coding: utf-8 --
from src.utils.ButtonUtils import ButtonUtils
from src.utils.constant import const
from src.steps.AccountManagement import AccountManagement
from src.steps.InputPW import InputPW
import time, sys


class LoginAndLogout:
    def loginTrainer(self):
        ButtonUtils.clickButton(const.btn_RelativeLayout)
        try:
            self.button = ButtonUtils.getButton(const.btn_trainer_tel)
            if self.button:
                InputPW().inputPW()
                time.sleep(5)
        except Exception as e:
            print('Please add user!')
            self.logoutTrainer()
            self.loginAdmin()
            AccountManagement().createTrainer_User()
            self.logOut()
            self.loginTrainer()

    def loginAdmin(self):
        ButtonUtils.clickButton(const.btn_admin)
        InputPW().inputPW()

    # 退出教练登陆
    def logoutTrainer(self):
        ButtonUtils.clickButton(const.btn_back)
        ButtonUtils.clickButton(const.btn_confirm_ok)
        time.sleep(10)
        try:
            self.loading_exist = ButtonUtils.getButton(const.btn_loading)
            if self.loading_exist:
                print("Failed to logout trainer!")
                sys.exit()
        except Exception as e:
            pass
        try:
            self.trainer_tel = ButtonUtils.getButton(const.btn_trainer_tel)
            if self.trainer_tel:
                print("Logout successfully!")
        except Exception as e:
            print("Failed to get the trainer list!")
            self.pw_exist = ButtonUtils.getButton(const.btn_psw_lable)
            if not self.pw_exist:
                print("The page is blank!")
            sys.exit()

    def logOut(self):
        try:
            self.icon = ButtonUtils.getButton(const.btn_back)
            while self.icon:
                self.icon.click()
                time.sleep(2)
                try:
                    ButtonUtils.clickButton(const.btn_confirm_ok)
                except Exception as e:
                    pass
                self.icon = ButtonUtils.getButton(const.btn_back)
        except Exception as e:
            pass