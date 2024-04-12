from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com")  #variable that stores a GET request
soup = BeautifulSoup(page_to_scrape.text, "html.parser")     #variable that stores the content of the website
quotes = soup.findAll("span", attrs={"class": "text"})
print(quotes)

for quote in quotes: #iterates through each quote
    print(quote.text)