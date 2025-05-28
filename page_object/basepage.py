from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 通用显式等待

    def find_element(self, locator):
        """带显式等待的元素定位"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """带显式等待的元素定位"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """通用点击操作"""
        self.find_element(locator).click()

    def get_text(self, locator):
        """获取元素文本"""
        return self.find_element(locator).text

    # 可扩展输入、下拉选择等通用操作