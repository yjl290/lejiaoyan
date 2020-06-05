from time import sleep

from Util import Get_Element


class Edit_Paper():

    def __init__(self, driver):
        self.driver = driver

    def menu(self):
        self.edit_paper = Get_Element.Search_Page_Elements(self.driver)
        self.edit_paper.click_button("paper", "editpaper_openmenu")
        sleep(1)
        self.edit_paper.doubleclick_button("paper", "editpaper_modelgrade")
        self.edit_paper.input_string("10", "paper", "editpaper_modelgrade_input")
        self.edit_paper.enter_input("paper", "editpaper_modelgrade_input")
        self.edit_paper.click_button("paper", "editpaper_questiongopen")
        sleep(1)
        self.edit_paper.doubleclick_button("paper", "editpaper_questiongrade")
        self.edit_paper.input_string("20", "paper", "editpaper_questiongrade_input")
        self.edit_paper.enter_input("paper", "editpaper_questiongrade_input")