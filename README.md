# Data Collection Pipeline Project

This Python project is an implementation of a data collection pipeline, which automatically browse a website and collect information from it.

This project requires [Selenium](https://github.com/SeleniumHQ/selenium/tree/trunk/py) and [Pandas](https://github.com/pandas-dev/pandas).

## Milestone 1 ~ 3: Prototyping the web scraper

The website I am scraping is [VNDB](https://vndb.org/), a visual novel wiki, because it is a website that does not change its layout very often. The script will be able to collect the data from top-rated visual novels with a certain keyword or genre.

I created a general-purpose basic scraper class with Selenium, with basic functionalities including clicking on elements by Xpath and accepting cookies applicable for all websites. I then created a child class of our basic scraper named VNDBScraper in a separate file, which is dedicated to the VNDB website.

## Milestone 4: Retrieving image & text data

In the VNDBScraper class, I created a method named `download_img()` which downloads the head image from the description page of a visual novel and save it in raw_data/images. Note that this method is never invoked - I just want to practise retrieving image data.

Then I created `get_info()` method which scrapes the information of all the visual novels in the search result table on a single page and save them as a list of dictionaries. The information collected includes description page url, title, platforms, languages available, release date, popularity and rating. I also created `next()` method which finds the "next page" button and clicks on it.

The procedure of scraping is contained in the `start_scrape()` function, which calls `get_info()` to scrape the data from the first page. Then it goes on to the next page until the number of novels scraped reaches a certain limit (default 300) or when it reaches the last page.
I made use of the `selenium.common.exceptions.NoSuchElementException` to determine whether or not we are on the last page:

```
while True:
    # Collect info with scraper.get_info()
    try:
        scraper.next()
    except NoSuchElementException:
        print('Scraping finished - Last page scraped.')
        break
```

Finally, the data collected are stored in [raw_data/data.json](raw_data) .

## Milestone 5: Testing

I tested all the methods of VNDBScraper class with the built-in unittest module and made sure that all the public methods are running error-free and giving the output as intended. For example, I confirmed the `get_info()` method correctly gives a list of non-empty dictionaries, each encodes all available information for a search result. Also, to test the `download_image()` method, I made use of the `glob` package and checked the path of the image with the following code:

```
list_of_files = glob.glob('raw_data/images/*')
image_path = max(list_of_files, key = path.getctime) # This returns the latest file
```

## Milestone 6: Create a docker image to run our scraper

I created a dockerfile according to the instructions given in [docker_selenium.md](https://aicore-files.s3.amazonaws.com/Foundations/DevOps/docker_selenium.md) and built a docker image to run our scraper.

The commands used are as follows:

To build the image:`docker build -t vndbscraper`

To push the container to Dockerhub:`docker tag vndbscraper alanimp18/vndbscraper_img` `docker push alanimp18/vndbscraper_img`

## Milestone 7: Setup the Github secrets

I generated an access token for my Docker CLI. Then I setup the Github secrets which contains the credentials required to log into my dockerhub repo. I also created a GitHub action that builds and pushes Docker image to DockerHub repo.
