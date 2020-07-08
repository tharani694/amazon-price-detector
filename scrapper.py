import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL ='https://www.amazon.in/dp/B07RTYFS9S/ref=s9_acsd_ri_bw_r2_camerash_1_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=M1P32G4GSH0WXSKGH87Y&pf_rd_t=101&pf_rd_p=646e166b-9457-4ae4-ba06-c579251512b8&pf_rd_i=10726224031'

headers = { "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text().replace(',','')
    #price.replace(',','')
    converted_price = float(price[2:])

    if(converted_price < 58000.0):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('tharani12ia@gmail.com', 'yjsenbyxfagnmauy')

    subject = 'Price fell down!'
    body = 'Check the amazon link!! https://www.amazon.in/dp/B07RTYFS9S/ref=s9_acsd_ri_bw_r2_camerash_1_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=M1P32G4GSH0WXSKGH87Y&pf_rd_t=101&pf_rd_p=646e166b-9457-4ae4-ba06-c579251512b8&pf_rd_i=10726224031'

    msg = f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'tharani12ia@gmail.com',
        'uglytharani@gmail.com',
        msg
    )

    print('EMAIL HAS BEEN SENT')
    server.quit()

check_price()

while(True):
    check_price()
    time.sleep(18000)