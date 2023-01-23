# README
This script is for scraping quotes and author details from Quotes.toscrape.com, a website that serves as a playground for web scraping. It uses the requests, json, pandas and BeautifulSoup library to make GET requests, parse and store the data.

## How to Use
1. Install the required libraries: requests, json, pandas and BeautifulSoup
2. Run the script
3. The resulting data will be stored in a Pandas DataFrame and exported to a csv and excel file.
4. Code Explanation

The script does the following:

1. Defines the URL for the website
2. Defines a Crawler class that has methods for scraping quotes and author details, and for storing the data in a Pandas DataFrame and exporting it to a csv and excel file.
3. The get_quotes method makes a GET request to the website, and using BeautifulSoup, it scrapes the quotes and author details from the HTML.
4. The get_detail method makes a GET request to the author's detail page, and using BeautifulSoup, it scrapes the author's additional information.
5. The generate_format method takes the scraped data and stores it in a Pandas DataFrame and exports it to a csv and excel file.
6. The crawling() method calls the above methods in the right order to retrieve, process and store the data.

Please note that the script is using the endpoint https://quotes.toscrape.com/ which is a free endpoint and the structure of the data returned by the endpoint is static.
Also, the script uses the headers to provide the user-agent while making the request.
