import smtplib

SENDER_MAIL = ""
SENDER_PASS = ""

def send_email(receiver_mail, subject, body):
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_MAIL, password=SENDER_PASS)
        connection.sendmail(
          from_addr=SENDER_MAIL,
          to_addrs=receiver_mail,
          msg=message
        )
