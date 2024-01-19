import os

from scraper.classes.Scraper import *

from scraper.driver.driver import *
from scraper.driver.get_web_elements import *
from scraper.driver.get_markets_data import *

# Load env variables
from dotenv import load_dotenv
load_dotenv("../.env")

# Empty markets list
markets_list = []

# URL to navigate to, load from env
get_markets_url = os.getenv("MARKETS_URL")

# Days of the week, convert to a list
days_of_the_week_list = ["mon", "tues", "wed", "thu", "fri", "sat", "sun"]

# Create new scraper instance
instance = instance_wrapper()


# Market data keys
market_data_keys = [
    "key",
    "full_name",
    "address",
    "hours_of_operation",
    "manager_name",
    "manager_phone",
    "manager_email",
    "website",
    "accepts_ebt",
    "accepts_wic",
]


# Main function
if __name__ == '__main__':

    def main():

        # Check if there is a valid instance, if not, exit the program
        if instance is None:
            print("No driver instance found. Exiting...")
            sys.exit(1)

        # Instantiate a Scraper class and pass the URL and driver instance
        scraper = Scraper(url=get_markets_url, driver=instance)
        scraper.open_driver_instance()

        # Get the title of the page
        title = scraper.get_site_title_meta()

        # Expand all toggle elements
        scraper.click_elements("dt-sc-toggle")

        # List of markets to use later
        list_of_markets = []

        # Get the list of markets from toggle elements
        markets_list = get_toggle_elements_list(scraper)

        # Get an indexed list of the days of the week from toggle columns
        days_of_the_week = get_toggle_columns_list(scraper)

        # Get the number of markets in each column
        num_of_markets = len(markets_list)

        # Loop through the list of toggle columns
        for i in days_of_the_week:

            # Get the list of markets for the current day (i)
            current_day_markets_list = get_market_elements_from_column(i)

            # Get the number of markets for the current day (i)
            num_of_markets = len(current_day_markets_list)

            # Get the day of the week based on index
            day_of_week = days_of_the_week_list[days_of_the_week.index(i)]

            # Print the number of markets for each day of the week
            # Print a list of the current day's markets
            print(day_of_week + ": " + num_of_markets.__str__())
            insert_newline()

            # Loop through each market in the current day's markets list
            for m in current_day_markets_list:

                # Assign a unique ID to each market according to the day of the week
                market_key = day_of_week + "_" + m.text[0:3]

                # Get the market details text and split into a list and print it
                market_details = get_market_details(m)
                market_details_list = market_details.text.split("\n")

                # Create an empty dictionary to store the market data
                market_data = {}

                # Populate the market data dictionary with the market keys
                for key in market_data_keys:
                    market_data[key] = ""

                # TODO: Refactor this code to use a function, can trim down

                # Get market data
                markey_key = market_key
                market_name = get_market_name(m)
                market_address = get_market_address(market_details_list)
                market_hours_of_operation = get_market_hours_of_operation(market_details_list)
                market_manager_name = get_market_manager_name(market_details_list)
                market_manager_phone = get_market_manager_phone(market_details_list)
                market_manager_email = get_market_manager_email(market_details_list)
                market_website = get_market_website(market_details_list)
                market_accepts_ebt = check_market_accepts_ebt(m)
                market_accepts_wic = check_market_accepts_wic(m)

                # TODO: Refactor function parameters, can organize keys in list and pass to function
                # Create the market data dictionary
                def create_market_data(
                        data,
                        unique_key,
                        full_name,
                        address,
                        hours_of_operation,
                        manager_name,
                        manager_phone,
                        manager_email,
                        website,
                        accepts_ebt,
                        accepts_wic
                ):

                    # Add keys to the market data dictionary
                    data["key"] = unique_key
                    data["full_name"] = full_name
                    data["address"] = address
                    data["hours_of_operation"] = hours_of_operation
                    data["manager_name"] = manager_name
                    data["manager_phone"] = manager_phone
                    data["manager_email"] = manager_email
                    data["website"] = website
                    data["accepts_ebt"] = accepts_ebt
                    data["accepts_wic"] = accepts_wic

                    # Return the market data dictionary
                    return data

                # Populate the market data dictionary with the market data
                market_data_keys_data = create_market_data(
                    market_data,
                    market_key,
                    market_name,
                    market_address,
                    market_hours_of_operation,
                    market_manager_name,
                    market_manager_phone,
                    market_manager_email,
                    market_website,
                    market_accepts_ebt,
                    market_accepts_wic
                )

                market = market_data_keys_data

                # Print the market data dictionary
                list_of_markets.append(market)

        # Create a constant for the market data
        markets_list_populated = list_of_markets

        # Convert our markets list to JSON data
        markets_json_data = convert_to_json(markets_list_populated)

        # Print the JSON data
        print(markets_json_data)

        # Output to file
        print_content_to_file("data/markets.json", markets_json_data)

        # Close the driver instance
        scraper.quit_driver_instance()

        # Print a message to the console
        print("Driver instance closed successfully.")
        print("You can find the data in the data/markets.json file.")
        print("Thank you for using the SD Farms Scraper App!")

    # Run the main function
    main()
