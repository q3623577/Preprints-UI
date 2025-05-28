import allure

from page_object import backend_pocess
import pytest
from page_object.login_op import page

class TestProcess:

    @allure.story("稿件处理--check")
    def test_check(self,get_data):
        process = backend_pocess.Process_Manu(page.driver)
        process.open_browser()
        process.open_detail_page(get_data("ppid"))
        process.check_list()
        process.click_accept("ok")

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

