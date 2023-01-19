import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url: str = "https://quotes.toscrape.com"


class Crawler(object):
    def __init__(self, url: str):
        self.url = url
        self.headers: dict = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
}


    def get_quotes(self, url: str):
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")

            # Scrapping Process
            contents = soup.find_all("div", attrs={"class": "quote"})
            quotes_list: list = []
            for content in contents:
                quote = content.find("span", attrs={"class": "text"}).text.strip()
                author = content.find("small", attrs={"class": "author"}).text.strip()

                # Retrieval of author details
                author_detail = content.find("a")["href"]

                # Data Processing
                data_dict: dict = {
                    "quote": quote,
                    "quotes by": author,
                    "author detail": url + author_detail,
                }
                quotes_list.append(data_dict)

            # Convert to JSON
            with open("quotes.json", "w+") as f:
                json.dump(quotes_list, f)

            print("Data Berhasil di Generate")
            return quotes_list

    def get_detail(self, detail_url: str):
        res = requests.get(detail_url, headers=self.headers)

        if res.status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")

        # Scraping Process

            author_title = soup.find("h3", attrs={"class": "author-title"}).text.strip()
            born = soup.find("span", attrs={"class": "author-born-date"}).text.strip()
            location = soup.find("span", attrs={"class": "author-born-location"}).text.strip()
            description = soup.find("div", attrs={"class": "author-description"}).text.strip()

            # Data Processing
            data_dict = {
                "author_title": author_title,
                "born": born,
                "born location": location,
                "description": description,
            }

            return (data_dict)

    def generate_format(self, filename: str, results: list):
        df = pd.DataFrame(results)
        if ".csv" or ".xlsx" not in filename:
            df.to_csv(filename + ".csv", index=False)
            df.to_excel(filename + ".xlsx", index=False)

        print("data generated")

    def crawling(self)-> list[dict[str,str]]:
        results: list[dict[str, str]] = []

        quotes: list = self.get_quotes(url=url)
        for quote in quotes:
            detail = self.get_detail(detail_url=quote["author detail"])

            final_result: dict = {**quote, **detail}

            results.append(final_result)

        # Process Data
        self.generate_format(results=results, filename="reports")

        return results




if __name__ == "__main__":
    scraper: Crawler = Crawler(url=url)
    scraper.crawling()

