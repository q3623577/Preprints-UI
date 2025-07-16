import os
import time

import pytest
from _pytest.config import ExitCode
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:/Users/MDPI/PycharmProjects/UI_test/')
# driver = webdriver.Chrome(options=options)
Continue = "/html/body/main/div/div[2]/div[2]/div[1]/form/div/div[3]/input[2]"
LoginBtn = '//*[@id="__nuxt"]/div[2]/header/div/div[2]/div/div[1]/div/div[1]/button/span'

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
    time.sleep(5)
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
        print("already logged in")
    time.sleep(3)
    try:
        flame = driver.find_element(by=By.XPATH, value='html/body/aside')
        # shadow_root=flame.shadow_root
        flame.shadow_root.find_element(by=By.ID,value='accept').click()
    except NoSuchElementException as e:
        print("already accept")
    yield driver
    print("success")
    driver.quit()
#
# def pytest_sessionfinish(session, exitstatus):
#     if exitstatus == ExitCode.OK:
#         # 生成临时JSON报告
#         os.system("pytest --alluredir=./allure-results")
#         # 转换为HTML报告（需已配置Allure环境变量）
#         os.system("allure generate ./allure-results -o ./allure-report --clean")
#         # 自动打开报告（可选）
#         os.system("allure open ./allure-report")








