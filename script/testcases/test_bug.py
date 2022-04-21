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
    @classmethod
    def setUpClass(cls):
        print("打开浏览器")
        s = Service(r"C:\Users\ASUS\Desktop\个人资料文件\2022.4.13\driver\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()
        cls.driver.get("http://139.224.113.59/zentao/user-login.html")

    @classmethod
    def tearDownClass(cls):
        "关闭浏览器"
        print("关闭浏览器")
        cls.driver.quit()

    def setUp(self):
        print("登录禅道")
        self.driver.find_element(By.ID, "account").send_keys("shelly")
        self.driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(2)
    def tearDown(self):
        print("登出禅道")
        self.driver.find_element(By.XPATH, "//a[@class='dropdown-toggle']/span[1]").click()
        self.driver.find_element(By.LINK_TEXT, "退出").click()

#测试用例1
    def test_addbug_success(self):
        "成功添加bug"

        sleep(1)
        self.driver.find_element(By.LINK_TEXT, "测试").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//header/div[@id='subHeader']/div[1]/nav[1]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element(By.LINK_TEXT, "提Bug").click()
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[1]/div[1]/div[1]/div[1]/button[1]").click()
        sleep(2)
        dialog = win32gui.FindWindow("#32770", "打开")
        combox_32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        combox = win32gui.FindWindowEx(combox_32, 0, "ComboBox", None)
        edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r"C:\Users\ASUS\Desktop\个人资料文件\123.txt")
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        self.driver.find_element(By.ID, "submit").click()
        sleep(2)
        try:
            # self.assertEqual(self.driver.find_element())
            self.assertEqual(self.driver.find_element(By.LINK_TEXT, "提Bug").text, "提Bug")
            print("创建bug成功")
        except:
            print("添加bug失败")
