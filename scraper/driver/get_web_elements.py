"""
markets_elements.py
This module contains functions that are used to get elements from the markets.

Functions:
|    get_market_elements_from_column(current_column, class_name="dt-sc-toggle")
|    get_toggle_elements_by_classname(scraper_instance, class_name="dt-sc-toggle")
|    get_toggle_columns_by_classname(scraper_instance, class_name="dt-sc-toggle-frame-set")
"""

import sys
from selenium.webdriver.common.by import By


# Get the market elements from each column
# These market elements represent each individual farmers market
def get_market_elements_from_column(current_column, class_name="dt-sc-toggle"):
    markets_list = current_column.find_elements(By.CLASS_NAME, class_name)
    if len(markets_list) > 0:
        return markets_list
    return markets_list


# Get the list of toggle elements from the page
# These toggle elements represent each individual farmers market
def get_toggle_elements_by_classname(scraper_instance, class_name="dt-sc-toggle"):
    toggle_class_name = class_name
    elems = scraper_instance.get_elements_by_class_name(toggle_class_name)

    if scraper_instance:
        return elems
    else:
        print("No driver instance found. Exiting...")
        sys.exit(1)


# Get the list of toggle columns from the page
# These toggle columns represent each day of the week
def get_toggle_columns_by_classname(scraper_instance, class_name="dt-sc-toggle-frame-set"):
    toggle_cols_classname = class_name
    elems = scraper_instance.get_elements_by_class_name(toggle_cols_classname)

    if scraper_instance:
        return elems
    else:
        print("No driver instance found. Exiting...")
        sys.exit(1)


# Get the list of toggle elements.  This can be used to get the number
# of markets in each column - corresponding with the days of the week
def get_toggle_elements_list(scraper):
    toggle_elements_list = []
    toggle_elements = get_toggle_elements_by_classname(scraper_instance=scraper)

    # Populate the toggle elements list
    for i in toggle_elements:
        toggle_elements_list.append(i)

    # Return the list of toggle elements
    return toggle_elements_list


# Get the list of toggle columns.  Each column corresponds with a day of the week.
def get_toggle_columns_list(scraper):
    toggle_columns_list = []
    toggle_column_elements = get_toggle_columns_by_classname(scraper_instance=scraper)

    # Populate the toggle columns list
    for i in toggle_column_elements:
        toggle_columns_list.append(i)

    # Return the list of toggle columns
    return toggle_columns_list
