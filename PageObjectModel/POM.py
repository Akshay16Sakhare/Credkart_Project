from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.ie.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class credkart_POM():
    register_button_selector = (By.XPATH, "//a[normalize-space()='Register']")
    registration_name_selector = (By.ID, "name")
    registration_email_selector = (By.ID, "email")
    registration_Passwd_selector = (By.ID, "password")
    registration_Confirm_Passwd_selector = (By.ID, "password-confirm")
    registration_Register_button_selector = (By.XPATH, "//button[@type='submit']")

    login_button_selector = (By.XPATH, "//a[normalize-space()='Login']")
    login_email_selector = (By.ID, "email")
    login_Passwd_selector = (By.ID, "password")
    login_Remember_me_selector = (By.XPATH, "//input[@name='remember']")
    login_Submit_selector = (By.XPATH, "//button[@type='submit']")

    credkart_text_xpath = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

#Registration:
    def click_register_option(self):
        self.driver.find_element(*self.register_button_selector).click()

    def enter_Registration_name(self, Name):
        self.wait.until(EC.presence_of_element_located((self.registration_name_selector))).send_keys(Name)

    def enter_Registration_email(self, Email):
        self.driver.find_element(*self.registration_email_selector).send_keys(Email)

    def enter_Registration_passwd(self, Password):
        self.driver.find_element(*self.registration_Passwd_selector).send_keys(Password)

    def confirm_passwd(self, Password):
        self.driver.find_element(*self.registration_Confirm_Passwd_selector).send_keys(Password)

    def click_register_button(self):
        self.driver.find_element(*self.registration_Register_button_selector)



#Login:
    def click_login_option(self):
        # self.driver.find_element(*self.login_button_selector).click()
        self.wait.until(EC.presence_of_element_located((self.login_button_selector))).click()

    def enter_Login_email(self, Email):
        self.wait.until(EC.presence_of_element_located((self.login_email_selector))).send_keys(Email)

    def enter_Login_passwd(self, Password):
        # self.driver.find_element(*self.login_Passwd_selector).send_keys(Password)
        self.wait.until(EC.presence_of_element_located((self.login_Passwd_selector))).send_keys(Password)

    def select_remember_me_check_box(self):
        # self.driver.find_element(*self.login_Remember_me_selector).click()
        self.wait.until(EC.presence_of_element_located((self.login_Remember_me_selector))).click()

    def click_Login_button(self):
        # self.driver.find_element(*self.login_Submit_selector).click()
        self.wait.until(EC.presence_of_element_located((self.login_Submit_selector))).click()

    def validate_credkart_text(self):
        try:
            self.wait.until(EC.presence_of_element_located((self.credkart_text_xpath)))
            print(self.wait.until(EC.presence_of_element_located((self.credkart_text_xpath))).text)
            print('Registration or Login pass')
            return 'Registration or Login pass'
        except:
            print('Registration or Login fail')
            return 'Registration or Login fail'

