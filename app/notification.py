# notification.py
from twilio.rest import Client

def send_notification(user_id: str, message: str, via: str):
    if via == "sms":
        # Configurar Twilio (debes reemplazar con tus credenciales)
        account_sid = 'tu_account_sid'
        auth_token = 'tu_auth_token'
        client = Client(account_sid, auth_token)
        
        # Número del usuario (en un caso real, debes obtenerlo de la base de datos)
        phone_number = "+123456789"
        
        client.messages.create(
            body=message,
            from_='+11234567890',  # Tu número de Twilio
            to=phone_number
        )
    elif via == "email":
        # Lógica para enviar correo electrónico (ej. usando SendGrid)
        pass
