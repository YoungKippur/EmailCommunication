import imaplib
import email
import sys
from datetime import datetime

host = 'smtp.gmail.com'
username = 'somOne@gmail.com' # Tu email 
password = ' ' # Tu contraseña

def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")

    msgg = " "

    _, search_data = mail.search(None, 'UNSEEN')

    for num in search_data[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)

        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                msgg = body.decode()
                return msgg
            
    return msgg

while True:
    my_inbox = " "
    now = str(datetime.now())
    my_inbox = get_inbox()
    if my_inbox ==  "shutdownAll":
        sys.stdout.write("shutdownAll...  [")
        sys.stdout.write(now)
        sys.stdout.write("]")
        print(" ")