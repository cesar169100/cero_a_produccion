############# Hacer nuestro primer GET request
## https://www.coinlore.com/cryptocurrency-data-api
## https://cleanuri.com/docs
## https://http.dog/

import requests
## Método GET
url="https://api.coinlore.net/api/ticker/?id=90"
response=requests.get(url) # Si imprimimos esto, regresa el statuscode, 200 si salió bien
response.status_code #como número
response.headers #info de la peticion
response.encoding #utf-8 y otros, etc
## Ver la data como json
data=response.json()
data[0]['price_usd']
#########################################
url="https://devitjobs.us/api/jobsLight"
response=requests.get(url)
data=response.json()
# Guardar el json
import json
with open('data_json', 'w', encoding='utf-8') as f: #Nombre deseado, accion escribir(write) y permite caracteres especiales(utf-8)
    json.dump(data,f,ensure_ascii=False,indent=4) #Forma legible para leer

## Método POST request
url_servicio="https://cleanuri.com/api/v1/shorten"
data={
    'url':'https://www.escueladedatosvivos.ai/cursos/bootcamp-de-data-science',
}
response=requests.post(url_servicio,json=data)
datF=response.json()