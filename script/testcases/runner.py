'''
@File:runner.py
@DateTime:2022/4/17 12:44
@Author:shelly
@Desc:
'''
import unittest
from BeautifulReport import BeautifulReport

# suite=unittest.TestSuite()
# suite.addTest(unittest.defaultTestLoader.discover(start_dir=r""))
# test_runner=unittest.TextTestRunner()
# test_runner.run(suite)
cases=unittest.defaultTestLoader.discover(start_dir=r"C:\Users\ASUS\Desktop\个人资料文件\2022.4.13\selenium_Test\selenium_day8\script\testcases",pattern='test*.py')
result=BeautifulReport(cases)
result.report(description="系统用户的测试报告", filename="SIT测试报告", report_dir=r"C:\Users\ASUS\Desktop\个人资料文件\2022.4.13\selenium_Test\selenium_day8\script\report")