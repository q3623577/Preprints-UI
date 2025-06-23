import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:/Users/MDPI/PycharmProjects/UI_test/')
# driver = webdriver.Chrome(options=options)
Continue = "/html/body/main/div/div[2]/div[2]/div[1]/form/div/div[3]/input[2]"
LoginBtn = '//*[@id="__nuxt"]/div[2]/header/div/div[2]/div/div[1]/div[1]/button/span'

@pytest.fixture(scope="function")
def browser():
    """浏览器初始化与销毁"""
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def login():
    """登录账户"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://zhou.sciprints.mdpi.dev/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # time.sleep(5)
    try:
        driver.find_element(by=By.XPATH,
                                value=LoginBtn).click()
        driver.implicitly_wait(10)
        driver.find_element(by=By.ID, value="username").send_keys("test.DA@mdpi.com")
        driver.find_element(by=By.ID, value="password").send_keys("Guozhuohu12345@")
        # time.sleep(100)
        driver.find_element(by=By.XPATH,
                                     value=Continue).click()
        driver.implicitly_wait(10)
    except NoSuchElementException as e:
        print("aleady logged in")
    time.sleep(3)
    try:
        flame = driver.find_element(by=By.XPATH, value='html/body/aside')
        # shadow_root=flame.shadow_root
        flame.shadow_root.find_element(by=By.ID,value='accept').click()
    except NoSuchElementException as e:
        print("aleady accept")
    yield driver
    print("success")
    driver.quit()

# page = TestOpenPage()
# page.login(username="zhuohu.guo@mdpi.com",password="Guozhuohu12345@")
# test=login()





# public_data={}
#
# @pytest.fixture(scope="function")
# def set_data():
#     def _set_data(key,value):
#         public_data[key] = value
#     return _set_data
#
# @pytest.fixture(scope="function")
# def get_data():
#     def _get_data(key):
#         return public_data.get(key)
#     return _get_data



