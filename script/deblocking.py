

import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

'''线性脚本'''

desired_capabilities = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:62001',
    'platformVersion':'5.1.1',
    'appPackage':'cn.missfresh.application',
    'appActivity':'cn.missfresh.module.base.main.view.SplashActivity'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)

'''九宫格解锁'''

#获取窗口大小
size=driver.get_window_size()
print('窗口大小:',size)

#先向上滑动
start_x=size['width']*0.5 #起点X坐标
start_y=size['height']*0.9 #起点y坐标
end_x=size['width']*0.5 #终点x坐标
end_y=size['height']*0.3 #终点y坐标
driver.swipe(start_x,start_y,end_x,end_y)#向上滑动

#解锁
ta=TouchAction(driver)#实例化类
time.sleep(3) #等待3秒
#九宫格
a=[[200,800],[360,800],[520,800],
   [195,960],[360,960],[520,960],
   [195,1120],[360,1120],[520,1120]]

ta.press(x=a[6][0],y=a[6][1]) #第一个点，按住
ta.wait(1000) #操作过程中等待
all=[3,0,4,8,5,2]#其余六个点
for i in all: #其余六个点循环
    ta.move_to(x=a[i][0], y=a[i][1])  # i为索引
    ta.wait(1000)

ta.release() #释放
ta.perform() #提交
time.sleep(3)


