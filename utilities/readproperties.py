import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Admin\PycharmProjects\CredKart_Project\Configuration\config.ini")

class Readconfig():

    @staticmethod
    def get_User_Name():
        Name = config.get('user info', 'user_name')
        return Name

    @staticmethod
    def get_User_Email():
        Email = config.get('user info', 'emailId')
        return Email

    @staticmethod
    def get_User_Password():
        Password = config.get('user info', 'password')
        return Password

    @staticmethod
    def get_URL():
        URL = config.get('user info', 'URL')
        return URL