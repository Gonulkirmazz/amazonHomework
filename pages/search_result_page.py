from base.base_functions import Base
from selenium.webdriver.common.by import By


class SearchResultPage(Base):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    CONFIRM_SEARCHED_TEXT = (By.CLASS_NAME, 'a-color-state')
    NEXT_PAGE = (By.CLASS_NAME, 'a-normal')
    CURRENT_PAGE = (By.CLASS_NAME, 'a-selected')

    def check_search_result_on_page(self):
        """
        Checks a specific element to confirm search result is displayed.

        """
        search_field_text = self.wait_element_visible(self.SEARCH_FIELD).text
        search_result_text = self.wait_element_visible(self.CONFIRM_SEARCHED_TEXT).text
        assert search_field_text in search_result_text
        print('Samsung search confirmed')

    def go_second_page(self):
        """
        Click to second page

        """

        self.wait_element_click(self.NEXT_PAGE).click()
        page_number = self.wait_element_visible(self.CURRENT_PAGE).text
        assert "2" in page_number
        print('Page 2 display confirmed')

    def select_preferred_product(self, preferred_product_order):
        """
        Clicks to 3rd product on current page

        """
        self.wait_element_click((By.CSS_SELECTOR, "div[data-index='{}'] .a-size-medium"
                                 .format(preferred_product_order))).click()
