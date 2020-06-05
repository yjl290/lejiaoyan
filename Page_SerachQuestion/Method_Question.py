from selenium.common.exceptions import ElementNotInteractableException

from Util import Get_Element
from Page_SerachQuestion import Search_Question
from Util import MongoDB_Data
from time import sleep
mongo = MongoDB_Data.Mongo_Data()


class Method_AddQuestion():

    def __init__(self, driver):
        self.driver = driver

    # 试题篮加题
    def new_omegaPaper_add(self, model, elm1, elm2, elm3, elm4, elm5):
        self.add_question = Get_Element.Search_Page_Elements(self.driver)
        element = mongo.questionbasket()
        if element == "empty_questionbasket_haveyes":
            sleep(1)
            self.add_question.click_button(model, elm1)
            self.add_question.click_button(model, elm2)
            sleep(1)
        else:
            sleep(1)
            self.add_question.click_button(model, elm3)
            self.add_question.switch_page_three()
            self.question = Search_Question.Search_Question(self.driver)
            self.question.join_questionbasket()
            self.add_question.switch_page_close3_return2()
            sleep(2)
            # self.driver.find_element_by_css_selector(
            #     ".ant-modal-close-x").click()
            self.add_question = Get_Element.Search_Page_Elements(self.driver)

            try:
                self.add_question.click_button(model, elm4)
            except:
                self.add_question.click_button(model, "new_edit_handout_addexample_subject_popupclose2")
                print("关闭成功")
            self.add_question.click_button(model, elm5)
            sleep(1)
            self.add_question.click_button(model, elm1)
            self.add_question.click_button(model, elm2)