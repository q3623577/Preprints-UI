import os
import time
from pyvirtualdisplay import Display
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
    display = Display(visible=0, size=(1920, 1080))
    display.start()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Chrome 109+新语法
    options.add_argument("--no-sandbox")  # 解决权限问题‌:ml-citation{ref="5" data="citationList"}
    options.add_argument("--disable-dev-shm-usage")  # 防止内存不足崩溃
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    driver.get("https://zhou.sciprints.mdpi.dev/")

    driver.implicitly_wait(10)
    time.sleep(5)

    try:
        driver.save_screenshot("debug1.png")
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
    display.stop()









