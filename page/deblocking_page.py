import time

from appium.webdriver.common.touch_action import TouchAction

from page.base_page import BasePage

'''九宫格解锁'''

class Deblocking(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def deblocking(self, all, direction):
        # 获取窗口大小
        size = self.driver.get_window_size()
        print('窗口大小:', size)

        # 向上滑动
        x1 = size['width'] * 0.1  # X左
        x2 = size['width'] * 0.5  # X中
        x3 = size['width'] * 0.9  # X右
        y1 = size['height'] * 0.1  # Y上
        y2 = size['height'] * 0.5  # Y中
        y3 = size['height'] * 0.9  # Y下

        if direction == 'up':  # 向上滑动
            self.driver.swipe(x2, y3, x2, y1)
        elif direction == 'down':  # 向下滑动
            self.driver.swipe(x2, y1, x2, y3)
        elif direction == 'left':  # 向左滑动
            self.driver.swipe(x3, y2, x1, y2)
        elif direction == 'right':  # 向右滑动
            self.driver.swipe(x1, y2, x3, y2)

        # 解锁
        ta = TouchAction(self.driver)  # 实例化类
        time.sleep(3)  # 等待3秒
        # 九宫格
        a = [[200, 800], [360, 800], [520, 800],
             [195, 960], [360, 960], [520, 960],
             [195, 1120], [360, 1120], [520, 1120]]

        start = all[0] - 1  # 传参的第一个点
        ta.press(x=a[start][0], y=a[start][1])  # 第一个点，按住
        ta.wait(500)  # 操作过程中等待
        for i in all[1:]:  # 其余六个点循环
            ta.move_to(x=a[i - 1][0], y=a[i - 1][1])  # i为索引
            ta.wait(500)

        ta.release()  # 释放
        ta.perform()  # 提交




