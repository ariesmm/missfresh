import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '5.1.1',
    'appPackage': 'cn.missfresh.application',
    'appActivity': 'cn.missfresh.module.base.main.view.SplashActivity',
    'noReset': 'True',
    'unicodeKeyboard': 'True',
    'resetKeyboard': 'True'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(10)
time.sleep(8)
#进入搜索页面
# driver.tap([(400,80)])
driver.find_element(By.ID,'cn.missfresh.application:id/tv_search_text').click()
time.sleep(3)
#输入数据并确定
driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="cn.missfresh.application:id/search_view"]').send_keys('面包')
time.sleep(1)
driver.press_keycode(66)
time.sleep(2)
#进入商品详情
driver.tap([(60,230)])
time.sleep(2)
#点击立即购买
# driver.find_element(By.XPATH,'//android.widget.TextView[@text="立即购买"]').click()
driver.tap([(625,1240)])
#点击去支付
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_confirm"]').click()
time.sleep(5)
driver.quit()