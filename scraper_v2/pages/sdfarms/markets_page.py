from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.relative_locator import locate_with


class FarmsPage:

    def __init__(self, driver):
        self.url = "https://www.sdfarmbureau.org/farmers-market/"
        self.driver = driver

        # Toggle elements represent each individual farmers market
        self.toggle_elements = self.driver.find_elements(By.CLASS_NAME, "dt-sc-toggle")
        self.one_fourth_cols = self.driver.find_elements(By.CLASS_NAME, "dt-sc-one-fourth")

    def open_page(self, url):
        """
        Method to navigate to the chosen URL
        :param url:
        :return:
        """
        print("Navigating to " + url + "...")
        return self.driver.get(url)

    def get_page_title(self):
        """
        Method to get the page title
        :return:
        """
        return self.driver.title

    def get_toggle_elements(self, class_name="dt-sc-toggle"):
        """
        Method to get the clickable toggle elements from the page
        :param class_name:
        :return:
        """
        elems = self.driver.find_elements(By.CLASS_NAME, class_name)
        return elems

    def get_one_fourth_cols(self, class_name="dt-sc-toggle-frame-set"):
        """
        Method to get all the one-fourth columns from the page
        :param class_name:
        :return:
        """
        elems = self.driver.find_elements(By.CLASS_NAME, class_name)
        return elems

    @staticmethod
    def click_expand_toggle_content(toggle_element):
        toggle_element.click()

    def get_toggle_elements_content(self):
        elements_list = []
        toggle_elements_content = self.driver.find_elements(
            By.XPATH,
            "//div[@class='dt-sc-toggle-content']/div[@class='block']/child::text()"
        )
        for i in toggle_elements_content:
            elements_list.append(i)

        return elements_list
