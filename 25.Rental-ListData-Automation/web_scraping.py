from bs4 import BeautifulSoup
import requests


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.6312.86 Safari/537.36 Brave/1.64.113",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)

data = response.text

soup = BeautifulSoup(data, "html.parser")

all_links_elements = soup.select(".StyledPropertyCardDataWrapper a")

all_links = [link['href'] for link in all_links_elements]

print(f"{len(all_links)} links found")

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")

all_address = [address.get_text().replace(' | ', ' ').strip() for address in all_address_elements]
print(all_address)

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [prices.get_text().replace('/mo','').split('+')[0] for prices in all_price_elements]
print(all_prices)
