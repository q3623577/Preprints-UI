# from test_case.test_addnew import TestAddNewPreprints
# from test_case.test_process import TestProcess
#
# import allure
#
# class TestMain:
#
#     def test_new(self,set_data):
#         TestAddNewPreprints().test_add_new_preprints(set_data)
#
#     def test_process_check(self,get_data):
#         TestProcess().test_check(get_data)


import datetime

# 创建日期对象
date_str = "2024-11-22"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")

# 将日期对象转化为Unix时间戳
timestamp = int(date_obj.timestamp())

print(timestamp)