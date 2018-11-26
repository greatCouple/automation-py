# -- coding: utf-8 --
from src.utils.ButtonManger import ButtonManger
from src.utils.constant import const
from src.utils.StartApp import driver
import time


class TrainingState:
    def data_add_by_progressbar(self):
        for x in range(0, 3):
            try:
                self.progress_bar = ButtonManger.getButton(const.btn_progress_bar)
                if self.progress_bar:
                    driver.swipe(560, 853, 1300, 853, 1)
            except Exception as e:
                time.sleep(1)
                pass
            x += 1
        time.sleep(2)

    def data_dec_by_progressbar(self):
        for x in range(0, 3):
            try:
                self.progress_bar = ButtonManger.getButton(const.btn_progress_bar)
                if self.progress_bar:
                    driver.swipe(1300, 853, 560, 853, 1)
            except Exception as e:
                time.sleep(1)
                pass
            x += 1
        time.sleep(2)

    def get_training_state(self):
        state = None
        try:
            self.Button = ButtonManger.getButton(const.btn_name).text
            if self.Button == "Back":
                state = "Stopped"
        except Exception as e:
            pass
        try:
            self.start_time = ButtonManger.getButton(const.btn_tainer_time_small)
            if self.start_time:
                self.state = "Started"
        except Exception as e:
            pass
        try:
            self.pause_text = ButtonManger.getButton(const.btn_pasue_text).text
            if self.pause_text == 'Paused':
                state = "Paused"
        except Exception as e:
            pass
        return state

    def Start(self):
        ButtonManger.clickButton(const.btn_start)  # 开始运动
        time.sleep(2)
        # startState = self.get_training_state()
        # if startState != 'Started':
        #     print("Failed to start")
        #     ButtonManger.clickButton(const.btn_start)
        # else:
        #     print("Started successfully!")
        # time.sleep(7)
        # try:
        #     self.progress_bar = ButtonManger.getButton(const.btn_progress_bar)
        #     if not self.progress_bar:
        #         ButtonManger.clickButton(const.btn_master)
        # except Exception as e:
        #     pass
        self.data_add_by_progressbar()
        self.data_dec_by_progressbar()
        self.data_add_by_progressbar()
        ButtonManger.clickButton(const.btn_abdomen)
        self.data_add_by_progressbar()
        self.data_dec_by_progressbar()
        self.data_add_by_progressbar()

    def Pause(self):
        ButtonManger.clickButton(const.btn_start)  # 暂停运动
        time.sleep(2)
        # pauseState = self.get_training_state()
        # if pauseState != "Paused":
        #     print("Failed to pause")
        # #		clickButton(const.btn_start)
        # else:
        #     print("Paused successfully!")
        time.sleep(7)

    def Stop(self):
        ButtonManger.clickButton(const.btn_back)  # 停止运动
        time.sleep(2)
        # stopState = self.get_training_state()
        # if stopState != "Stopped":
        #     print("Failed to stop")
        # else:
        #     print("Stopped successfully!")
        time.sleep(7)
