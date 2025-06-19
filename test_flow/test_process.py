import allure
import pytest

from page_object import backend_pocess
from page_object.excel_op import ExcelOp


class TestProcess:

    @allure.story("稿件处理--check")
    def test_check(self,login):
        process = backend_pocess.Process_Manu(login)
        process.open_browser()
        excel_op = ExcelOp()
        preprints_id = excel_op.get_data()[-1][0]
        process.open_detail_page(preprints_id)
        process.check_list()
        process.click_accept("ok")
        excel_op.update_data(preprints_id,"checked")


    @pytest.mark.skip
    def test_accept(self):
        pass

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

