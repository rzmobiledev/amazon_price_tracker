import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/COMFEE-Stainless-Steamer-One-Touch-Programs/dp/B0987JNH24/?th=1"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "referer": "https://www.amazon.com/",
    "sec-fetch-site": "cross-site",  # or same-origin
    "sec-fetch-mode": "navigate",
}


class AmazonPriceTracker:

    def show_current_price(self) -> float:
        response = requests.get(url=URL, headers=HEADERS)
        soup = BeautifulSoup(markup=response.content, features="html.parser")

        price_text = soup.find(name="span", class_="a-price-whole").getText()
        float_text = soup.find(name="span", class_="a-price-fraction").getText()

        price = float(price_text + float_text)
        return price
