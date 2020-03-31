from base.base_functions import Base
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage


class WishListPage(Base):
    WISH_LIST_PRODUCT = (By.CSS_SELECTOR, "h3 .a-link-normal")
    DELETE_FROM_WISH_LIST = (By.LINK_TEXT, "Delete item")
    DELETE_CONFIRM = (By.CSS_SELECTOR, ".a-alert-inline-success div")

    def wish_list_product_confirm(self):
        """
        Confirms that product which is added on previous page in on the wish list

        """
        product_confirm = self.wait_element_visible(self.WISH_LIST_PRODUCT).text
        confirm = ProductPage.PRODUCT_TEXT
        assert confirm in product_confirm
        print("Product is in Wish List")

    def delete_from_wish_list(self):
        """
        Deletes the product which is added and  confirm it is deleted

        """
        self.wait_element_click(self.DELETE_FROM_WISH_LIST).click()
        delete_confirm = self.wait_element_visible(self.DELETE_CONFIRM).is_displayed()
        assert delete_confirm, True
        print('Product deleted from wish list')
