from base.base_functions import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    USER_MAIL_FIELD = (By.ID, 'ap_email')
    CONTINUE_BUTTON = (By.ID, 'continue')
    USER_PASSWORD_FIELD = (By.ID, 'ap_password')
    SUBMIT_BUTTON = (By.ID, 'signInSubmit')

    def login_amazon(self, user_mail, user_password):
        """
        Enters login information to fields
        :param str user_mail: Users mail information to enter email field
        :param str user_password: Users password information to enter password field

        """
        self.send_input(self.USER_MAIL_FIELD, user_mail)
        self.wait_element_click(self.CONTINUE_BUTTON).click()
        self.send_input(self.USER_PASSWORD_FIELD, user_password)
        self.wait_element_click(self.SUBMIT_BUTTON).click()
