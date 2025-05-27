import firebase_admin
from firebase_admin import credentials, messaging

# Asegúrate de que la ruta sea correcta según tu estructura de carpetas
cred = credentials.Certificate("./credentials/firebase_admin_sdk.json")

# Para evitar errores si ya fue inicializado
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Función para enviar notificación push
def send_push_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,  # Token único del dispositivo desde la app móvil
    )

    try:
        response = messaging.send(message)
        print("Notificacion enviada:", response)
    except Exception as e:
        print("Error al enviar la notificacion:", e)
