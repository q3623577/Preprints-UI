import time

import unittest
from page_object.login_op import TestOpenPage
from page_object.submit_op import PageObjectSubmit
import pytest
import allure
# from test_case.conftest import set_data, get_data
from datetime import datetime
#登录





class TestAddPreprints:
    now_time = datetime.now()
    current_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
    @pytest.fixture(autouse=True)
    def setUp(self,login):
        self.driver = login
        self.hold=PageObjectSubmit(self.driver)
        yield

    def tearDown(self):
        self.driver.quit()

    def test_add_new_preprints(self):
        submit_new =self.hold
        submit_new.click_submit()
        submit_new.click_agree()
        submit_new.click_add_new()

        #投稿第一步
        submit_new.click_subject()
        submit_new.click_subject2()
        submit_new.click_MDPI_topics()
        js = "document.documentElement.scrollTop=500"
        self.driver.execute_script(js)  # 下滑滚动条
        submit_new.click_next()

        # 投稿第二步
        submit_new.click_type()
        submit_new.input_content('title',self.current_time+" title")
        submit_new.input_content('abstract',self.current_time+" ab")
        submit_new.input_content('keywords',self.current_time+" key")
        time.sleep(1)
        js = "document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)  # 下滑滚动条
        submit_new.click_next1()

        # 投稿第三步
        submit_new.input_affi(self.current_time+" affi")
        submit_new.click_region()
        submit_new.click_corresponding("yes")
        submit_new.click_confirm()
        submit_new.click_next_button()

        # 投稿第四步
        submit_new.click_declarations('no','no')
        submit_new.click_next2()

        # 投稿第五步
        submit_new.upload_file('paper',r'E:\test-data\test_4\preprints-132659-manuscript.docx')
        submit_new.upload_file('pdf', r'E:\test-data\test_4\preprints-132659-final_file.pdf')
        submit_new.click_accpet()
        submit_new.click_confirm_submit()


        submit_new.click_proceed()
        # page.driver.implicitly_wait(10)

        # preprint_id = submit_new.get_preprint_id()
        # set_data("ppid",preprint_id)

    # 投稿follow-up version
    def test_follow_new_preprints(self,login):
        submit_follow = login
        submit_follow.click_submit()
        submit_follow.click_agree()
        submit_follow.click_add_follow()
        time.sleep(3)
        submit_follow.click_pp_select()
        submit_follow.input_detail_of_change("test_auto in "+self.current_time)
        submit_follow.click_next()

        #投稿第一步,不修改，直接跳过
        submit_follow.click_next()

        # 投稿第二步
        submit_follow.input_content('title'," follow version ")
        submit_follow.click_next()

        # 投稿第三步
        submit_follow.click_confirm()
        submit_follow.click_next_button()

        # 投稿第四步
        submit_follow.click_next_button()

        # 投稿第五步
        submit_follow.upload_file('paper',r'E:\test-data\test_4\preprints-132659-manuscript.docx')
        submit_follow.upload_file('pdf', r'E:\test-data\test_4\preprints-132659-final_file.pdf')
        submit_follow.click_accpet()
        submit_follow.click_confirm_submit()
        submit_follow.click_proceed()
        # page.driver.implicitly_wait(10)
        # preprint_id = submit_follow.get_preprint_id()



if __name__ == '__main__':
    # AddPreprints().add_new_preprints(set_data)
    # AddPreprints().follow_new_preprints()E:\test-data\test_4\preprints-132659-final_file.pdf
    
    

    time.sleep(120)