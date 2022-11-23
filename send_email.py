import smtplib
import ssl
host = 'smtp.gmail.com'
port = 465

username = 'abhihot9@gmail.com'
password = 'hyaooxdmtponiwvz'
receiver = 'abhihot9@gmail.com'
context = ssl.create_default_context()


def send(message):
    with smtplib.SMTP_SSL(host, port , context= context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
