"""
markets_data.py
This module contains functions that are used to get data from the markets.

Functions:
|    get_market_location(market)
|    get_market_details(market)
|    get_market_name(market)
|    get_market_hours_of_operation(market_details_list)
|    get_market_address(market_details_list)
|    get_market_manager_name(market_details_list)
|    get_market_manager_email(market_details_list)
|    get_market_manager_phone(market_details_list)
|    get_market_website(market_details_list)
|    check_market_accepts_ebt(market)
|    check_market_accepts_wic(market)
"""

from selenium.webdriver.common.by import By
from ..utils import *


# get_market_location(market)
# Get the market location from the toggle content
def get_market_location(market):
    location_str = market.text
    remove_whitespace(location_str)
    return location_str


# get_market_details(market)
# Get the market details from the toggle content
def get_market_details(market):

    # Select the next immediate sibling element to the current element
    market_details = market.find_element(By.XPATH, "following-sibling::*")
    return market_details


# get_market_name(market)
# Get the market name from the toggle content
def get_market_name(market):
    details = get_market_details(market)

    # Get the first element in the list
    market_name = details.text.split("\n")[0]

    remove_whitespace(market_name)
    return market_name


# get_market_hours_of_operation(market_details_list)
# Get hours of operation from the toggle content
def get_market_hours_of_operation(market_details_list):
    details = market_details_list

    # Find the element that contains the string "Manager: "
    # and get its index in the list
    manager_element = find_string_in_element("Manager:", details)
    manager_element_index = details.index(manager_element)

    # Get the preceding index of the manager element,
    # which is the hours of operation
    hours_element_index = manager_element_index - 1
    hours_element = details[hours_element_index]

    # Convert the hours element to a string
    hours_element_str = convert_to_string(hours_element)

    remove_whitespace(hours_element_str)
    return hours_element_str


# get_market_address(market_details_list)
# Get the market address line 1 from the toggle content
def get_market_address(market_details_list):
    details = market_details_list

    # Find the element that contains the string "Location:"
    address = find_string_in_element("Location:", details)

    # Convert the address to a string
    # Remove the "Location: " text from the string
    address_str = convert_to_string(address)
    address_str = address_str.split("Location: ")[1] if "Location: " in address_str else address_str

    # Return the first address line
    remove_whitespace(address_str)
    return address_str


# get_market_manager_name(market_details_list)
# Get the market manager name from the toggle content
def get_market_manager_name(market_details_list):
    details = market_details_list

    # Find the element that contains the string "Manager:"
    # Return the text after the colon
    manager_element = find_string_in_element("Manager:", details)
    manager = manager_element.split(":")[1]

    manager = remove_whitespace(manager)
    return manager


# get_market_manager_email(market_details_list)
# Get the market manager's email address from the toggle content
def get_market_manager_email(market_details_list):
    details = market_details_list

    # Find the element that contains the string "Email:"
    email_element = find_string_in_element("Email:", details)

    # Convert the email address to a string
    email = convert_to_string(email_element)

    # Return the text after the colon
    email = email.split(": ")[1] if ": " in email else email

    email = remove_whitespace(email)
    return email


# get_market_manager_phone(market_details_list)
# Get the market manager's phone number from the toggle content
def get_market_manager_phone(market_details_list):
    details = market_details_list

    # Find the element that contains the string "Phone:"
    phone_element = find_string_in_element("Phone:", details)

    # Convert the phone number to a string
    phone = convert_to_string(phone_element)

    # Remove the "Phone: " text from the string
    phone = phone.split("Phone: ")[1] if "Phone: " in phone else phone

    phone = remove_whitespace(phone)
    return phone


# get_market_website(market_details_list)
# Get the market website from the toggle content
def get_market_website(market_details_list):
    details = market_details_list

    # Find the element that contains the string "Website:"
    website_element = find_string_in_element("Website:", details)

    # Convert the website to a string
    website = convert_to_string(website_element)

    # Remove the "Website: " text from the string
    website = website.split("Website: ")[1] if "Website: " in website else website

    website = remove_whitespace(website)
    return website


# check_market_accepts_ebt(market)
# Check if the market accepts EBT
def check_market_accepts_ebt(market):
    details = get_market_details(market)
    if "EBT" in details.text:
        return True
    else:
        return False


# check_market_accepts_wic(market)
# Check if the market accepts WIC
def check_market_accepts_wic(market):
    details = get_market_details(market)
    if "WIC" in details.text:
        return True
    else:
        return False


# check_market_accepts_ebt_or_wic(market)
# Check if the market accepts EBT or WIC
def check_market_accepts_ebt_or_wic(market):
    accepts_ebt = check_market_accepts_ebt(market)
    accepts_wic = check_market_accepts_wic(market)

    if accepts_ebt or accepts_wic:
        return True
    else:
        return False
