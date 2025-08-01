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
        time.sleep(2)
        # print(preprint_id) # set_data("ppid",preprint_id)

    # 投稿follow-up version
    def test_follow_new_preprints(self,login):
        submit_new =PageObjectSubmit(login)
        submit_new.click_submit()
        time.sleep(2)
        submit_new.click_agree()
        time.sleep(5)
        submit_new.click_add_follow()
        time.sleep(8)
        submit_new.click_pp_select()
        logger.info("点击添加follow稿件成功, 进入投稿页面")

        #投稿第1步
        time.sleep(2)
        submit_new.input_detail_of_change('this is UI test content'+self.current_time)
        time.sleep(2)
        submit_new.click_next()
        logger.info("投稿第1步成功")

        #投稿第2步
        # submit_new.click_subject()
        # submit_new.click_subject2()
        # submit_new.click_MDPI_topics()
        time.sleep(2)
        js = "document.documentElement.scrollTop=500"
        login.execute_script(js)  # 下滑滚动条
        submit_new.click_next1()
        logger.info("投稿第2步成功")

        # 投稿第3步
        # submit_new.click_type()
        time.sleep(5)
        submit_new.input_content_follow('title'," version 2")
        submit_new.input_content_follow('abstract',"version 2")
        submit_new.input_content_follow('keywords',"version 2")
        time.sleep(1)
        js = "document.documentElement.scrollTop=1000"
        login.execute_script(js)  # 下滑滚动条
        submit_new.follow_next()
        logger.info("投稿第3步成功")

        # 投稿第4步
        # submit_new.input_affi(self.current_time+" affi")
        # submit_new.click_region()
        # submit_new.click_corresponding("yes")
        time.sleep(3)
        js = "document.documentElement.scrollTop=500"
        login.execute_script(js)
        submit_new.click_confirm()
        submit_new.follow_next1()
        logger.info("投稿第4步成功")

        # 投稿第5步
        # submit_new.click_declarations('no','no')
        time.sleep(2)
        submit_new.click_next2()
        logger.info("投稿第5步成功")

        # 投稿第6步
        docx_path=file_op.get_file_dir('.docx')
        submit_new.upload_file_follow('paper',docx_path)
        pdf_path=file_op.get_file_dir('.pdf')
        submit_new.upload_file_follow('pdf', pdf_path)
        submit_new.click_accpet()
        time.sleep(10)
        submit_new.click_confirm_submit()
        submit_new.click_proceed()
        logger.info("投稿第6步成功")

        # 投稿第7步 存储数据
        time.sleep(5)
        preprint_id = submit_new.get_preprint_id()
        status = submit_new.get_status()
        excel_op = ExcelOp()
        excel_op.add_data([preprint_id,status,self.current_time])
        excel_op.save_data()
        logger.info("保存preprints_id数据成功")
        time.sleep(2)


    
