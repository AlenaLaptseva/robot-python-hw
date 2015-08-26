__author__ = 'Alena_Laptseva'

from UIUserLib import UIUserLib


class UserLib(UIUserLib):


    def Login(self,loginUrl,browser,login,password):
        self.open_login_page(loginUrl,browser)
        self.enter_login_and_password(login,password)



    def verify_if_the_user_logged(self):
        if self.page_should_contain_element(UIUserLib.locators['user options locator'],"User is not logged")==None:
            return "User is successfully logged"

    def verify_if_the_message_present(self):
        if self.page_should_contain_element(UIUserLib.locators['message'],"Message 'Incorrect login or password' does not exist")==None:
            return(self.get_text(UIUserLib.locators['message']))

if __name__ == '__main__':
   j = UserLib()
   j.Login('http://blackbox28.clarabridge.net:80/cmp/login','firefox','admin','admin')
   c=j.check_the_message()
   print(c)