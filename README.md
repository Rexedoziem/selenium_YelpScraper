# selenium_YelpScraper
An automation of YelpScraper using selenium

# Yelp Scraper

This script scrapes information about bars in various cities from Yelp.com using the Python package Selenium. It then saves the information to a CSV file.
# Requirements

    Python 3.x
    Selenium
    pandas
    tqdm
    
# Installation

    Install Python 3.x from the official website.
    Install the required packages by running pip install -r requirements.txt in the command line.

# Usage

To use the script, simply run python yelp_scraper.py in the command line. The script will then prompt you to enter a city to search for bars in.

The script will then use Selenium to navigate to Yelp.com and search for bars in the given city. It will scrape the following information for each bar:

    Image
    Restaurant name
    Address
    Contact address
    Reviews
    Dish name
    Timing
    Ratings
    Restaurant URL
    Restaurant ownership

The information will be saved to a CSV file named <city>.csv.

Note that the script may take a while to run, especially if there are many bars in the city being searched.
# Contributing

If you would like to contribute to this project, please submit a pull request with your changes.
# License

This project is licensed under the MIT License. See the LICENSE file for more information.
