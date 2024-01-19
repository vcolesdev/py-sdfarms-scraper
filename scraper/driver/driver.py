"""
driver.py
This module contains the driver instance for the scraper.

Functions:
|    get_driver_instance(options)
|    instance_wrapper(extra_options=None)
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


# Static method for retrieving a Firefox driver instance
def get_driver_instance(options: Options):
    driver = Firefox(options=options)
    return driver


# Create a Scraper instance
def instance_wrapper(extra_options: Options = None):

    # Set driver options
    set_driver_options = Options()
    set_driver_options.headless = True

    # Set extra options here:
    if extra_options:
        set_driver_options = extra_options

    # Get driver instance and pass the driver options
    instance = get_driver_instance(set_driver_options)

    # Return the driver instance
    return instance
