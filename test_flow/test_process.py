import allure
import pytest
from page_object.log_op import logger
from page_object import backend_pocess
from page_object.excel_op import ExcelOp


class TestProcess:

    @allure.story("稿件处理--check")
    def test_check(self,login):
        process = backend_pocess.Process_Manu(login)
        process.open_browser()
        excel_op = ExcelOp()
        preprints_id = excel_op.get_data()[-1][0]
        logger.info("获取preprints_id成功："+preprints_id)
        process.open_detail_page(preprints_id)
        logger.info("打开详情页成功")
        process.check_list()
        logger.info("check-list成功")
        # process.click_accept("ok")
        excel_op.update_data(preprints_id,"checked")
        logger.info("更新excel成功")
        excel_op.save_data()
        logger.info("保存excel成功")

    def test_sanctions_check(self,login):
        process = backend_pocess.Process_Manu(login)
        process.check_sanctions('no','no')
        logger.info("sanctions-check成功")


    @pytest.mark.skip
    def test_accept(self,login):
        process = backend_pocess.Process_Manu(login)
        process.click_accept('ok')
        logger.info("accept成功")


    @pytest.mark.skip
    def test_Send_AB(self):
        pass

    @pytest.mark.skip
    def test_modification(self):
        pass

    @pytest.mark.skip
    def test_confirmation(self):
        pass

    @pytest.mark.skip
    def test_reject(self):
        pass

    @pytest.mark.skip
    def test_withdraw(self):
        pass

