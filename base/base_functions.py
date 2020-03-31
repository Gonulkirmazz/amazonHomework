from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def wait_element_click(self, element):
        """
        Waits until the element become clickable

        """
        return self.wait.until(ec.element_to_be_clickable(element))

    def wait_element_visible(self, element):
        """
        Waits until the element become visible on page

        """
        return self.wait.until(ec.visibility_of_element_located(element))

    def hover(self, element):
        """
        Hover to element and do the actions while menu is open

        """
        hover_element = self.wait_element_click(element)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()

    def send_input(self, selector, value):
        """
        Enters input to given element

        """
        self.wait.until(ec.presence_of_element_located(selector)).send_keys(value)

    def get_url(self):
        """
        Gets the URL of current page

        """
        self.driver.current_url
