import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Python parser and email sender for checking the price of an item on Amazon.
#Created by Ryan Rasi.
#https://github.com/RyanRasi
#http://ryanrasi.com

#Variable initialisation and declaration.

#URL of item you want the parser to check for - default is Cyber Punk 2077.
URL = "https://www.amazon.co.uk/CD-Projekt-Red-Cyberpunk-2077/dp/B07DM6JTVZ/ref=sr_1_1?keywords=the+last+of+us+part+2&qid=1562425216&s=gateway&sr=8-1"

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#Add your email address here - may run into issues in two factor authentication is turned off.
email = "Enter your email address"
#Add your email password here, you can go onto the sign in using app passwords on the google website to generate a random one to use specifically for this - link is https://support.google.com/accounts/answer/185833?hl=en
email_password = "Enter your email password"

#Check price class is activated at line 77.
def check_price():
    page = requests.get(URL, headers=headers)
    #Gets the HTML content from the page.
    soup = BeautifulSoup(page.content, 'html.parser')
    #Finds the title of the item and parses it into text.
    title = soup.find(id="productTitle").get_text()
    #Finds the price with the currency identifier.
    price_currency = soup.find(id="priceblock_ourprice").get_text()
    price = price_currency.replace("£", "")
    #Replaces the pounds sterling currency identifier to nothing.
    converted_price = float(price[0:8])
    #Converts the price to a float so that it can have arguments applied to it .

    
    #Strips the blank space around the title.
    print(title.strip())
    #Prints the current price and adds the currency identifier.
    print("Current price is: £" + price)

    #The argument for checking if the price of the game has gone down to less than 48.99.
    if (converted_price < 50.00): #Check is the price is less than 50 and if it is then it will send me an email
        #If price has gone down then the send mail class is activated.
        send_mail(title, price) #Send mail class with the paramters of the title and price of product so that they can be included in the email subject and body


#Send mail class
def send_mail(title, price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #Server activation and communication.
    server.login(email, email_password)
    #Server login using details specified on lines 18 and 20.

    #Subject of email.
    subject = 'Price has fallen down for Amazon item'
    #Body of email - concatenates variables usch as price and the URL of product.
    body = title.strip() + '\n\nPrice now stands at £' + price + '\n\nCheck out the Amazon link \n' + URL

    msg = f"Subject: {subject}\n\n{body}"
    #Sends the email and encodes it with UTF-8 so that it can support sending the pound sterling symbol.
    server.sendmail(
        email,  #From email address.
        email,  #To email address.
        msg.encode("UTF-8") #UTF-8 Encoding.
    )   #Email is sent this way as it makes more sense for a sole person to send and recive emails from the same account with this parser.
    print('Email has been sent to ' + email)
    #Prints that the email has been sent in the terminal.
    #Quits the email server.
    server.quit()

#While loop that runs indefinitely that runs the check_price function and then waits an hour to run again.
while(True):
    check_price()
    #Checks once an hour if left continuously running.
    time.sleep(3600) #One hour
    #Loop waits an hour before running again to check the price, this may seem too short so the user can change it to something more reasonable such as a day.
#Program is designed to be ran until desired price is lowered and all of the values apart from the currency are in variables so that the user can easily adapt it to their needs.