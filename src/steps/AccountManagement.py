# -- coding: utf-8 --
import time
from src.utils.ButtonManger import ButtonManger
from src.utils.constant import const
from src.steps.InputPW import InputPW
from src.utils.YamlUtil import YamlUtil


class AccountManagement:
    # 创建账户
    def createAccount(self, account, password):
        self.account = account
        self.password = password
        ButtonManger.clickButton(const.btn_tab_add)  # 点击添加按钮
        ButtonManger.clickButton(const.btn_user_nickname)
        ButtonManger.getButton(const.btn_user_nickname).send_keys(self.account)  # 设置账号
        ButtonManger.clickButton(const.btn_et_tel)
        ButtonManger.getButton(const.btn_et_tel).send_keys(self.password)  # 设置电话
        ButtonManger.clickButton(const.btn_user_create_pin)
        InputPW().inputPW()
        time.sleep(1)
        InputPW().inputPW()  # 确认密码
        ButtonManger.clickButton(const.btn_user_save)  # 点击创建
        time.sleep(5)
        try:
            self.nickname1 = ButtonManger.getButton(const.btn_trainer_name).text
            if self.nickname1 == self.account:
                print("Create " + account + " successfully!")
        except Exception as e:
            print("Failed to create user!")
            pass

    # 删除学员
    def deleteAccount(self):
        self.tel1 = ButtonManger.getButton(const.btn_trainer_name).text
        ButtonManger.clickButton(const.btn_user_detail_edit)
        ButtonManger.clickButton(const.btn_user_delete)
        ButtonManger.clickButton(const.btn_confirm_ok)
        time.sleep(5)
        try:
            self.tel2 = ButtonManger.getButton(const.btn_trainer_tel).text
            if self.tel2 and self.tel2 == self.tel1:
                print("Failed to deleteAccount!")
        except Exception as e:
            print("deleteAccount successfully!")
            pass

    # 删除所有学员
    def deleteAll(self):
        self.nickname2 = ButtonManger.getButton(const.btn_trainer_name).text
        while self.nickname2 != "Add New Account":
            self.deleteAccount()
            self.nickname2 = ButtonManger.getButton(const.btn_trainer_name).text

    # 创建账户
    def createTrainer_User(self):
        ButtonManger.clickButton(const.btn_AccountSetting)  # 点击账户设置
        self.nickname2 = ButtonManger.getButton(const.btn_trainer_name).text
        if self.nickname2 != "Add New Account":
            self.deleteAll()
            print("Delete all the trainers!")
        trainers = YamlUtil.read('trainer')
        for key in trainers.keys():
            AccountManagement().createAccount(key, trainers.get(key))
        ButtonManger.clickButton(const.btn_tab_user)  # 切换到学员添加界面
        time.sleep(3)

        self.nickname3 = ButtonManger.getButton(const.btn_trainer_name).text
        if self.nickname3 != "Add New Account":
            self.deleteAll()
            print("Delete all the users!")
        users = YamlUtil.read('user')
        for key in users.keys():
            AccountManagement().createAccount(key, users.get(key))
        ButtonManger.clickButton(const.btn_back)
