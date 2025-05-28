from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class TestOpenPage:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=C:/Users/MDPI/PycharmProjects/UI_test/')
        self.driver = webdriver.Chrome(options=self.options)
        self.Continue = "/html/body/main/div/div[2]/div[2]/div[1]/form/div/div[3]/input[2]"
        self.LoginBtn = '//*[@id="__nuxt"]/div[2]/header/div/div[2]/div/div[1]/div[1]/button/span'

    def login(self,username,password):
        self.driver.get("https://zhou.sciprints.mdpi.dev/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # time.sleep(5)
        try:
            self.driver.find_element(by=By.XPATH,
                                     value=self.LoginBtn).click()
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.ID, value="username").send_keys(username)
            self.driver.find_element(by=By.ID, value="password").send_keys(password)
            # time.sleep(100)
            self.driver.find_element(by=By.XPATH,
                                     value=self.Continue).click()
            self.driver.implicitly_wait(10)
        except NoSuchElementException as e:
            print("aleady logged in")
        time.sleep(3)
        try:
            self.driver.find_element(by=By.XPATH, value='/html/body/aside//div/div/footer/div[2]/div/button[2]').click()
        except NoSuchElementException as e:
            print("aleady accept")
        return self.driver

# page = TestOpenPage()
# page.login(username="zhuohu.guo@mdpi.com",password="Guozhuohu12345@")


