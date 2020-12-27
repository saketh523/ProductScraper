import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from re import sub
import smtplib 
import time

URL = 'https://www.amazon.in/DJI-Mavic-Mini-More-Combo/dp/B07RKPP1YL/ref=sr_1_1?crid=2DM00OTLGPJ4K&dchild=1&keywords=mavic+mini&qid=1609026126&sprefix=mavi%2Caps%2C309&sr=8-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

def check_price():
        
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()

    converted_price = Decimal(sub(r'[^\d.]', '', price))

    if(converted_price > 80000):
        send_mail()
    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('networkcapture123@gmail.com', 'feuhlqadhiofggrj')

    subject = 'Price fell down!'
    body = 'Check the amazon link: ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'networkcapture123@gmail.com',
        'jammulasakethreddy@gmail.com',
        msg
    )

    print('Hey EMAIL HAS BEEN SENT!')

    server.quit()

check_price()

# Check daily
#while(True):
 #   check_price()
  #  time.sleep(86400)






