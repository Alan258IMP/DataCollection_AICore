# ComputerVisionPro_AICore

This Python project is an implementation of an industrial-grade data collection pipeline, which automatically browse a website and collect information from it.

This project requires [Selenium](https://github.com/SeleniumHQ/selenium/tree/trunk/py) and [Pandas](https://github.com/pandas-dev/pandas) modules.

## Milestone 1 ~ 3: Prototyping the web scraper

The website I am going to scrape is [VNDB](https://vndb.org/), a visual novel wiki, because it is a website that does not change its layout very often. We aim to collect the data from top-rated visual novels with a certain keyword or genre.

We created a general-purpose basic scraper class with Selenium, with basic functionalities including clicking on elements by Xpath and accepting cookies applicable for all websites. We then created a child class of our basic scraper named "VNDBScraper" in a separate file, which is dedicated to the VNDB website.

## Milestone 4: Retrieving image & text data






