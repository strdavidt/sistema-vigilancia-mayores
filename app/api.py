from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bd_config import db  # importar la conexión a Firestore
from typing import Optional

app = FastAPI()

class UserData(BaseModel):
    uid: str
    nombre: str
    correo: str
    token_fcm: str

@app.post("/registrar_usuario/")
async def registrar_usuario(data: UserData):
    print("Datos recibidos:")
    print(f"UID: {data.uid}")
    print(f"Nombre: {data.nombre}")
    print(f"Correo: {data.correo}")
    print(f"Token FCM: {data.token_fcm}")

    # Referencia al documento por UID
    doc_ref = db.collection("usuarios").document(data.uid)
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.update({
            "token_fcm": data.token_fcm
        })
        return {"mensaje": "Token actualizado correctamente (usuario ya registrado)"}

    # Guardar si no existe
    doc_ref.set({
        "nombre": data.nombre,
        "correo": data.correo,
        "token_fcm": data.token_fcm
    })

    return {"mensaje": "Usuario registrado exitosamente"}
