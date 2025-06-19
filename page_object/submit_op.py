import time
from selenium.webdriver.common.by import By
import pyautogui
import pyperclip
# from login_op import page
from time import sleep

from page_object.basepage import BasePage


class PageObjectSubmit(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.click_radio = None
        # self.driver = driver
        self.btn = "//a[normalize-space()='Submit']"
        self.agree = 'checkbox-input'
        #选择投稿路径
        self.add_new = "//body/div[@id='__nuxt']/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]/span[1]"
        self.add_follow = '//*[@id="__nuxt"]/div[2]/div[1]/div/div/div/div[2]/button[2]/span'

        #follow_version
        self.pp_select_list ='//*[@id="__nuxt"]/div[2]/div[1]/div/div/div[1]'
        self.ctn = '//*[@id="__nuxt"]/div[2]/div[1]/div/div/div[2]/button[2]'
        self.detail_of_change_title = "iframe[title='Rich Text Area']"
        self.input_detail = 'tinymce'


        #第一步元素
        self.subject = '//*[@id="__nuxt"]/div[2]/div[1]/div/div/div[2]/form/div[1]/div/div[1]'
        self.all_subject = "ul[role='listbox']"
        self.subject_select = 'li'
        self.subject2 = '//*[@id="__nuxt"]/div[2]/div[1]/div/div/div[2]/form/div[1]/div/div[2]/div/div'
        self.subject2_select = "li"
        self.mdpi_topic = "input[role='combobox']"
        self.mdpi_topic_select = "li"

        #第二步元素
        self.type = '//*[@id="basic-info"]/div[1]/div/div'
        self.type_select = 'li'
        self.input_iframe = 'tox-edit-area__iframe'
        self.input = '/html/body'

        #第三步元素
        self.check_dot = "div[role='radio']"  # 和declarations共用一个class标签

        #第四步元素
        self.affiliation = 'affiliation'
        self.region = 'country'
        self.region_select = '//*[@id="country0"]/option[1]'
        self.confirm = 'authorListChecked'


        #第五步元素
        self.file = "manuscript-files"
        self.accept = "privacyAgreementValue"
        self.submit_button = "//button[@type='submit']"

        #提交
        self.proceed_gap = "div[class='flex gap-2']"
        self.preprint_id = "//p[contains(text(),'1')]"


    # 点击submit
    def click_submit(self):
        self.find_element((By.XPATH, self.btn)).click()
        # 

    # 勾选协议
    def click_agree(self):
        self.find_element((By.NAME, self.agree)).click()

    #  开始新投稿
    def click_add_new(self):
        self.find_element((By.XPATH, self.add_new)).click()
        

    # 投稿后续版本
    def click_add_follow(self):
        self.find_element((By.XPATH, self.add_follow)).click()
        

    def click_pp_select(self):
        self.find_elements((By.XPATH, self.pp_select_list))[0].click()
        # 
        # list[0].click()

        self.find_element((By.XPATH, self.ctn)).click()
        

    def input_detail_of_change(self,content):
        iframe = self.find_element((By.CSS_SELECTOR, self.detail_of_change_title))
        self.driver.switch_to.frame(iframe)
        
        self.find_element((By.ID, self.input_detail)).send_keys(content)
        self.driver.switch_to.parent_frame()
        




    # 定位第一个subject框,选择指定项
    def click_subject(self):
        self.find_element((By.XPATH, self.subject)).click()
        all_sub=self.find_element((By.CSS_SELECTOR, self.all_subject))
        sleep(2)
        all_sub.find_elements(By.TAG_NAME, self.subject_select)[2].click()
        # print(subjects)
        

    # 定位二级subject，选择指定项
    def click_subject2(self):
        subject2 = self.find_element((By.XPATH, self.subject2))
        subject2.click()
        # subject2_all = self.find_element((By.CSS_SELECTOR, self.all_subject))
        sleep(1)
        self.find_element((By.CSS_SELECTOR, self.all_subject)).find_elements(By.TAG_NAME, self.subject2_select)[2].click()
        

    def click_MDPI_topics(self):
        self.find_elements((By.CSS_SELECTOR, self.mdpi_topic))[-1].click()
        open_topic = self.find_element((By.CSS_SELECTOR, "ul[class='common-field__options']"))
        # self.driver.implicitly_wait(10)
        sleep(1)
        open_topic.find_elements(By.TAG_NAME, self.mdpi_topic_select)[2].click()

    def click_next(self):  #步骤1
        # js = "document.documentElement.scrollTop=500"
        # self.driver.execute_script(js)  # 下滑滚动条
        self.find_elements((By.CSS_SELECTOR, "button[type='submit']"))[0].click()


    def click_next1(self):  #步骤2
        # js = "document.documentElement.scrollTop=500"
        # self.driver.execute_script(js)  # 下滑滚动条
        self.find_elements((By.CSS_SELECTOR, "button[type='submit']"))[1].click()

    def click_next2(self):  #步骤4，
        # js = "document.documentElement.scrollTop=500"
        # self.driver.execute_script(js)  # 下滑滚动条
        self.find_elements((By.CSS_SELECTOR, "button[type='submit']"))[-1].click()
        

    def click_next_button(self):   #步骤3，5 用的button类型
        js = 'window.scrollTo(0,500)'
        self.driver.execute_script(js)  # 下滑滚动条
        buttons = self.find_elements((By.CSS_SELECTOR, "div[class='flex pt-lg']"))[1]
        self.driver.implicitly_wait(10)
        BT = buttons.find_elements(By.CSS_SELECTOR, "button[type='button']")[-1]
        BT.click()
        

    # 选择type
    def click_type(self):
        type_parent = self.find_element((By.XPATH, self.type))
        js = 'window.scrollTo(0,200)'
        self.driver.execute_script(js)  # 下滑滚动条
        type_parent.click()
        self.driver.implicitly_wait(10)
        type_parent.find_elements(By.TAG_NAME, self.type_select)[0].click()
        

    # 输入title/abstract/keywords
    def input_content(self, item, content):
        iframes_input = self.find_elements((By.CLASS_NAME, self.input_iframe))
        if item == 'title':
            # title_frame = self.find_element((By.XPATH, self.title)
            title_frame = iframes_input[0]
            self.driver.switch_to.frame(title_frame)
            
            self.find_element((By.XPATH, self.input)).send_keys(content)
            self.driver.switch_to.parent_frame()
        elif item == 'abstract':
            # abstract_frame = self.find_element((By.XPATH, self.abstract)
            abstract_frame = iframes_input[1]
            self.driver.switch_to.frame(abstract_frame)
            
            self.find_element((By.XPATH, self.input)).send_keys(content)
            self.driver.switch_to.parent_frame()
        elif item == 'keywords':
            # keywords_frame = self.find_element((By.XPATH, self.keywords)
            keywords_frame = iframes_input[2]
            self.driver.switch_to.frame(keywords_frame)
            
            self.find_element((By.XPATH, self.input)).send_keys(content)
            self.driver.switch_to.parent_frame()
        

    # 输入affiliation
    def input_affi(self, content):
        
        self.find_element((By.NAME, self.affiliation)).send_keys(content)

    # 选择region
    def click_region(self):
        reg = self.find_element((By.NAME, self.region))
        reg.click()
        self.driver.implicitly_wait(10)
        country = reg.find_elements(By.TAG_NAME, "option")
        country[0].click()
        # self.find_element((By.XPATH, self.region_select).click()


    # 勾选corresponding author and confirm
    def click_corresponding(self, content):
        self.click_radio = self.find_elements((By.CSS_SELECTOR, self.check_dot))
        if content == 'yes':
            self.click_radio[0].click()
        elif content == "No":
            self.click_radio[1].click()
            self.driver.implicitly_wait(10)

    def click_confirm(self):
        self.find_element((By.NAME, self.confirm)).click()

    # 勾选declarations
    def click_declarations(self,s1,s2):
        ethical_check = self.find_element((By.ID,"ethicalApprovalCheck")).find_elements(By.CSS_SELECTOR, "div[role='radio']")
        ethical_file = self.find_element((By.ID, "approvePublicationcheck")).find_elements(By.CSS_SELECTOR, "div[role='radio']")
        self.driver.implicitly_wait(10)
        time.sleep(2)
        if s1 == 'yes':
            ethical_check[0].click()
        elif s1 == "no":
            ethical_check[-1].click()

        if s2 == 'yes':
            ethical_file[0].click()
        elif s2 == "no":
            ethical_file[-1].click()


    # 上传文件
    def upload_file(self, filetype, file_path):
        # time.sleep(2)
        file_flame = self.find_element((By.XPATH, '//*[@id="__nuxt"]/div[2]/div[1]/div/div/div[6]'))
        up_buttons = file_flame.find_elements(By.CSS_SELECTOR, 'button[type=button]')
        if filetype == 'paper':
            up_buttons[0].click()
            sleep(1)
            pyperclip.copy(file_path)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter', 3)

        elif filetype == 'pdf':
            up_buttons[1].click()
            pyperclip.copy(file_path)
            sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter', 3)

        elif filetype == 'ga':
            up_buttons[2].click()
            pyperclip.copy(file_path)
            sleep(1)
            pyautogui.hotkey('ctrl', 'v')

            pyautogui.press('enter', 2)
        elif filetype == 'figures':
            up_buttons[3].click()
            sleep(1)
            pyperclip.copy(file_path)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter', 3)

        elif filetype == 'supple':
            up_buttons[4].click()
            sleep(1)
            pyperclip.copy(file_path)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter', 3)

        # time.sleep(8)

    def click_accpet(self):
        self.find_element((By.NAME, self.accept)).click()
        

    def click_confirm_submit(self):
        self.find_elements((By.CSS_SELECTOR,
                                  "button[class='m-button m-button--md m-button--primary rounded']"))[-1].click()

        

    def click_proceed(self):
        proceed = self.find_element((By.CSS_SELECTOR, self.proceed_gap))
        proceed.find_elements(By.TAG_NAME, "button")[1].click()
        self.driver.implicitly_wait(10)
        

    def get_preprint_id(self):
        return self.find_element((By.XPATH,"//p[contains(text(),'1')]")).text

    def get_status(self):
        return self.find_element((By.XPATH,'//*[@id="__nuxt"]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[1]')).text

