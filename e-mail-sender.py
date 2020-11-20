import smtplib, ssl
import getpass

import json

with open("e-mail.json") as read_file:
    sender = json.load(read_file)



port = 465

reciver_mail = "jo.walter97@gmx.de"

message = "Hallo Welt!"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender["adress"], sender["password"])

    server.sendmail(sender["adress"], reciver_mail, message)


