from base.base_functions import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    USER_MAIL = 'gorkem@getnada.com'
    USER_PASSWORD = '123gm123'
    USER_MAIL_FIELD = (By.ID, 'ap_email')
    CONTINUE_BUTTON = (By.ID, 'continue')
    USER_PASSWORD_FIELD = (By.ID, 'ap_password')
    SUBMIT_BUTTON = (By.ID, 'signInSubmit')

    def login_amazon(self):
        """
        Enters login information to fields

        """
        self.send_input(self.USER_MAIL_FIELD, self.USER_MAIL)
        self.wait_element_click(self.CONTINUE_BUTTON).click()
        self.send_input(self.USER_PASSWORD_FIELD, self.USER_PASSWORD)
        self.wait_element_click(self.SUBMIT_BUTTON).click()
