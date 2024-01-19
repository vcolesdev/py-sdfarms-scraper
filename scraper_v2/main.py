from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.sdfarms.markets_page import FarmsPage


def main():
    print("Hello from main()!  Running driver instance...")

    # Create a new instance of the Chrome driver
    ff_driver = webdriver.Firefox()
    markets_page = FarmsPage(ff_driver)

    # Open the page
    markets_page.open_page(markets_page.url)

    # Get the page title
    page_title = markets_page.get_page_title()
    print("Page Title: " + page_title)

    # Get the toggle elements representing each farmers market
    toggle_elements = markets_page.get_toggle_elements()
    print("There are " + str(len(toggle_elements)) + " markets.")

    # Expand each toggle element by clicking on it
    for i in toggle_elements:
        markets_page.click_expand_toggle_content(i)


if __name__ == '__main__':
    print("Hello from SD Farms Scraper v2!")

    main()
