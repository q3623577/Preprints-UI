import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.basepage import BasePage
from tool_uint import file_op
from tool_uint.log_op import logger


class Process_Manu:
    def __init__(self,login):
        self.backend_url = "https://zhou.sciprints.mdpi.dev/editor/index"

        self.options = webdriver.ChromeOptions()
        self.driver = login
        self.options.add_argument('--user-data-dir=C:/Users/MDPI/PycharmProjects/UI_test/')
        self.wait = WebDriverWait(self.driver, 10)
        self.js_to_mid = "document.documentElement.scrollTop=500"
        self.js_to_down = "document.documentElement.scrollTop=1000"

        self.check_sanction_step1_No='//*[@id="editor-manuscript-sanction-check"]/button[2]'
        self.check_sanction_step2_No='//*[@id="me-sanction-check-form"]/label[1]/input'
        self.check_sanction_step1_Yes='//*[@id="editor-manuscript-sanction-check"]/button[1]'
        self.check_sanction_step2_Yes='//*[@id="me-sanction-check-form"]/label[2]/input'
        self.check_submit='//*[@id="me-sanction-check-form"]/button'

        self.accept_button='//a[contains(text(),"Accept")]'
        self.cancel_button='//a[contains(text(),"Cancel")]'
        self.ok_button='//a[contains(text(),"Ok")]'

        self.online_button='//*[@id="main-content"]/div[2]/div[2]/div/div[23]/div[1]/a[1]'
        self.online_confirm_button='/html/body/div[9]/div[3]/div/button'
        self.online_reminder_button='/html/body/div[10]/div[3]/div/button'
        self.upload_layout_down='//*[@id="main-content"]/div[2]/div[2]/div/div[23]/div[4]/div/div[2]/div[2]/a'
        self.upload_final_pdf='//*[@id="main-content"]/div[2]/div[2]/div/div[23]/div[4]/div/div[3]/div[2]/a'

        self.online_checkbox='//*[@id="manuscript_qualifies"]'
        self.online_announce='//*[@id="main-content"]/div[2]/div[2]/div/div[23]/div[4]/div/div[2]/div[2]/div[2]/a'
        self.online_send_email='//*[@id="submit_next_btn"]'

    def open_browser(self):
        self.driver.execute_script(f"window.open('{self.backend_url}', '_blank');")
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def open_detail_page(self,ppid):
        time.sleep(3)
        value = '//td/a[contains(text(),'+ppid+')]'
        self.driver.find_element(by=By.XPATH, value=value).click()
        self.driver.implicitly_wait(10)

    def check_list(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(5)

        try:
            self.driver.execute_script(self.js_to_mid)
            checklist= self.driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[2]/div[2]/div/div[20]/form')
            checks = checklist.find_elements(by=By.CSS_SELECTOR, value="input[type='radio']")
            for check in checks[:16:2]:
                check.click()
            self.driver.implicitly_wait(10)
            self.driver.execute_script(self.js_to_down)
            self.driver.find_element(by=By.CSS_SELECTOR,value="button[type='submit']").click()
        except NoSuchElementException:
            print("The checklist is checked")

    def check_sanctions(self,step1,step2):
        self.driver.execute_script(self.js_to_down)
        if step1 =='yes':
            self.driver.find_element(by=By.XPATH,value=self.check_sanction_step1_Yes).click()
        elif step1 =='no':
            self.driver.find_element(by=By.XPATH,value=self.check_sanction_step1_No).click()
            if step2 =='yes':
                self.driver.find_element(by=By.XPATH,value=self.check_sanction_step2_Yes).click()
            else:
                self.driver.find_element(by=By.XPATH,value=self.check_sanction_step2_No).click()
        self.driver.find_element(by=By.XPATH,value=self.check_submit).click()
        self.driver.implicitly_wait(10)

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

    def click_online(self):
        time.sleep(5)
        self.driver.execute_script(self.js_to_down)
        self.driver.find_element(by=By.XPATH, value=self.online_button).click()
        self.driver.find_element(by=By.XPATH, value=self.online_confirm_button).click()
        self.driver.find_element(by=By.XPATH, value=self.online_reminder_button).click()

        time.sleep(10)
        docx_path = file_op.get_file_dir('.docx')
        self.driver.find_element(by=By.XPATH, value=self.upload_layout_down).click()
        pyperclip.copy(docx_path)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter', 3)
        logger.info("upload layout file")

        time.sleep(10)
        pdf_path = file_op.get_file_dir('.pdf')
        self.driver.find_element(by=By.XPATH, value=self.upload_final_pdf).click()
        pyperclip.copy(pdf_path)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter', 3)
        logger.info("upload final pdf file")

        time.sleep(20)
        pyautogui.press('esc', 1)
        self.driver.execute_script(self.js_to_down)
        self.driver.find_element(by=By.XPATH, value=self.online_checkbox).click()
        self.driver.find_element(by=By.XPATH, value=self.online_announce).click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=self.online_send_email).click()
        self.driver.implicitly_wait(10)

    

# if __name__ == '__main__':
#     obj = Process_Manu()
#     obj.open_browser()
#     # obj.driver.execute_script(obj.js_to_down)
#     obj.open_detail_page("132266")
#
#     obj.check_list()
#     obj.click_accept("cancel")
