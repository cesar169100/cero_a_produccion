# Esquema elemental para la creación de una appi
from fastapi import FastAPI
import uvicorn

data=[
    {
        "id":1,
        "name":"lo que sea",
        "price":10
    },
    {
        "id":2,
        "name":"lo que sea 2",
        "price":100 
    }
]

app=FastAPI()

#Hace referencia al root y añade este simbolo al final de la url. En este caso la url será http://127.0.0.1:800,
#lo que hará la siguiente línea es para abrir http://127.0.0.1:8000/. Esto es el endpoint estándar, podemos
#crear más.
#@app.get("/")  
@app.get("/home") #Otro ejemplo. Abrirá http://127.0.0.1:8000/home
def read_root():
    return("Appi ejemplo")

#Otro endpoint
@app.get("/productos")
def read_productos():
    return data

#Otro que devuelve el id solicitado
@app.get("/productos/{data_id}") #Valida que es entero
def read_productos(data_id: int):
    product=[product for product in data if product['id']==data_id]
    if len(product)==0:
        return {"error":"producto no encontrado"}, 404
    return product[0]


#Levantamos en http://127.0.0.1:8000 Ejecutar desde consola como ejemplo
if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

## Para correr lo anterior es necesario definir ciertas condiciones para que nuestro web server corra nuestro
## programa; como definir el host, los puertos, etc y eso se hace utilizando uvicorn.