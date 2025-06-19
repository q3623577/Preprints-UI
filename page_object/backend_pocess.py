import time


from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.basepage import BasePage


class Process_Manu:
    def __init__(self,login):
        self.backend_url = "https://zhou.sciprints.mdpi.dev/editor/index"

        self.options = webdriver.ChromeOptions()
        self.driver = login
        self.options.add_argument('--user-data-dir=C:/Users/MDPI/PycharmProjects/UI_test/')
        self.wait = WebDriverWait(self.driver, 10)
        self.js_to_down = "document.documentElement.scrollTop=100000"

    def open_browser(self):
        self.driver.execute_script(f"window.open('{self.backend_url}', '_blank');")
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def open_detail_page(self,ppid):
        value = '//td/a[contains(text(),'+ppid+')]'
        self.driver.find_element(by=By.XPATH, value=value).click()
        self.driver.implicitly_wait(10)

    def check_list(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        try:
            checklist= self.driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[3]/div[2]/div[2]')
            checks = checklist.find_elements(by=By.CSS_SELECTOR, value="input[type='radio']")
            self.driver.execute_script(self.js_to_down)
            for check in checks[:16:2]:
                check.click()
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.CSS_SELECTOR,value="button[type='submit']").click()
        except NoSuchElementException:
            print("The checklist is checked")


    def click_accept(self,check):
        self.driver.execute_script(self.js_to_down)
        self.driver.find_element(by=By.XPATH, value='//a[contains(text(),"Accept")]').click()
        print("click accept")
        if check =='ok':
            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value='//a[contains(text(),"Ok")]').click()
        elif check =='cancel':
            time.sleep(3)
            self.driver.find_elements(by=By.XPATH,value='//a[contains(text(),"Cancel")]')[3].click()
            print("???")
        self.driver.implicitly_wait(10)

    

if __name__ == '__main__':
    obj = Process_Manu()
    obj.open_browser()
    # obj.driver.execute_script(obj.js_to_down)
    obj.open_detail_page("132266")

    obj.check_list()
    obj.click_accept("cancel")
