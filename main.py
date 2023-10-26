from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

# Crea la base de datos
# conn = sqlite3.connect("contactos.db")

app = FastAPI()

class Contacto(BaseModel):
    email: str
    nombre: str
    telefono: str

conn = mysql.connector.connect(
    user='qyr7zk3plin84bf9',
    password='n90v5wi5ggfm0tjc',
    host='i0rgccmrx3at3wv3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    port='3306',
    database='xvjcrk5vf85h9jwg'
)

@app.get("/")
def inicio():
    return {'Developer by': 'Janneth f:'}

# Rutas para las operaciones CRUD
@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    """Crea un nuevo contacto."""
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contactos (email, nombre, telefono) VALUES (?, ?, ?)',
                    (contacto.email, contacto.nombre, contacto.telefono))
    conn.commit()
    return contacto

@app.get("/contactos")
async def obtener_contacto():
    """Obtiene todos los contactos."""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contactos')
    response = []
    for row in cursor:
        contacto = Contactos(email=row[0], nombre=row[1], telefono=row[2])
        response.append(contacto)
    return response

@app.get("/contactos/{email}")
async def obtener_contacto(email: str):
    """Obtiene un contacto por su email."""
    # Consulta el contacto por su email
    coursor = conn.cursor()
    cursor.execute('SELECT * FROM contactos WHERE email = ?', (email,))
    row = cursor.fetchone()
    if row: 
        contacto = Contacto(email=row[0], nombre=row[1], telefono=row[2])
        return contacto
    else:
        return None

@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contacto):
    """Actualiza un contacto."""
    # TODO Actualiza el contacto en la base de datos
    cursor = conn.cursor()
    cursor.execute('UPDATE contactos SER nombre = ?, telefono = ? WHERE email = ?',
              (contacto.nombre, contacto.telefono, contacto.email))
    conn.commit()
    return contacto


@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str):
    """Elimina un contacto."""
    # TODO Elimina el contacto de la base de datos
    cursor = conn.cursor()
    cursor.execute('DELETE contactos WHERE email = ?', (email,))
    conn.commit()
    return {"message": "Contacto eliminado con éxito"}
