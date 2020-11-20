import smtplib, ssl
import getpass

import json

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

# -------------------------------------------
# Sender einlesen, Port einstellen und den Empfänger einstellen
print("Datei lesen...")
with open("e-mail.json") as read_file:
    sender = json.load(read_file)

port = 465

reciver_mail = "jo.walter97@gmx.de"


# --------------------------------------------
# Nachricht bauen
print("Nachricht erstellen...")

msg = MIMEMultipart()
msg["From"] = sender["adress"]
msg["To"] = reciver_mail
msg["Subject"] = "Hallo Welt!"

# Nachrichtentext einfügen
msg.attach(MIMEText("Bitte Anhang lesen.", "plain"))

# Anhang anhängen
filename = "Anhang.txt"
with open(filename, "rb") as fil:
    Anhang = MIMEBase("application", "octet-steam")
    Anhang.set_payload(fil.read())

encoders.encode_base64(Anhang)
Anhang.add_header(
    "Content-Disposition",
    f"attachment; filename = {filename}",
)

msg.attach(Anhang)
text = msg.as_string()

# ------------------------------------------
# Nachricht senden
print("Nachricht senden...")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender["adress"], sender["password"])

    server.sendmail(sender["adress"], reciver_mail, text)


print("Fertig!")