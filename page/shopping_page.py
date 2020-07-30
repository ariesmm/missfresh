'''

'''
import time

from selenium.webdriver.common.by import By


class ShoppingPage():
    def __init__(self,driver):
        self.driver = driver

    #元素定位符
        self.loc_ele_click_search = (By.ID,'cn.missfresh.application:id/tv_search_text')
        self.loc_ele_input = (By.XPATH,'//android.widget.EditText[@resource-id="cn.missfresh.application:id/search_view"]')
        self.loc_ele_pay = (By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_confirm"]')


    #点击搜索框
    def ele_click_search(self):
        self.driver.find_element(*self.loc_ele_click_search).click()
        time.sleep(3)

    #输入数据并确定
    def ele_input(self,tradename):
        self.driver.find_element(*self.loc_ele_input).send_keys(tradename)
        time.sleep(1)
        self.driver.press_keycode(66)
        time.sleep(2)

    #进入商品详情
    def ele_product_details(self):
        self.driver.tap([(60,230)])
        time.sleep(2)

    #立即购买
    def ele_buy(self):
        self.driver.tap([(625,1240)])
        time.sleep(2)

    #立即支付
    def ele_pay(self):
        self.driver.find_element(*self.loc_ele_pay).click()
        time.sleep(5)

    '''购买商品'''
    def shopping_mania(self,tradename):
        self.ele_click_search() #点击搜索框
        self.ele_input(tradename) #输入数据并确定
        self.ele_product_details() #进入商品详情
        self.ele_buy() #立即购买
        self.ele_pay() #立即支付
