import requests #lets us get data from a website
from bs4 import BeautifulSoup #pythons library for getting individual items from website

import smtplib #mail protocol
import ssl #secure connection

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import time #importing time lets us run this Infinitely 

# storing our link in a variable 
URL = 'https://www.amazon.com/dp/B08GLX7TNT/?coliid=I1DVWOY5H6XTA5&colid=13ADXHC8L4W24&psc=1&ref_=gv_ov_lig_pi_dp'

# create a dictionary for our headers, this tells us information in our browser
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}


def checking_price():
    """Description:
    Checking_price goes on to declared website and grabs information
    and uses that information to determine if the price is low enough
    to send an email.

    Parameters: None

    Return: None
    """
    page = requests.get(URL, headers=headers) #gets data

    soup = BeautifulSoup(page.content, 'html.parser') #gets content

    title = soup.find(id="productTitle").get_text() #finds the title tag in html

    print(title.strip()) #make sure its getting the right information, this should be the product title

    price = soup.find(id="priceblock_ourprice").get_text() #this is a string and needs to be converted to a number
    converted_price = int(price[1:-3]) #converts the price to a number and takes away the $ and decimals

    print(converted_price) #make sure everything is looking good

    if(converted_price < 150): #if its below the price we want, calls send_email function
        send_email_google()


def send_email_google():

    """Description:
    send_email_google gets information about where and to whom the
    email is sent to, and what that message contains. Uses MIME
    to set up the message, subject, to, from, and attaching the
    message to the body. It then sents up a server to use to send
    email and then logins and sends the email. If none of this
    works it sends an error message saying that it doesn't work.

    Parameters: None

    Return: None
    """

    try:

        #variables to store information for later
        email = 'ntsgames2222@gmail.com'
        password = '######' #for security reasons I have blocked this
        send_to_email = 'smith.tanner2222@gmail.com'
        subject = 'Price fell down!'
        message = 'Check the amazon link: https://www.amazon.com/dp/B08GLX7TNT/?coliid=I1DVWOY5H6XTA5&colid=13ADXHC8L4W24&psc=1&ref_=gv_ov_lig_pi_dp'

        #using MIME to send the email
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        #Since we are using just a link we can use a plain text message option
        msg.attach(MIMEText (message, 'plain'))

        #creating a server using smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587) #this is gmails protocol with a port of 587
        server.starttls() #encrypts the connection
        server.login(email, password) #login with credentials
        text = msg.as_string() #sending message as a string
        server.sendmail(email, send_to_email, text) #send the email with the right paramenters
        server.quit() #quit the server

        print("Message has been sent!") # the good message

    except:
        
        print("Unable to send") #the bad message

def main():
    """
    Main function of the program to run everything
    """

    #This allows us to run Infinitely 
    while(True):

        checking_price()
        time.sleep(86400) #runs once a day

# better practice for running main
if __name__ == "__main__":
    main()
