import smtplib, ssl



port = 465
sender_mail = "email.sender489@gmail.com"
password = "K^X7KroA9R%2nx%"

reciver_mail = "jo.walter97@gmx.de"

message = "Hallo Welt!"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_mail, password)

    server.sendmail(sender_mail, reciver_mail, message)


