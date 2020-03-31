import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_result_page import SearchResultPage
from pages.product_page import ProductPage
from pages.wish_list_page import WishListPage


class AmazonTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/User/Downloads/chromedriver')
        self.driver.get('https://www.amazon.com/')
        self.driver.maximize_window()

    def test_partner(self):
        HomePage(self.driver).visited_page()
        HomePage(self.driver).click_login_page()
        LoginPage(self.driver).login_amazon()
        HomePage(self.driver).search_keyword()
        SearchResultPage(self.driver).check_search_result_on_page()
        SearchResultPage(self.driver).go_second_page()
        SearchResultPage(self.driver).select_preferred_product(2)
        ProductPage(self.driver).add_to_wish_list()
        ProductPage(self.driver).open_wish_list_menu()
        WishListPage(self.driver).wish_list_product_confirm()
        WishListPage(self.driver).delete_from_wish_list()

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
