import allure
from test_flow import test_submit_flow,test_process
import pytest

class TestCase:

    @allure.feature("test_submit_flow")
    @allure.story("test_submit_new_preprints")
    def test_submit_new(self,login):
        test_submit_flow.TestAddPreprints().test_add_new_preprints(login)

    @allure.feature("test_process")
    @allure.story("test_process_check")
    def test_check(self,login):
        test_process.TestProcess().test_check(login)

    @allure.feature("test_process")
    @allure.story("test_process_sanctions_check")
    def test_sanctions_check(self,login):
        test_process.TestProcess().test_sanctions_check(login)

    @allure.feature("test_process")
    @allure.story("test_process_accept")
    def test_accept(self,login):
        test_process.TestProcess().test_accept(login)

    @allure.feature("test_process")
    @allure.story("test_process_online")
    def test_online(self,login):
        test_process.TestProcess().test_online(login)





