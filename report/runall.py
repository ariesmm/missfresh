import time
import unittest

from BeautifulReport import BeautifulReport

'''使用BeautifulReport生成报告'''

test_dir='testcase' #测试目录
log_path='report' #日志存放目录
filename=time.strftime('%Y-%m-%d-%H-%M-%S') #文件名

discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*')

BeautifulReport(discover).report(
    description='每日优鲜自动化测试报告',
    log_path=log_path,
    filename=filename)
