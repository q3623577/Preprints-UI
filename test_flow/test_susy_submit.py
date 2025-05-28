import unittest

import pytest

from page_object.susy_submit import *
import time

class Test_susy_submit(unittest.TestCase):

    # def test_susy_submit(self):
    #     pass

    @classmethod
    def setUpClass(cls):
        # susy_login('zhuohu.guo@mdpi.com', 'Guozhuohu12345@')
        susy_login('Author&ExternalEditor@gmial.com','Susy123456')

    # @classmethod
    # def tearDownClass(cls):
    #     dr.find_element_by_xpath('//*[@id="topmenu"]/ul/li[1]/form/input[2]').click()
    #     # dr.quit()
    #     dr.close()
    #     # pass

    def test_submit_step1(self):
        submit_step1_1()
        Expected = "MDPI | New Submission - Input Author Details | Step 2"
        time.sleep(1)
        Actual = dr.title
        self.assertEqual(Expected, Actual, msg="断言失败，进入的不是投稿第2步")

    def test_submit_step2(self):
        submit_step2()
        dr.implicitly_wait(10)
        Expected = "MDPI | New Submission - Input Reviewers Details | Step 3"
        time.sleep(1)
        Actual = dr.title
        self.assertEqual(Expected, Actual, msg="断言失败，进入的不是投稿第3步")

    # @pytest.mark.skip
    def test_submit_step3(self):
        submit_step3()
        Expected = "MDPI | New Submission - Upload Manuscript | Step 4"
        time.sleep(1)
        Actual = dr.title
        self.assertEqual(Expected, Actual, msg="断言失败，进入的不是投稿第4步")

    # @pytest.mark.skip
    def test_submit_step4(self):
        submit_step4()
        Expected = "MDPI | New Submission - Confirm Your Submission | Step 5"
        time.sleep(1)
        Actual = dr.title
        self.assertEqual(Expected, Actual, msg="断言失败，进入的不是投稿第5步")

    # @pytest.mark.skip
    def test_submit_step5(self):
        submit_step5()
        Expected = "MDPI Susy"
        time.sleep(1)
        Actual = dr.title
        self.assertEqual(Expected, Actual, msg="断言失败，进入的不是投稿完成页面")

if __name__ == '__main__':
    unittest.main()
