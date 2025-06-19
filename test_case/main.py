from datetime import datetime

import allure
import pytest

from page_object.submit_op import PageObjectSubmit
from test_flow import test_submit_flow,test_process


class TestCase:
    # now_time = datetime.now()
    # current_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
    # @pytest.fixture(autouse=True)
    # def setUp(self,login):
    #     self.driver = login
    #     self.hold=PageObjectSubmit(self.driver)
    #     yield
    #
    # def tearDown(self):
    #     self.driver.quit()

    @allure.feature("test_submit_flow")
    @allure.story("test_submit_new_preprints")
    # @pytest.mark.parametrize("test_data",get_data())
    def test_submit_new(self,login):
        test_submit_flow.TestAddPreprints().test_add_new_preprints(login)


    @allure.feature("test_process")
    @allure.story("test_process")
    def test_check(self,login):
        test_process.TestProcess().test_check(login)


