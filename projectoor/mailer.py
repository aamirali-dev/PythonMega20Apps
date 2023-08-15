import smtplib
import ssl

def send_email(msg):
    host = 'localhost'
    port = 2525

    username = ''
    password = ''

    receiver = 'app8flask@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg)
