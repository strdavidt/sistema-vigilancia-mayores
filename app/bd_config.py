import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("../credentials/firebase_admin_sdk.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Crear la conexión a Firestore
db = firestore.client()
