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
#进入购物车
# driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/cartTab"]').click()
driver.tap([(453,1233)])
time.sleep(3)
#去逛逛
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_go"]').click()

time.sleep(3)
#选择酒水冲调类型
driver.tap([(303,147)])
time.sleep(3)
#进入商品详情
driver.tap([(60,230)])
time.sleep(2)
#加入购物车
# driver.find_element(By.XPATH,'//android.widget.TextView[@text="加入购物车"]').click()
driver.tap([(240,1243)])
time.sleep(2)
#进入购物车
driver.find_element(By.XPATH,'//android.widget.ImageView[@resource-id="cn.missfresh.application:id/iv_cart_icon"]').click()
time.sleep(3)
#购物车商品数量修改
driver.find_element(By.ID,'cn.missfresh.application:id/iv_product_add').click()
time.sleep(2)
driver.find_element(By.ID,'cn.missfresh.application:id/iv_product_sub').click()
time.sleep(2)
#购物车删除
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_delete"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_ensure"]').click()
time.sleep(3)

driver.quit()