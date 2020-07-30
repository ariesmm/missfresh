import time

from appium.webdriver.common.touch_action import TouchAction

from page.base_page import BasePage


class DeblockingPage(BasePage):
    '''九宫格解锁'''
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def deblocking(self, pwd, direction):


        '''适配分辨率滑动、解锁'''
        lst = [
            [196, 800], [360, 800], [520, 800],
            [196, 960], [360, 960], [520, 960],
            [196, 1125], [360, 1125], [520, 1125]
        ]
        size = self.driver.get_window_size()
        size_x = size['width']
        size_y = size['height']
        if direction == 'up':  # 从下往上
            self.driver.swipe(size_x * 0.5, size_y * 0.9, size_x * 0.5, size_y * 0.3)
            time.sleep(2)
        elif direction == 'down':  # 从上往下
            self.driver.swipe(size_x * 0.5, size_y * 0.3, size_x * 0.5, size_y * 0.9)
        elif direction == 'left':  # 从右往左
            self.driver.swipe(size_x * 0.9, size_y * 0.5, size_x * 0.3, size_y * 0.5)
        elif direction == 'right':  # 从左往右
            self.driver.swipe(size_x * 0.3, size_y * 0.5, size_x * 0.9, size_y * 0.5)

        if size_x == 720 and size_y == 1280:
            lst = lst
        else:
            x_base = size_x / 720
            y_base = size_y / 1280
            for i in range(len(lst)):
                lst[i][0] = lst[i][0] * x_base
                lst[i][1] = lst[i][1] * y_base

        ta = TouchAction(self.driver)
        # 按住第一个点
        ta.press(x=lst[pwd[0] - 1][0], y=lst[pwd[0] - 1][1])
        ta.wait(500)
        # 依次移动
        for i in pwd[1:]:
            ta.move_to(x=lst[i - 1][0], y=lst[i - 1][1])
            ta.wait(500)

        ta.release()  # 释放
        ta.perform()  # 提交

    def swipe_to(self,driver, direction):
        '''
        窗口滑动
        direction为方向参数
        'up':#从下往上
        'down':#从上往下
        'left':#从右往左
        'right':#从左往右
        '''
        windows_size = self.driver.get_window_size()
        x = windows_size['width']
        y = windows_size['height']
        if direction == 'up':  # 从下往上
            driver.swipe(x * 0.5, y * 0.9, x * 0.5, y * 0.3)
            time.sleep(2)
        elif direction == 'down':  # 从上往下
            driver.swipe(x * 0.5, y * 0.3, x * 0.5, y * 0.9)
        elif direction == 'left':  # 从右往左
            driver.swipe(x * 0.9, y * 0.5, x * 0.3, y * 0.5)
        elif direction == 'right':  # 从左往右
            driver.swipe(x * 0.3, y * 0.5, x * 0.9, y * 0.5)



