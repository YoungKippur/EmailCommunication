# TERMINADO (Creo, la verdad que no entiendo eso del final pero anda asi que ta bien :) (Es una cara feliz))
# auto-py-to-exe

import smtplib
import sys
import requests    # Creo que esto esta de mas (Pero ni idea)
import time
from datetime import datetime  # Tampoco tengo idea de porque mierda metio esto

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'somOne@gmail.com' # Tu email 
password = '1234' # Tu contraseña
msgg1 = "shutdownAll"

def send_mail(text='Email Body', subject='serverData', from_email='Server <somOne@gmail.com>', to_emails=['someOne@gmail.com']): # !Remplazar¡
    assert isinstance(to_emails, list)
 
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    
    msg_str = msg.as_string()
    # login
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

    # with smtplib.SMTP() as server:
    #      server.login()
    #      pass

# Menu
print("Seleccione una de las siguientes opciones:")
print("    1. Apagar todas las computadoras")
print("    0. Salir")
print("    ")
sel = int(input("Eleccion: "))
print("    ")

if sel == 1: 
    try:
        send_mail(text=msgg1)
        sent = "Comando enviado correctamente :)"
        print(sent)
        time.sleep(3)
    except:
        sent = "No se pudo enviar el comando :("
        print(sent)
        sent = "Contacte con el administrador (Marcos)"
        print(sent)
        time.sleep(5)

if sel == 0:
    print("Adios.. :)")
    time.sleep(3)