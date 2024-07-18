import requests
import selectorlib
import smtplib, ssl      #sending out email
import os                #sending out email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

URL = "http://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scraping from web"""
    request = requests.get(url)
    source = request.text
    return source

def extract(source):
   extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
   value = extractor.extract(source)["tours"]
   return value

def send_email(message):
 # Email content
    sender_email = "carlocasabuens@gmail.com"
    receiver_email = "carlocasabuens@gmail.com"
    subject = "Music events"
    body = "New event was found"

# Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

# Add body to email
    message.attach(MIMEText(body, "plain"))

    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Port for TLS encryption

    try:
        # Establish a secure session with the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, "nzor kfwx pdwv hmdd")  # Replace with your email password

        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

    finally:
        try:
            server.quit()  # Close the SMTP server connection
        except NameError:
            pass  # Handle the case where `server` was never defined due to an exception
    
    
def store(extracted):
    with open("data.txt", "a") as file:   
        file.write(extracted + "\n")

def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
    
        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:                       #checking if extracted is not in data.txt
                store(extracted)                               #will only store if there is an event
                send_email(message="New event was found!")
        time.sleep(2)      

    