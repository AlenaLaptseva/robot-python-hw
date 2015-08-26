__author__ = 'Alena_Laptseva'

from Selenium2Library import Selenium2Library



class UIUserLib(Selenium2Library):

    locators={
        "login button locator":"xpath=//button[@type='submit']",
        "message":"xpath=//div/font[text()='Incorrect login or password.']",
        "user name text locator":"xpath=//*[@id='j_username']",
        "password name text locator":"xpath=//*[@name='j_password']",
        "login button locator":"xpath=//button[@type='submit']",
        "user options locator":"xpath=//div[@id='GButtonUserMenu']"
    }
    def __init__(self):
        super(UIUserLib,self).__init__(run_on_failure="Nothing")

    def open_login_page(self,loginUrl,browser):
        self.open_browser(loginUrl,browser)
        self.maximize_browser_window()
        self.page_should_contain_element(UIUserLib.locators['login button locator'])


    def enter_login_and_password(self,login,password):
        self.input_text(UIUserLib.locators['user name text locator'],login)
        self.input_text(UIUserLib.locators['password name text locator'],password)
        self.click_button(UIUserLib.locators['login button locator'])
        self.set_selenium_implicit_wait(10)

