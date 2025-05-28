from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
import  time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from datetime import datetime



dr = webdriver.Chrome()
now_time = datetime.now()
current_time = now_time.strftime("%Y-%m-%d %H:%M:%S")

def susy_login(email,password):
    # dr = webdriver.Chrome()
    # dr.implicitly_wait(10)
    dr.maximize_window()
    # 登录
    dr.get('http://deployment.susy.mdpi.test/')
    try:
      dr.find_element(by=By.ID,value='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()  # 弹窗确认
    except:
        pass
    time.sleep(2)
    dr.find_element(by=By.XPATH, value='//*[@id="susy-home-page"]/div/a[1]').click()  # 点击login
    dr.find_element(by= By.ID,value='username').send_keys(email)  # 输入账号
    dr.find_element(by= By.ID,value='password').send_keys(password)  # 输入密码
    dr.find_element(by=By.XPATH, value='/html/body/main/div/div[2]/div[2]/div[1]/form/div/div[3]/input[2]').click() # 点击继续
    dr.find_element(by=By.XPATH, value="//button[@id='CybotCookiebotDialogBodyButtonAccept']").click()



def submit_step1_1():    #常规投稿
    # 作者投稿
    dr.implicitly_wait(10)
    dr.find_element(by=By.XPATH, value="//a[contains(text(),'Submit')]").click()  # 点击投稿菜单
    dr.implicitly_wait(10)
    dr.find_element(by=By.ID, value='form_template_used_0').click()  # 勾选使用模版
    dr.implicitly_wait(10)
    path1 = os.path.dirname(os.path.dirname(__file__))
    path2 = r'testdata\Auto_submission_file.docx'
    path3 = os.path.join(path1, path2) #拼接出文件路径，即投稿文件
    dr.find_element(by=By.ID, value='form_manuscript_file').send_keys(path3)  # 上传投稿文件
    dr.implicitly_wait(10)
    dr.find_element(by=By.XPATH, value=
        '//*[@id="maincol"]/div[1]/div[2]/div/div[2]/div[1]/fieldset/form/div[5]/div[2]/input').click()  # 点击上传
    # 投稿第一步
    dr.find_element(by=By.XPATH, value='//*[@id="form_journal_id_chosen"]').click()  # 点击期刊下拉框
    dr.implicitly_wait(10)
    dr.find_element(by=By.XPATH, value='//*[@id="form_journal_id_chosen"]/div/ul/li[2]').click()  # 选择Agriculture期刊

    dr.find_element(by=By.XPATH, value='//*[@id="form_article_type_id_chosen"]').click()  # 点击文章类型选择框

    js = "document.documentElement.scrollTop=100000"
    dr.execute_script(js)  # 下滑滚动条
    time.sleep(2)
    dr.find_element(by=By.XPATH, value='//*[@id="form_article_type_id_chosen"]/div/ul/li[2]').click()  # 选择article类型
    dr.find_element(by=By.ID, value='form_title').send_keys('UI auto_test_title_to_preprints '+current_time)  # 输入标题名称
    dr.find_element(by=By.ID, value='form_abstract').send_keys('UI auto_test_abstract')  # 输入摘要
    js = "document.documentElement.scrollTop=100000"
    dr.execute_script(js)  # 下滑滚动条
    time.sleep(2)
    # dr.find_element(by=By.ID, value='form_keywords').send_keys('UI auto_test_keywords')  #输入keywords
    #dr.find_element(by=By.ID, value='form_instructions').click()  # 勾选条款
    # dr.find_element(by=By.XPATH, value='//*[@id="maincol"]/div[2]/form/div/fieldset/div[22]/div[2]/input').click()

    dr.find_element(by=By.CSS_SELECTOR,value="input[value='Proceed to the next step']").click() # 点击进入下一步
    # time.sleep(2)

def submit_step1_2():     #特刊投稿
    # 作者投稿
    dr.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[2]/ul/li[1]/a').click()  # 点击投稿菜单
    dr.implicitly_wait(10)
    dr.find_element(by=By.ID, value='form_template_used_0').click()  # 勾选使用模版
    path1 = os.path.dirname(os.path.dirname(__file__))
    path2 = r'testdata\Auto_submission_file.docx'
    path3 = os.path.join(path1, path2) #拼接出文件路径，即投稿文件
    dr.find_element(by=By.ID, value='form_manuscript_file').send_keys(path3)  # 上传投稿文件
    dr.implicitly_wait(10)
    dr.find_element(by=By.XPATH, value=
        '//*[@id="maincol"]/div[1]/div[2]/div/div[2]/div[1]/fieldset/form/div[5]/div[2]/input').click()  # 点击上传
    # 投稿第一步
    dr.find_element(by=By.XPATH, value='//*[@id="form_journal_id_chosen"]').click()  # 点击期刊下拉框
    dr.implicitly_wait(10)
    dr.find_element(by=By.XPATH, value='//*[@id="form_journal_id_chosen"]/div/ul/li[9]').click()  # 选择Agriculture期刊


    dr.find_element(by=By.XPATH, value='//*[@id="form_search_topic_chosen"]').click()   #点击特刊选择框
    time.sleep(2)
    dr.find_element(by=By.XPATH, value='//*[@id="form_search_topic_chosen"]/div/ul/li[9]').click()   #选择"test merrin"特刊

    dr.find_element(by=By.XPATH, value='//*[@id="form_article_type_id_chosen"]').click()  # 点击文章类型选择框
    time.sleep(2)
    dr.find_element(by=By.XPATH, value='//*[@id="form_article_type_id_chosen"]/div/ul/li[3]').click()  # 选择article类型
    dr.find_element(by=By.ID, value='form_title').send_keys('UI auto_test_title')  # 输入标题名称
    dr.find_element(by=By.ID, value='form_abstract').send_keys('UI auto_test_abstract')  # 输入摘要
    js = 'window.scrollTo(0,500)'
    dr.execute_script(js)  # 下滑滚动条
    #dr.find_element(by=By.ID, value='form_instructions').click()  # 勾选条款
    dr.find_element(by=By.XPATH, value='//*[@id="maincol"]/div[2]/form/div/fieldset/div[22]/div[2]/input').click()  # 点击进入下一步

def submit_step2():
    # 投稿第二步
    # dr.implicitly_wait(10)
    time.sleep(2)
    dr.find_element(by=By.NAME, value='form[email_1]').send_keys('zhuohu.guo@mdpi.com')  # 输入机构邮箱
    dr.find_element(by=By.NAME, value='form[firstname_1]').send_keys('zhuohu')  # 输入名字
    dr.find_element(by=By.NAME, value='form[lastname_1]').send_keys('guo')  # 输入姓氏
    dr.find_element(by=By.ID, value='form_corresponding_1_0').click()  # 是否通讯作者
    # dr.find_element(by=By.ID, value='form_submitting_author_1_0').click()  # 是否提交作者
    dr.find_element(by=By.ID, value='form_title_id_1').click()  # 点击头衔下拉框
    dr.find_element(by=By.XPATH, value='//*[@id="form_title_id_1"]/option[2]').click()  # 选择头衔
    js = 'window.scrollTo(0,600)'
    dr.execute_script(js)  # 下滑滚动条
    dr.find_element(by=By.XPATH, value='//*[@id="form_country_id_1_chosen"]').click()  # 点击国家下拉框
    dr.implicitly_wait(10)
    dr.find_element(by=By.XPATH, value='//*[@id="form_country_id_1_chosen"]/div/ul/li[2]').click()  # 选择国家
    action = ActionChains(dr)  # 选择机构
    e = dr.find_element(by=By.CSS_SELECTOR, value='ul[class="tag-editor ui-sortable"]')  # 选择机构
    action.click(e)  # 选择机构
    action.send_keys('The University of Melbourne')  # 选择机构
    # action.move_by_offset(50,50).click()
    action.perform()  # 选择机构
    # dr.find_element(by=By.XPATH, value='//*[@id="form_sync_cv_1"]/label[2]').click()  # 是否展示作者生平
    # dr.find_element(by=By.ID, value='form_sync_cv_1_1').click()  # 是否展示作者生平
    # js1 = "var d=document.getElementById('form_short_cv_1');d.value='It is biography.';"  # 输入作者生平
    # dr.execute_script(js1)
    # time.sleep(1)
    print("what hell0")
    js = 'window.scrollTo(0,1100)'
    dr.execute_script(js)  # 下滑滚动条
    time.sleep(2)
    try:
        for i in range(5):
            if dr.title == "MDPI | New Submission - Input Reviewers Details | Step 3":
                break
            else:
                dr.find_element(by=By.ID, value='proceed-to-step3').click()
                dr.implicitly_wait(10)# 确认姓名 进入下一步
    except NoSuchElementException:
        print("what hell!!!")
    #dr.find_element(by=By.ID, value='form_checklist_1').click()  # 勾选条款1
    #dr.find_element(by=By.ID, value='form_checklist_2').click()  # 勾选条款2
    #dr.find_element(by=By.ID, value='form_checklist_3').click()  # 勾选条款3

    # time.sleep(10)

def submit_step3():
    #投稿第三步
    js = 'window.scrollTo(0,400)'
    dr.execute_script(js)  # 下滑滚动条
    dr.implicitly_wait(5)
    # dr.find_element(by=By.ID, value='journal_editorial_board').click()  # 点击期刊编辑面板
    # time.sleep(3)
    # dr.find_element(by=By.XPATH, value='//*[@id="editor_board_dialog"]/div/table/tbody/tr[1]/td[1]/input').click()  # 选审稿人
    # dr.find_element(by=By.XPATH, value='//*[@id="editor_board_dialog"]/div/table/tbody/tr[2]/td[1]/input').click()  # 选审稿人
    # dr.find_element(by=By.XPATH, value='//*[@id="editor_board_dialog"]/div/table/tbody/tr[3]/td[1]/input').click()  # 选审稿人
    # dr.find_element(by=By.XPATH, value='//*[@id="wholebody"]/div[29]/div[3]/div/button[1]').click()  # 点击添加按钮

    js = 'window.scrollTo(0,1300)'
    dr.execute_script(js)  # 下滑滚动条
    dr.find_element(by=By.NAME, value='process_next').click()  # 点击进入下一步

def submit_step4():
    #投稿第四步
    js = 'window.scrollTo(0,600)'
    dr.execute_script(js)  # 下滑滚动条
    dr.find_element(by=By.NAME, value='coverletter_text').send_keys("It is coverletter.")  # 输入推荐信
    dr.find_element(by=By.ID, value='permission_file_choice_2').click()  # 没有版权问题
    js = 'window.scrollTo(0,1400)'
    dr.execute_script(js)  # 下滑滚动条
    dr.find_element(by=By.ID, value='funding_info_choice_2').click()  # 无funding
    dr.find_element(by=By.ID, value='potential_conflict_choice_2').click()  # 无conflict
    js = 'window.scrollTo(0,1900)'
    dr.execute_script(js)  # 下滑滚动条
    dr.find_element(by=By.ID, value='gen_ai_choice_2').click()  #未使用AI写作
    dr.find_element(by=By.ID, value='form_published_elsewhere_4').click()  # 未被发表过
    js='window.scrollTo(0,2200)'
    dr.execute_script(js) # 下滑滚动条
    dr.find_element(by=By.ID, value='recruiting_reviewers_choice_2').click()  #招聘审稿人
    dr.find_element(by=By.ID, value='open_review_choice_1').click() #开放同行评审
    dr.execute_script('window.scrollTo(0,4000)')
    dr.find_element(by=By.ID, value='form_available_repository_1').click()  #数据仓库
    dr.find_element(by=By.XPATH, value='//*[@id="minor-english-editing"]/div/div[2]/div[1]/div[1]/span[2]/input').click() #English edit
    dr.find_element(by=By.ID, value='uploadAll').click()  # 进入下一步

def submit_step5():
    # 投稿第五步
    time.sleep(1)
    js = 'window.scrollTo(0,2000)'
    dr.execute_script(js)  # 下滑滚动条
    time.sleep(1)
    dr.find_element(by=By.ID, value='form_terms_and_conditions').click()  # 勾选条款1
    dr.find_element(by=By.ID, value='form_confirm_terms_of_use').click()  # 勾选条款2
    dr.find_element(by=By.ID, value='form_confirm_understand_policies').click()  # 勾选条款3
    dr.find_element(by=By.ID, value='final_step').click()  # 提交给编辑
    time.sleep(3)
    dr.find_element(by=By.CSS_SELECTOR, value="button[class='btn btn-default']").click()  # 关闭调查弹窗
    # js_2 = 'window.scrollTo(0,1000)'
    dr.execute_script('window.scrollTo(0,600)')  # 下滑滚动条
    dr.find_element(by=By.NAME, value='post_preprints_choice').click() #转投preprints
     #打开 subject下拉框
    dr.find_element(by=By.XPATH, value='//*[@id="subject"]/option[2]').click()
    dr.implicitly_wait(10)
    dr.find_element(by=By.XPATH, value='//*[@id="sub-subject"]/option[2]').click()
    dr.execute_script('window.scrollTo(0,700)')
    dr.find_element(by=By.ID, value ='preprints_doi_apply').click()
    dr.find_element(by=By.ID,value='post_preprints_submit_btn').click()


