import imghdr
import smtplib

from email.message import EmailMessage

PASSWORD = 'random'
SENDER = 'app@flacke.com'
RECIEVER = 'app@flacke.com'


def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = 'New Customer Showed Up'
    email_message.set_content('Hey we just saw a new customer')
    with open(image_path, 'rb') as file:
        content = file.read()

    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, RECIEVER, email_message.as_string())
    gmail.quit()

