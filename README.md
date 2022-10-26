# ComputerVisionPro_AICore

This Python project is an implementation of an industrial-grade data collection pipeline, which automatically browse a website and collect information from it.

This project requires [Selenium](https://github.com/SeleniumHQ/selenium/tree/trunk/py) and [Pandas](https://github.com/pandas-dev/pandas) modules.

## Milestone 1 ~ 3: Prototyping the web scraper

The website I am scraping is [VNDB](https://vndb.org/), a visual novel wiki, because it is a website that does not change its layout very often. We aim to collect the data from top-rated visual novels with a certain keyword or genre.

I created a general-purpose basic scraper class with Selenium, with basic functionalities including clicking on elements by Xpath and accepting cookies applicable for all websites. We then created a child class of our basic scraper named VNDBScraper in a separate file, which is dedicated to the VNDB website.

## Milestone 4: Retrieving image & text data

In the VNDBScraper class, I created a method named download_img() which downloads the head image from the description page of a visual novel

## Milestone 5: Testing

I tested all the methods of VNDBScraper class with the built-in unittest module and made sure that all the public methods are running error-free and giving the output as intended. For example I confirmed the get_info() method correctly gives a list of dictionaries, each encodes all available information for a search result.

## Milestone 6: Create a docker image to run our scraper

We created a dockerfile according to the instructions given in [docker_selenium.md](https://aicore-files.s3.amazonaws.com/Foundations/DevOps/docker_selenium.md) and built a docker image to run our scraper.

The command used are as follows:




