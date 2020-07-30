import time

from selenium.webdriver.common.by import By


class ShoppingTrolleyPage():
    def __init__(self,driver):
        self.driver=driver

    #元素定位符号
        self.loc_ele_visit_the = (By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_go"]')
        self.loc_ele_look_cart = (By.XPATH,'//android.widget.ImageView[@resource-id="cn.missfresh.application:id/iv_cart_icon"]')
        self.loc_ele_changenum_add = (By.ID, 'cn.missfresh.application:id/iv_product_add')
        self.loc_ele_changenum_cutdown = (By.ID, 'cn.missfresh.application:id/iv_product_sub')
        self.loc_ele_delete_commodity = (By.XPATH,
                            '//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_delete"]')
        self.loc_ele_delete_confirm = (By.XPATH,
                            '//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_ensure"]')


    #进入购物车
    def ele_cart(self):
        self.driver.tap([(453, 1233)])
        time.sleep(3)

    #去逛逛
    def ele_visit_the(self):
        self.driver.find_element(*self.loc_ele_visit_the).click()
        time.sleep(3)

    #选择酒水冲调类型
    def ele_select(self):
        self.driver.tap([(303,147)])
        time.sleep(3)

    #进入商品详情
    def ele_commodity_details(self):
        self.driver.tap([(60,230)])
        time.sleep(2)

    #加入购物车
    def ele_add_commodity(self):
        self.driver.tap([(240, 1243)])
        time.sleep(2)

    #进入购物车
    def ele_look_cart(self):
        self.driver.find_element(*self.loc_ele_look_cart).click()
        time.sleep(3)

    #购物车商品数量增加
    def ele_changenum_add(self):
        self.driver.find_element(*self.loc_ele_changenum_add).click()
        time.sleep(2)
    #购物车商品数量减少
    def ele_changenum_cutdown(self):
        self.driver.find_element(*self.loc_ele_changenum_cutdown).click()
        time.sleep(2)

    #购物车删除商品
    def ele_delete_commodity(self):
        self.driver.find_element(*self.loc_ele_delete_commodity).click()
        time.sleep(2)
    #确定删除
    def ele_delete_confirm(self):
        self.driver.find_element(*self.loc_ele_delete_confirm).click()
        time.sleep(3)

    ''''''
    def add_goods(self):
        self.ele_cart() #进入购物车
        self.ele_visit_the() #去逛逛
        self.ele_select() #选择商品类型
        self.ele_commodity_details() #进入商品详情
        self.ele_add_commodity() #加入购物车

    def change_the_goods(self):
        self.ele_look_cart() #进入购物车
        self.ele_changenum_add() #购物车商品数量增加
        self.ele_changenum_cutdown() #减少

    def remove_goods(self):
        self.ele_delete_commodity() #删除所选择的商品
        self.ele_delete_confirm()