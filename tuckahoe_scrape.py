import requests
from bs4 import BeautifulSoup

# Fetch and parse the webpage
tuckahoe_scrape = requests.get("https://www.tuckahoeschools.org/")
soup = BeautifulSoup(tuckahoe_scrape.text, "html.parser")
links = soup.find_all('a')  # Find all <a> tags (hyperlinks)
for link in links:          # Loop through each link, extracting and printing the href attribute
    href = link.get('href')
    if href:  # Only print the link if it's not None
        print(href)

