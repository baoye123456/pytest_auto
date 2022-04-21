'''
@File:test_login.py
@DateTime:2022/4/17 12:41
@Author:shelly
@Desc:
'''
import time
import win32gui
import win32con
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class TestCases (unittest.TestCase):
    def setUp(self):
        "打开测览器"
        print("打开测览器")
        s = Service(r"C:\Users\ASUS\Desktop\个人资料文件\2022.4.13\driver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get("http://139.224.113.59/zentao/user-login.html")

    def tearDown(self):
        "关闭浏览器"
        print("关闭浏览器")
        sleep(2)
        self.driver.quit()


# 测试用例1
    def test_login_success(self):
        "成功登录"
        self.driver.find_element(By.ID, "account").send_keys("shelly")
        self.driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)
        try:
            assert  self.driver.title =="我的地盘 - 禅道"
            print("验证登录成功测试----passed")
        except:
            print("验证登录成功测试----failed")



if __name__ == "_main":
    # unittest.main()
    suite = unittest.TestSuite()
#     # suite.addTest(TestCases("test_adduser"))
#     # suite.addTest(TestCases("test_showuser"))
#     # suite.addTest(TestCases("test_updateuser"))
#     # suite.addTest(TestCases("test_deleteuser"))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCases))
    test_runner = unittest.TextTestRunner()
    test_runner.run(suite)