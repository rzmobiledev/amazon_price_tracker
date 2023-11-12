import smtplib
import os
from dotenv import load_dotenv
from amazon_tracker import AmazonPriceTracker

load_dotenv()

HOST = "smtp.gmail.com"
PORT = 587
PASSWORD = os.environ.get("GMAIL_API_KEY")
FROM = "rzmobiledev@gmail.com"
TO = "rizal.safril@gmail.com"

# scrapping price from class AmazonPriceTracker
price_tracker = AmazonPriceTracker()
current_price = price_tracker.show_current_price()

if current_price < 100.00:
    with smtplib.SMTP(host=HOST, port=PORT) as conn:
        conn.starttls()
        conn.login(user=FROM, password=PASSWORD)
        conn.sendmail(
            msg=f"Subject:Price is going down\n\nThe price is down at ${current_price}",
            from_addr=FROM,
            to_addrs=TO
        )
