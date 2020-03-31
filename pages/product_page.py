from base.base_functions import Base
from selenium.webdriver.common.by import By


class ProductPage(Base):
    PRODUCT_NAME = (By.ID, 'productTitle')
    ADD_TO_WISH_LIST = (By.ID, 'add-to-wishlist-button-submit')
    WAIT_FOR_PRODUCT = (By.CLASS_NAME, "w-action-button")
    CLOSE_WISH_LIST = (By.CLASS_NAME, 'w-button-text')
    WISH_LIST_NAVIGATOR = (By.ID, "nav-link-accountList")
    WISH_LIST_CLICK = (By.LINK_TEXT, "Wish List")
    PRODUCT_TEXT = ''
    WISH_LIST_URL = 'https://www.amazon.com/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance'

    def add_to_wish_list(self):
        """
        Adds product to wish list and checks the page url according to page performs the action

        """
        self.PRODUCT_TEXT = self.wait_element_visible(self.PRODUCT_NAME).text
        self.wait_element_click(self.ADD_TO_WISH_LIST).click()
        if self.get_url() == self.WISH_LIST_URL:
            pass
        else:
            self.wait_element_click(self.WAIT_FOR_PRODUCT)
            self.wait_element_click(self.CLOSE_WISH_LIST).click()

    def open_wish_list_menu(self):
        """
        Opens the wish list menu to reach wish list page.

        """
        self.hover(self.WISH_LIST_NAVIGATOR)
        self.wait_element_click(self.WISH_LIST_CLICK).click()
