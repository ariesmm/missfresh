
from appium import webdriver


'''原始app驱动'''
def appdriver():
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
    app_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    return app_driver #返回驱动
