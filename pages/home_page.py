from base.base_functions import Base
from selenium.webdriver.common.by import By


class HomePage(Base):
    SEARCH_TEXT = "Samsung"
    AMAZON_PAGE_CONFIRM = (By.CLASS_NAME, 'nav-logo-link')
    LOGIN_PAGE_CLICK = (By.ID, 'nav-link-accountList')
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.CLASS_NAME, 'nav-input')

    def visited_page(self):
        """
        Check a specific element to confirm we are on amazon web site.

        """
        self.wait_element_visible(self.AMAZON_PAGE_CONFIRM)
        print('You are on Amazon Website')

    def click_login_page(self):
        """
        Clicks login element.

        """
        self.wait_element_click(self.LOGIN_PAGE_CLICK).click()

    def search_keyword(self, search_text):
        """
        Enters a text to search field and press to search button
        :param str search_text: a string text to use as a search request
        
        """
        self.send_input(self.SEARCH_FIELD, search_text)
        self.wait_element_click(self.SEARCH_BUTTON).click()
