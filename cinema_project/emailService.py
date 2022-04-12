import smtplib, ssl, email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def emailS(EMAIL_A, body, subject):
    EMAIL_ADDRESS = "karanrajsinghranawat@gmail.com"
    EMAIL_PASSWORD = "nsysklbkvydrgexm"

    # subject = "An email with attachment from Python"
    # body = "This is an email with attachment sent from Python"
    sender_email = EMAIL_ADDRESS
    receiver_email = EMAIL_A
    password = EMAIL_PASSWORD

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    # path = "/home/karan/Downloads/sec20-jagielski.pdf"
    # filename = "sec20-jagielski.pdf"
    # with open(path, "rb") as attachment:
    #     # Add file as application/octet-stream
    #     # Email client can usually download this automatically as attachment
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read())

    # encoders.encode_base64(part)

    # part.add_header(
    #     "Content-Disposition",
    #     f"attachment; filename= {filename}",
    # )
    # html = """\
    # <html>
    # <body>
    #     <p>Hi,<br>
    #     <h1>How are you?</h1><br>
    #     <a href="http://www.realpython.com">Real Python</a> 
    #     has many great tutorials.
    #     </p>
    # </body>
    # </html>
    # """
    # message.attach(MIMEText(html, "html"))
    message.attach(MIMEText(body, "plain"))
    # message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        return True
    except:
        return False