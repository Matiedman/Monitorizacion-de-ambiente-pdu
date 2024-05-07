import smtplib, os, ssl, pickle, requests                                 # Import smtplib for sending function
from dotenv import load_dotenv
from email.message import EmailMessage                          	  # Import the email modules we'll need
from google.oauth2.credentials import Credentials               
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from json import dumps
from httplib2 import Http


email_sender, email_reciever, password = "", "", ""

def emailConfig():

    load_dotenv() # Se carga el archivo .env o se lo llama para que sea usado. 
    global email_sender, email_reciever, password

    # Se guardan el mail con remitente, destinatario. 
    email_sender = "email que envia alertas."
    password = os.getenv('PASSWORD')                           # Se accede al .env y se busca el valor de "PASSWORD".
    email_reciever = "email de Infraestructura que recibe las alertas."                     
    return

# Se envian mails alertando sobre un evento ambiental ocurrido. Puede ser haber pasado los limites de humedad o temperatura
def sendEmailsToAlertForHumi(humiData):

    sendMsgsAlert("humi")

    subject  = "ALERTA! La humedad pasó los limites establecidos."
    
    # Lo que sigue es la construccion del cuerpo del msj a enviar. Se puede hacer en HTML. Tambien se pueden añadir imágenes. 
    if humiData < 25:
        body = "La humedad esta a menos del 25%. Al momento de este email marcó " + str(humiData) + "%. Realizar las acciones pertinentes. "     
    
    else:
        body = "La humedad esta a mas del 90%. Al momento de este email marcó " + str(humiData) + "%. Realizar las acciones pertinentes. "
        
   # Se crea el mail  asunto, y cuerpo del mensaje.
    theEmail = EmailMessage()                                         # Se inicializa el objeto email para luego cargar los parametros.
    theEmail["From"] = email_sender
    theEmail["To"] = email_reciever
    theEmail["Subject"] = subject
    theEmail.set_content(body)
    contexto = ssl.create_default_context()                           # Se crea un contexto o canal seguro para la comunicacion por defecto.

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = contexto) as smtp:   # Se accede al servidor, en este caso al de gmail.
        smtp.login(email_sender, password)                                      # Se loguea para enviar el email.
        smtp.sendmail(email_sender, email_reciever, theEmail.as_string())       # Se envía el mail

    return


def sendEmailsToAlertForTemp(tempData):

    sendMsgsAlert("temp")

    subject  = "ALERTA! La temperatura pasó los limites establecidos"
    # Lo que sigue es la construccion del cuerpo del msj a enviar. Se puede hacer en HTML. Tambien se pueden añadir imágenes. 
    if tempData < 12:
        body = "La temperatura esta a menos de 12ºC. Al momento de este email marcó " + str(tempData) + "ºC. Realizar las acciones pertinentes. "
    else:
        body = "La temperatura esta a mas de 20ºC. Al momento de este email marcó " + str(tempData) + "ºC. Realizar las acciones pertinentes. "
        
    theEmail = EmailMessage()                                         # Se inicializa el objeto email para luego cargar los parametros.
    theEmail["From"] = email_sender
    theEmail["To"] = email_reciever
    theEmail["Subject"] = subject
    theEmail.set_content(body)
    contexto = ssl.create_default_context()                           # Se crea un contexto o canal seguro para la comunicacion por defecto.

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = contexto) as smtp:   # Se accede al servidor, en este caso al de gmail.
        smtp.login(email_sender, password)                                      # Se loguea para enviar el email.
        smtp.sendmail(email_sender, email_reciever, theEmail.as_string())       # Se envía el mail
    
    return
    
# Se envian las alertas por medio del chat de Google. 
def sendMsgsAlert(msg):

    # """Google Chat incoming webhook."""

    # Se crea el contexto. 
    url = "https://chat.googleapis.com/v1/spaces/AAAAzTP2i7k/messages?key= Una contraseña_con Much@s caracteres como estos #$%DFWdfsdf#$%SDSFS#..."
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    
    if msg == "humi":
        app_message = {"text": "¡¡¡ATENCIÓN!!!. Se ha pasado el limite establecido de humedad en el DC Campus Virtial. Realizar acciones necesarias. "}
        http_obj.request(uri=url, method="POST", headers=message_headers, body=dumps(app_message), )
        return
    
    if msg == "temp":
        app_message = {"text": "¡¡¡ATENCIÓN!!!. Se ha pasado el limite establecido de temperatura en el DC Campus Virtial. Realizar acciones necesarias. "}
        http_obj.request(uri=url, method="POST", headers=message_headers, body=dumps(app_message), )
        return
    
    #Mensaje por defecto:    
    app_message = {"text": "¡¡¡ATENCIÓN!!!. Se le ha enviado un email alertando sobre el traspaso de los limites establecidos de temperatura y/o humedad."}
    http_obj.request(uri=url, method="POST", headers=message_headers, body=dumps(app_message), )
    return


    
# Ejemplo de TRY and CATCH
    # try: 
    #     smtp = smtplib.SMTP('smtp.gmail.com', 465) 
    #     smtp.sendmail(remitente, destinatario, email) 
    #     print ("Correo enviado") 
    # except Exception as e: 
    #     print ("""Error: el mensaje no pudo enviarse. 
    #     Compruebe que sendmail se encuentra instalado en su sistema""")
    #     print("su error es el siguiente: " + e)
