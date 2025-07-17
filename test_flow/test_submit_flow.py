import os
import time
from datetime import datetime

import pytest

from tool_uint import file_op
from tool_uint.excel_op import ExcelOp
from tool_uint.log_op import logger
from page_object.submit_op import PageObjectSubmit


#登录
directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + r'\testdata'


class TestAddPreprints:
    now_time = datetime.now()
    current_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
    # @pytest.fixture(autouse=True)
    # def setUp(self,login):
    #     self.driver = login
    #     self.hold=PageObjectSubmit(self.driver)
    #     yield
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_add_new_preprints(self,login):
        submit_new =PageObjectSubmit(login)
        submit_new.click_submit()
        submit_new.click_agree()
        submit_new.click_add_new()
        logger.info("点击添加新稿件成功, 进入投稿页面")

        #投稿第一步
        submit_new.click_subject()
        submit_new.click_subject2()
        submit_new.click_MDPI_topics()
        js = "document.documentElement.scrollTop=500"
        login.execute_script(js)  # 下滑滚动条
        submit_new.click_next()
        logger.info("投稿第一步成功")

        # 投稿第二步
        submit_new.click_type()
        time.sleep(10)
        submit_new.input_content('title',self.current_time+" title")
        submit_new.input_content('abstract',self.current_time+" ab")
        submit_new.input_content('keywords',self.current_time+" key")
        time.sleep(2)
        js = "document.documentElement.scrollTop=1000"
        login.execute_script(js)  # 下滑滚动条
        submit_new.click_next1()
        logger.info("投稿第二步成功")

        # 投稿第三步
        submit_new.input_affi(self.current_time+" affi")
        submit_new.click_region()
        submit_new.click_corresponding("yes")
        submit_new.click_confirm()
        submit_new.click_next_button()
        logger.info("投稿第三步成功")

        # 投稿第四步
        submit_new.click_declarations('no','no')
        submit_new.click_next2()
        logger.info("投稿第四步成功")

        # 投稿第五步
        docx_path=file_op.get_file_dir('.docx')
        submit_new.upload_file('paper',docx_path)
        pdf_path=file_op.get_file_dir('.pdf')
        submit_new.upload_file('pdf', pdf_path)
        submit_new.click_accpet()
        time.sleep(10)
        submit_new.click_confirm_submit()
        submit_new.click_proceed()
        logger.info("投稿第五步成功")

        # 投稿第六步 存储数据
        time.sleep(5)
        preprint_id = submit_new.get_preprint_id()
        status = submit_new.get_status()
        excel_op = ExcelOp()
        excel_op.add_data([preprint_id,status,self.current_time])
        excel_op.save_data()
        logger.info("保存preprints_id数据成功")
        file_op.replace_numbers(directory,['.zip','.dox','.docx','.pdf'],replacement=preprint_id)  # 将数字替换为"NUM"
        # print(preprint_id) # set_data("ppid",preprint_id)

    # 投稿follow-up version
    def test_follow_new_preprints(self,login):
        submit_new =PageObjectSubmit(login)
        submit_new.click_submit()
        submit_new.click_agree()
        time.sleep(5)
        submit_new.click_add_follow()
        submit_new.pp_select_list()
        submit_new.input_detail_of_change('this is UI test content'+self.current_time)

        logger.info("点击添加follow稿件成功, 进入投稿页面")

        #投稿第一步
        submit_new.click_subject()
        submit_new.click_subject2()
        submit_new.click_MDPI_topics()
        js = "document.documentElement.scrollTop=500"
        login.execute_script(js)  # 下滑滚动条
        submit_new.click_next()
        logger.info("投稿第一步成功")

        # 投稿第二步
        submit_new.click_type()
        time.sleep(5)
        submit_new.input_content('title',self.current_time+" title")
        submit_new.input_content('abstract',self.current_time+" ab")
        submit_new.input_content('keywords',self.current_time+" key")
        time.sleep(1)
        js = "document.documentElement.scrollTop=1000"
        login.execute_script(js)  # 下滑滚动条
        submit_new.click_next1()
        logger.info("投稿第二步成功")

        # 投稿第三步
        submit_new.input_affi(self.current_time+" affi")
        submit_new.click_region()
        submit_new.click_corresponding("yes")
        submit_new.click_confirm()
        submit_new.click_next_button()
        logger.info("投稿第三步成功")

        # 投稿第四步
        submit_new.click_declarations('no','no')
        submit_new.click_next2()
        logger.info("投稿第四步成功")

        # 投稿第五步
        submit_new.upload_file('paper',r'E:\test-data\test_auto\preprints-132659-manuscript.docx')
        submit_new.upload_file('pdf', r'E:\test-data\test_auto\preprints-132659-final_file.pdf')
        submit_new.click_accpet()
        time.sleep(10)
        submit_new.click_confirm_submit()
        submit_new.click_proceed()
        logger.info("投稿第五步成功")

        # 投稿第六步 存储数据
        time.sleep(5)
        preprint_id = submit_new.get_preprint_id()
        status = submit_new.get_status()
        excel_op = ExcelOp()
        excel_op.add_data([preprint_id,status,self.current_time])
        excel_op.save_data()
        logger.info("保存preprints_id数据成功")




    # AddPreprints().add_new_preprints(set_data)
    # AddPreprints().follow_new_preprints()E:\test-data\test_4\preprints-132659-final_file.pdf

    
