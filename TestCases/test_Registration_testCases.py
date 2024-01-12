import time
import pytest
from PageObjectModel.POM import credkart_POM
from utilities.readproperties import Readconfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_user_registration():

    get_user_name = Readconfig.get_User_Name()
    get_user_email = Readconfig.get_User_Email()
    get_user_passwd = Readconfig.get_User_Password()

    # def __init__(self):
    #     self.wait = WebDriverWait(self.driver, 10)

    @pytest.mark.regression
    def test_registrations_Of_User(self, setup):
        self.driver = setup
        self.regi_att = credkart_POM(self.driver)
        self.regi_att.click_register_option()
        self.regi_att.enter_Registration_name(self.get_user_name)
        self.regi_att.enter_Registration_email(self.get_user_email)
        self.regi_att.enter_Registration_passwd(self.get_user_passwd)
        self.regi_att.confirm_passwd(self.get_user_passwd)
        self.regi_att.click_register_button()
        time.sleep(5)

        self.driver.close()

    @pytest.mark.regression
    def test_login_of_user(self, setup):
        self.driver = setup
        self.regi_att = credkart_POM(self.driver)
        self.regi_att.click_login_option()
        self.regi_att.enter_Login_email(self.get_user_email)
        self.regi_att.enter_Login_passwd(self.get_user_passwd)
        self.regi_att.select_remember_me_check_box()
        self.regi_att.click_Login_button()
        time.sleep(5)

        # verify if you are landed on the correct Page:

        exp_page_Title = "CredKart"
        actual_page_Title = self.driver.title
        if exp_page_Title == actual_page_Title:
            print(
                f"The expected title '{exp_page_Title}' is same as actual title '{actual_page_Title}'.\nThank You for Logging in.")
        else:
            print("Title does not match.")

        self.driver.close()

    def test_Login_using_params(self, setup, getDataForLogin):
        self.driver = setup
        self.regi_att = credkart_POM(self.driver)
        self.regi_att.click_login_option()

        self.regi_att.enter_Login_email(getDataForLogin[0])
        print('Email : ' + getDataForLogin[0])

        self.regi_att.enter_Login_passwd(getDataForLogin[1])
        print('Password : ' + getDataForLogin[1])

        self.regi_att.click_Login_button()

        if self.regi_att.validate_credkart_text() == 'Registration or Login pass':
            if getDataForLogin[2] == 'pass':
                print('Correct Login Credentials. We are inside, Proof : '+self.regi_att.validate_credkart_text())
                assert True

            elif getDataForLogin[2] == 'fail':
                print('Incorrect Login Credentials.')
                assert False

        else:
            if getDataForLogin[2] == 'pass':
                print('Incorrect Login Credentials.')
                assert False

            elif getDataForLogin[2] == 'fail':
                print('Incorrect Login Credentials.')
                assert True
