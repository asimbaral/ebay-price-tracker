import requests
import bs4
from bs4 import BeautifulSoup
import smtplib
import time
from email.message import EmailMessage

#Enter email here:
myEmail = ""
print(myEmail)
password = str(input("Enter your gmail password: "))
receiversEmail = ""

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print("Email Server created!")
server.login(myEmail, password)
print("Logged in!")

def sendEmail():
    url = "https://www.ebay.com/itm/Bose-QuietComfort-35-II-Wireless-Headphones-Factory-Renewed/164122980384?epid=17031092936&hash=item26367df020%3Ag%3AQywAAOSwM9hea69H&_trkparms=%2526rpp_cid%253D5d03f86cb1a35b73f55871fe&var=463744408894"

    lowestPrice = 200

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="itemTitle")
    unwanted = title.find('span')
    unwanted.extract()

    finalTitle = title.text.strip()

    price = soup.find(id="mm-saleDscPrc")
    finalPrice = float(str(price.text.split(" ")[1])[1:])

    message = "The price is now lower than $" + str(lowestPrice) + "! \n\n " + url

    msg = EmailMessage()
    msg.set_content(message)

    subject = finalTitle + ": Price has been lowered!"

    
    msg['Subject'] = subject
    msg['From'] = myEmail
    msg['To'] = receiversEmail

    print("Checking price now!")
    if(finalPrice <= lowestPrice):
        server.send_message(msg)
        print("Email Sent!")
        server.quit()

    time.sleep(3600)


while True:
    sendEmail()
