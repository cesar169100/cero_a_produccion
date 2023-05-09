import requests

url_1="http://127.0.0.1:8000/home"
url_2="http://127.0.0.1:8000/productos"
url_3="http://127.0.0.1:8000/productos/1"
# Acceder al index/home
response=requests.get(url_3)
print(response.json())

## Para ejecutar, primero echar a andar la appi del main, luego, en otra terminal, correr el call_api