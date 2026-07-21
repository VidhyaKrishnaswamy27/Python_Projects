import requests
from bs4 import BeautifulSoup
import smtplib

url="https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CYMYK6?th=1"
header = {
    "User-Agent": "CCBot/2.0 (https://commoncrawl.org/faq/)",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url,headers=header)
web_page=response.text

soup=BeautifulSoup(web_page,"html.parser")

price=soup.find(name="span",class_="aok-offscreen")
amazon_price=price.get_text()
print(amazon_price)

product=soup.find(name="span",id="productTitle").getText().split("\n")[0]
print(product)

# if amazon_price<100:
#     email="krishnaswamy.vidhya@gmail.com"
#     password="tqkmkgsrbhaytmsd"
#
#     with smtplib.SMTP("smtp.gmail.com",587) as server:
#         server.starttls()
#         server.login(email,password)
#         server.sendmail(email,email,f"Subject: {product} price drop\n Amazon price dropped for {product}below target price. Buy now. Click below {url}".encode("utf-8"))
#
#


