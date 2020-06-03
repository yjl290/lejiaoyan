from time import sleep

from Page_SerachQuestion import Search_Question
from Util import Get_Element, MongoDB_Data

driver = None
mongo = MongoDB_Data.Mongo_Data()

class Search_paper():

    def __init__(self, driver):
        self.driver = driver
        self.search_paper = Get_Element.Search_Page_Elements(self.driver)
        self.keyword = "自动测试试卷名"

    # 我的试卷
    def screen_condition(self):
        self.search_paper = Get_Element.Search_Page_Elements(self.driver)
        self.search_paper.move_top()
        self.search_paper.move_mouse("Navigation", "move_mouse_my")
        sleep(1)
        self.search_paper.click_button("Navigation", "button_mypaper")
        sleep(1)

    # 搜索
    def button_search(self):
        try:
            self.search_paper.click_button("paper", "paper_search")
        except:
            self.search_paper.click_script("paper", "paper_search")
    # 重置
    def button_reset(self):
        self.search_paper.click_button("paper", "paper_reset")

    # 关键字
    def screen_search_input(self):
        self.search_paper.clear_input("paper", "paper_input")
        self.search_paper.input_string(self.keyword, "paper", "paper_input")
    # 添加试卷
    def add_paper(self):
        self.search_paper.click_button("paper", "add_paper")
        self.search_paper.input_string('自动测试试卷名', "paper", "add_paper_name")
        sleep(1)
        self.search_paper.click_script("paper", "add_paper_class")
        sleep(1)
        self.search_paper.click_button("paper", "add_paper_class31")
        self.search_paper.click_script("paper", "add_paper_ok")
        sleep(2)
        # 编辑试卷
        self.search_paper.switch_new_page()
        self.search_paper.click_button("paper", "editpaper_moduledelete")
        self.search_paper.click_button("paper", "editpaper_moduleadd")
        sleep(1)
        self.search_paper.input_string("11111", "paper", "editpaper_moduleadd_name")
        self.search_paper.click_button("paper", "editpaper_moduleadd_ok")
        sleep(1)
        self.search_paper.click_button("paper", "editpaper_moduleadd_clickname")
        self.search_paper.input_string("11111", "paper", "editpaper_moduleadd_inputname")
        self.search_paper.click_button("paper", "editpaper_moduleadd_class")
        sleep(1)
        self.search_paper.click_button("paper", "editpaper_moduleadd_class32")
        self.search_paper.click_button("paper", "editpaper_moduleadd_add")
        sleep(1)
        self.search_paper.click_button("paper", "editpaper_moduleadd_X")
        self.search_paper.switch_page_close()

    # 复制试卷
    def copy_handout(self):
        self.search_paper.move_mouse("paper", "paper_menu")
        self.search_paper.click_button("paper", "paper_cope")
        sleep(1)
    # 删除试卷
    def delete_handout(self):
        # self.search_handout.move_top()
        # Handout.button_reset(self)
        # self.search_handout.input_string("自动测试讲义名1", "handout", "search_input")
        sleep(2)
        # Handout.button_search(self)
        # self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        self.search_paper.click_button("paper", "paper_delete")
        # try:
        #     self.search_handout.click_button("handout", "handout_delete")
        # except:
        #     print()
        sleep(1)
        self.search_paper.click_button("paper", "paper_delete_ok")

        # Handout.screen_search_input()
    # 属性
    def attribute_handout(self):
        self.search_paper.move_between()
        self.search_paper.click_button("paper", "paper_attribute")
        self.search_paper.click_button("paper", "paper_attribute_ok")

    # 编辑试卷
    def edit_paper(self):
        Search_paper.button_search(self)
        self.search_paper.click_button("paper", "editpaper_name")
        self.search_paper.switch_new_page()
        sleep(1)
        self.search_paper.click_button("paper", "editpaper_go")
        self.search_paper.click_button("paper", "editpaper_moduleadd_add")
        sleep(1)
        element = mongo.questionbasket()
        if element == "empty_questionbasket_haveyes":
            self.search_paper.click_button("paper", "edit_paper_use")
            sleep(1)
            self.search_paper.click_button("paper", "edit_paper_useyes")
        else:
            #  sleep(1)
            self.search_paper.click_button("paper", "edit_paper_popupadd")
            self.search_paper.switch_page_three()
            #  sleep(1)
            self.question = Search_Question.Search_Question(self.driver)
            self.question.join_questionbasket()
            self.search_paper.switch_page_close3_return2()
            sleep(1)
            self.search_paper = Get_Element.Search_Page_Elements(self.driver)
            self.search_paper.click_button("paper", "editpaper_moduleadd_X1")
            sleep(1)
            self.search_paper.click_button("paper", "editpaper_moduleadd_add")
            sleep(1)
            self.search_paper.click_button("paper", "edit_paper_use")
            sleep(1)
            self.search_paper.click_button("paper", "edit_paper_useyes")
            sleep(2)


    # 创建测验
    #学生版排版
    # def student_handout(self):
    #     sleep(2)
    #     self.search_handout.move_between()
    #     try:
    #         sleep(1)
    #         self.search_handout.move_mouse("handout", "move_mouse_handout_other1")
    #     except:
    #         self.search_handout.move_mouse("handout", "move_mouse_handout_other")
    #     self.search_handout.click_button("handout", "handout_student")
    #     self.search_handout.switch_new_page()
    #     sleep(3)
    #     self.search_handout.click_script("handout", "handout_student_points_addBlank")
    #     self.search_handout.click_script("handout", "handout_student_yes")
    #     self.search_handout.Refresh()
    #     self.search_handout = Get_Element.Search_Page_Elements(self.driver)
    #     sleep(3)
    #     state1 = self.search_handout.isElementExist("handout", "handout_student_points_Blank2")
    #     print(state1)
    #     self.search_handout.click_script("handout", "handout_student_points_deleteBlank")
    #     self.search_handout.click_script("handout", "handout_student_yes")
    #     self.search_handout.Refresh()
    #     self.search_handout = Get_Element.Search_Page_Elements(self.driver)
    #     sleep(3)
    #     state2 = self.search_handout.isElementExist("handout", "handout_student_points_Blank2")
    #     print(state2)
    #     # self.search_handout.input_string(5, "handout", "handout_student_points_input")
    #     # self.search_handout.enter_input("handout", "handout_student_points_input")
    #     # self.search_handout.click_script("handout", "handout_student_yes")
    #     # self.search_handout.Refresh()
    #     # self.search_handout = Get_Element.Search_Page_Elements(self.driver)
    #     # sleep(3)
    #     self.search_handout.move_between()
    #
    #     try:
    #         question_class = self.search_handout.get_page_element("handout", "handout_student_question2").get_attribute(
    #             'class')
    #     except:
    #         question_class = self.search_handout.get_page_element("handout",
    #                                                               "handout_student_question21").get_attribute('class')
    #     print(question_class)
    #     sleep(10)
    #     question_id = question_class.split('_')[2]
    #     element = '//*[@id="' + question_id + '_0"]'
    #
    #     # class_value1 = self.search_handout.get_page_element("handout", element).get_attribute('class')
    #     class_value1 = self.driver.find_element_by_xpath(element).get_attribute('class')
    #     print(class_value1)
    #     # self.search_handout.click_script("handout", element)
    #     elements = self.driver.find_element_by_xpath(element)
    #     self.driver.execute_script("arguments[0].click();", elements)
    #     self.search_handout.click_script("handout", "handout_student_yes")
    #     self.search_handout.Refresh()
    #     self.search_handout = Get_Element.Search_Page_Elements(self.driver)
    #     sleep(3)
    #     self.search_handout.move_between()
    #     # class_value2 = self.search_handout.get_page_element("handout", element).get_attribute('class')
    #     class_value2 = self.driver.find_element_by_xpath(element).get_attribute('class')
    #     print(class_value2)
    #     # self.search_handout.click_script("handout",element)
    #     elements = self.driver.find_element_by_xpath(element)
    #     self.driver.execute_script("arguments[0].click();", elements)
    #     self.search_handout.click_script("handout", "handout_student_yes")
    #     self.search_handout.Refresh()
    #     self.search_handout = Get_Element.Search_Page_Elements(self.driver)
    #     sleep(3)
    #     self.search_handout.move_between()
    #     # class_value3 = self.search_handout.get_page_element("handout", element).get_attribute('class')
    #     class_value3 = self.driver.find_element_by_xpath(element).get_attribute('class')
    #     print(class_value3)
    #     # self.search_handout.click_script("handout", element)
    #     elements = self.driver.find_element_by_xpath(element)
    #     self.driver.execute_script("arguments[0].click();", elements)
    #     self.search_handout.click_script("handout", "handout_student_yes")
    #     self.search_handout.Refresh()
    #     self.search_handout = Get_Element.Search_Page_Elements(self.driver)
    #     sleep(3)
    #     self.search_handout.move_between()
    #     # class_value4 = self.search_handout.get_page_element("handout", element).get_attribute('class')
    #     class_value4 = self.driver.find_element_by_xpath(element).get_attribute('class')
    #     print(class_value4)
    #     state = self.search_handout.get_page_element_name("handout", "handout_student_page")
    #     print(state == "第1页")
    #     self.search_handout.click_script("handout", "handout_student_page_hide")
    #     pagestate1 = self.search_handout.get_page_element_name("handout", "handout_student_page")
    #     print(pagestate1 == "")
    #     background = self.search_handout.get_page_element("handout", "handout_student_background").get_attribute(
    #         'style')
    #     print(background)
    #     self.search_handout.click_script("handout", "handout_student_template")
    #     self.search_handout.Refresh()
    #     self.search_handout = Get_Element.Search_Page_Elements(self.driver)
    #     sleep(3)
    #     background1 = self.search_handout.get_page_element("handout", "handout_student_background").get_attribute(
    #         'style')
    #     print(background1)
    #     # self.search_handout.cut("学生版排版-普通模板")
    #     self.search_handout.click_script("handout", "handout_student_odd_even")
    #     sleep(1)
    #     self.search_handout.click_script("handout", "handout_student_template_odd_even")
    #     self.search_handout.Refresh()
    #     self.search_handout = Get_Element.Search_Page_Elements(self.driver)
    #     sleep(3)
    #     background2 = self.search_handout.get_page_element("handout", "handout_student_background").get_attribute(
    #         'style')
    #     print(background2)
    #     self.search_handout.move_between()
    #     # self.search_handout.cut("学生版排版-奇偶模板")
    #     self.search_handout.switch_page_close()
    #     # true  false  true、col-xs-12  3  6  12、""
    #     dict = {'blank1': state1, 'blank2': state2, 'example_option1': class_value1, 'example_option2': class_value2,
    #             'example_option3': class_value3, 'example_option4': class_value4, 'page': pagestate1,
    #             'background': background, 'background1': background1, 'background2': background2}
    #     return dict
    #
    # #归档
    # def file_handout(self):
    #     sleep(2)
    #     Handout.screen_search_input(self)
    #     Handout.button_search(self)
    #     self.search_handout.move_between()
    #     self.search_handout.move_mouse("handout", "move_mouse_handout_other")
    #     self.search_handout.click_button("handout", "handout_file")
    #     sleep(1)
    #     self.search_handout.input_string("自动", "handout", "handout_file_input")
    #     self.search_handout.click_button("handout", "handout_file_search")
    #     sleep(1)
    #     self.search_handout.click_button("handout", "handout_file_file")
    #     sleep(1)
    #     try:
    #         self.search_handout.click_button("handout", "handout_file_file_yes")
    #     except Exception:
    #         print(1)
    #     sleep(1)
    #     self.search_handout.click_button("handout", "handout_file_file_file")
    #     sleep(2)
    #     handout_list = Handout.get_file_handout_attribute(self)
    #     lehandout_list = Handout.get_file_lehandout_attribute(self)
    #     sleep(1)
    #     self.search_handout.click_button("handout", "handout_file_file_file_yes")
    #     return {'handout_list':handout_list, 'lehandout_list':lehandout_list}
    #
    # def update_file_handout(self):
    #     Handout.screen_search_input(self)
    #     Handout.button_search(self)
    #     self.search_handout.move_between()
    #     self.search_handout.move_mouse("handout", "move_mouse_handout_other1")
    #     self.search_handout.click_button("handout", "handout_file")
    #     sleep(1)
    #     self.search_handout.click_button("handout", "handout_file_updatefile")
    #     sleep(1)
    #     try:
    #         self.search_handout.click_button("handout", "handout_file_updatefile_yes")
    #     except Exception:
    #         print(1)
    #     sleep(2)
    #
    # def delete_file_handout(self):
    #     Handout.screen_search_input(self)
    #     Handout.button_search(self)
    #     self.search_handout.move_between()
    #     self.search_handout.move_mouse("handout", "move_mouse_handout_other1")
    #     self.search_handout.click_button("handout", "handout_file")
    #     sleep(1)
    #     self.search_handout.click_button("handout", "handout_file_delete")
    #     state = self.search_handout.isElementExist("handout", "handout_file_file_file")
    #     print(state)
    #
    # def get_file_handout_attribute(self):
    #     self.handoutname = self.search_handout.get_page_element_name("handout", "file_verification_handout_name")
    #     self.classes = self.search_handout.get_page_element_name("handout", "file_verification_handout_classes")
    #     self.year = self.search_handout.get_page_element_name("handout", "file_verification_handout_year")
    #     self.type = self.search_handout.get_page_element_name("handout", "file_verification_handout_type")
    #     self.season = self.search_handout.get_page_element_name("handout", "file_verification_handout_season")
    #     self.school = self.search_handout.get_page_element_name("handout", "file_verification_handout_school")
    #     self.createman = self.search_handout.get_page_element_name("handout", "file_verification_handout_createman")
    #     self.list = [self.handoutname, self.classes, self.year, self.type, self.season, self.school, self.createman]
    #     return self.list
    #
    # def get_file_lehandout_attribute(self):
    #     self.handoutname = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_name")
    #     self.classes = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_classes")
    #     self.year = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_year")
    #     self.type = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_type")
    #     self.season = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_season")
    #     self.school = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_school")
    #     self.createman = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_createman")
    #     self.list = [self.handoutname, self.classes, self.year, self.type, self.season, self.school, self.createman]
    #     return self.list
    # #查看试卷
