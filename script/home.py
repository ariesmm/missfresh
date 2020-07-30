from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

'''首页搜索商品加入购物车'''

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '5.1.1',
    'appPackage': 'cn.missfresh.application',
    'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity',
    'noReset':True,
    'unicodeKeyboard':True
}
#初始化driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)

#获取窗口尺寸
time.sleep(10)
size = driver.get_window_size()
size_x = size['width']
size_y = size['height']

#滑动屏幕浏览商品
for i in range(2):
    driver.swipe(size_x * 0.5, size_y * 0.8, size_x * 0.5, size_y * 0.3)

#点击首页搜索框
driver.find_element(By.ID,'cn.missfresh.application:id/tv_search_text').click()
#进入搜索页面并输入关键字
time.sleep(2)
driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="cn.missfresh.application:id/search_view"]').clear()
driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="cn.missfresh.application:id/search_view"]').send_keys('鸡蛋')
#点击搜索
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_search"]').click()
#点击商品
driver.find_element(By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/result_recycler\"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()

#浏览商品详情
for i in range(5):
    driver.swipe(size_x * 0.5, size_y * 0.8, size_x * 0.5, size_y * 0.3)

#加入购物车
time.sleep(3)
driver.find_element(By.XPATH,'//android.widget.TextView[@text="加入购物车"]').click()
print('已加入购物车')

#进入购物车查看
time.sleep(3)
driver.find_element(By.XPATH,'//android.widget.ImageView[@resource-id="cn.missfresh.application:id/iv_cart_icon"]').click()
print('进入购物车查看')
time.sleep(5)

#退出
driver.quit()