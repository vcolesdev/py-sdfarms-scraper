"""
--------------------------------------------------
Scraper Class
--------------------------------------------------

version: 1.0.0
author: Vanessa Coles
description: This class has methods that allow the user to navigate to the chosen URL and perform actions on the page.

--------------------------------------------------
"""

from selenium.webdriver.common.by import By


class Scraper:

    # Constructor
    # @param url: The URL to scrape data from
    # @param driver: The driver instance
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    """
    ---------------------------------------------
    Driver Methods
    ---------------------------------------------
    | open_driver_instance
    | quit_driver_instance
    | get_site_title_meta
    ---------------------------------------------
    """

    # Method to navigate to the chosen URL
    # @return: The driver instance
    def open_driver_instance(self):
        instance = self.driver
        print("Navigating to " + self.url + "...")
        return instance.get(self.url)

    # Method to quit an active driver instance
    def quit_driver_instance(self):
        instance = self.driver
        print("Quitting driver instance...")
        instance.quit()

    # Method to get the site title from the page
    def get_site_title_meta(self):
        instance = self.driver

        # Look for the title element
        title_element = instance.find_element(By.TAG_NAME, "title")

        # Check if the title element exists and return the inner text
        if title_element:
            inner_text = title_element.get_attribute("innerHTML")
            print("Title Inner Text: " + inner_text)
            return inner_text
        else:
            # Otherwise return the driver instance title
            print("Title: " + instance.title)
            return instance.title

    """
    ---------------------------------------------
    Element Methods
    ---------------------------------------------
    | get_element_by_id
    | get_elements_by_class_name
    | get_elements_by_tag_name
    ---------------------------------------------
    """

    # Method to get the list of elements by id
    def get_element_by_id(self, element_id):
        instance = self.driver

        # Locate an element by ID
        element_by_id = instance.find_elements(By.ID, element_id)

        # Check if the element ID exists and return None if not
        if element_id is None:
            print("The element with the specified ID does not exist.")
            return None
        else:
            # Return the list of elements
            print("Elements: " + element_by_id.__str__() + " found.")
            return element_by_id

    # Method to get the list of elements by class name
    def get_elements_by_class_name(self, class_name):
        instance = self.driver

        # Get the list of elements by class name
        elements_by_class_name = instance.find_elements(By.CLASS_NAME, class_name)

        # Check if the element class name exists and return None if not
        if class_name is None:
            print("The element with the specified class name does not exist.")
            return None
        else:
            # Return the list of elements
            print("Elements: " + elements_by_class_name.__str__() + " found.")
            return elements_by_class_name

    # Method to get the list of elements by tag name
    def get_elements_by_tag_name(self, tag_name):
        instance = self.driver

        # Get the list of elements by tag name and convert to a list
        elements_by_tag_name = instance.find_elements(By.TAG_NAME, tag_name)
        elements_list = list(elements_by_tag_name)

        # Check if the element tag name exists and return None if not
        if tag_name is None:
            print("The element with the specified tag name does not exist.")
            return None
        else:
            # Return the list of elements
            print("Elements: " + "\n" + elements_list.__str__() + " found.")
            return elements_by_tag_name

    """
    ----------------------------------------------
    Action Methods
    ---------------------------------------------
    | click_element
    | click_elements
    ---------------------------------------------
    """

    # Click on a single element on the page
    @staticmethod
    def click_element(element):
        if element is not None:
            element.click()

    # Click on multiple elements specified by class name
    def click_elements(self, class_name):
        elements = self.get_elements_by_class_name(class_name)
        for element in elements:
            element.click()
