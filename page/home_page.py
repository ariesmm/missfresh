import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.deblocking_page import DeblockingPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #点击首页搜索框
        self.loc_ele_home_search=(By.ID,'cn.missfresh.application:id/tv_search_text')
        #进入搜索页面并输入关键字
        self.loc_ele_home_search_text=(By.XPATH,'//android.widget.EditText[@resource-id="cn.missfresh.application:id/search_view"]')
        #点击搜索
        self.loc_ele_home_search_button=(By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_search"]')
        #点击第一个商品
        self.loc_ele_home_search_goods=(By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id=\"cn.missfresh.application:id/result_recycler\"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
        #加入购物车
        self.loc_ele_home_search_add_to_cart=(By.XPATH,'//android.widget.TextView[@text="加入购物车"]')
        #进入购物车
        self.loc_ele_home_search_cart = (
        By.XPATH, '//android.widget.ImageView[@resource-id="cn.missfresh.application:id/iv_cart_icon"]')


    def ele_home_search(self):
        time.sleep(2)
        '''点击首页搜索框'''
        self.driver.find_element(*self.loc_ele_home_search).click()

    def ele_home_search_text(self,keywords):
        '''进入搜索页面并输入关键字'''
        time.sleep(2)
        self.driver.find_element(*self.loc_ele_home_search_text).clear()
        self.driver.find_element(*self.loc_ele_home_search_text).send_keys(keywords)

    def ele_home_search_button(self):
        '''点击搜索'''
        self.driver.find_element(*self.loc_ele_home_search_button).click()

    def ele_home_search_goods(self):
        '''点击第一个商品'''
        self.driver.find_element(*self.loc_ele_home_search_goods).click()

    def ele_home_search_add_to_cart(self):
        '''加入购物车'''
        time.sleep(3)
        self.driver.find_element(*self.loc_ele_home_search_add_to_cart).click()

    def ele_home_search_cart(self):
        '''进入购物车'''
        time.sleep(3)
        self.driver.find_element(*self.loc_ele_home_search_cart).click()
        print('成功加入购物车')
        time.sleep(3)

    def ele_home_search_cart_result(self):
        '''结果验证'''
        time.sleep(3)
        cart_result=self.driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_location\"]').text
        return cart_result

    def homepage(self,keywords):
        '''首页搜索并加入购物车'''
        time.sleep(5)
        d=DeblockingPage(self.driver) #实例化滑动
        for i in range(5): #滑动5次
            d.swipe_to_up()

        self.ele_home_search() #首页搜索框
        self.ele_home_search_text(keywords) #进入搜索页面，输入关键字
        self.ele_home_search_button() #点击搜索按钮
        time.sleep(2)
        self.ele_home_search_goods() #点击第一个商品
        time.sleep(3) #停留3秒
        for i in range(5):  #进入商品详情页面，滑动5次
            d.swipe_to_up()
        self.ele_home_search_add_to_cart() #加入购物车
        self.ele_home_search_cart() #进入购物车
        cart_result=self.ele_home_search_cart_result() #断言
        return cart_result #返回结果


