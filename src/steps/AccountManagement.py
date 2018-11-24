# -- coding: utf-8 --
import time
from src.utils.ButtonUtils import ButtonUtils
from src.utils.constant import const
from src.steps.InputPW import InputPW
from src.utils.ReadYaml import ReadYaml


class AccountManagement:
    # 创建账户
    def createAccount(self, account, password):
        self.account = account
        self.password = password
        ButtonUtils.clickButton(const.btn_tab_add)  # 点击添加按钮
        ButtonUtils.clickButton(const.btn_user_nickname)
        ButtonUtils.getButton(const.btn_user_nickname).send_keys(self.account)  # 设置账号
        ButtonUtils.clickButton(const.btn_et_tel)
        ButtonUtils.getButton(const.btn_et_tel).send_keys(self.password)  # 设置电话
        ButtonUtils.clickButton(const.btn_user_create_pin)
        InputPW().inputPW()
        time.sleep(1)
        InputPW().inputPW()  # 确认密码
        ButtonUtils.clickButton(const.btn_user_save)  # 点击创建
        time.sleep(5)
        try:
            self.nickname1 = ButtonUtils.getButton(const.btn_trainer_name).text
            if self.nickname1 == self.account:
                print("Create " + account + " successfully!")
        except Exception as e:
            print("Failed to create user!")
            pass

    # 删除学员
    def deleteAccount(self):
        self.tel1 = ButtonUtils.getButton(const.btn_trainer_name).text
        ButtonUtils.clickButton(const.btn_user_detail_edit)
        ButtonUtils.clickButton(const.btn_user_delete)
        ButtonUtils.clickButton(const.btn_confirm_ok)
        time.sleep(5)
        try:
            self.tel2 = ButtonUtils.getButton(const.btn_trainer_tel).text
            if self.tel2 and self.tel2 == self.tel1:
                print("Failed to deleteAccount!")
        except Exception as e:
            print("deleteAccount successfully!")
            pass

    # 删除所有学员
    def deleteAll(self):
        self.nickname2 = ButtonUtils.getButton(const.btn_trainer_name).text
        while self.nickname2 != "Add New Account":
            self.deleteAccount()
            self.nickname2 = ButtonUtils.getButton(const.btn_trainer_name).text

    # 创建账户
    def createTrainer_User(self):
        ButtonUtils.clickButton(const.btn_AccountSetting)  # 点击账户设置
        self.nickname2 = ButtonUtils.getButton(const.btn_trainer_name).text
        if self.nickname2 != "Add New Account":
            self.deleteAll()
            print("Delete all the trainers!")
        trainers = ReadYaml().readYaml('trainer')
        for key in trainers.keys():
            AccountManagement().createAccount(key, trainers.get(key))
        ButtonUtils.clickButton(const.btn_tab_user)  # 切换到学员添加界面
        time.sleep(3)

        self.nickname3 = ButtonUtils.getButton(const.btn_trainer_name).text
        if self.nickname3 != "Add New Account":
            self.deleteAll()
            print("Delete all the users!")
        users = ReadYaml().readYaml('user')
        for key in users.keys():
            AccountManagement().createAccount(key, users.get(key))
        ButtonUtils.clickButton(const.btn_back)
