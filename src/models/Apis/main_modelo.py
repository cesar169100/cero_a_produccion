import pandas as pd
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import uvicorn
from pydantic import BaseModel #Verificacion de tipos de dato
import pickle

app=FastAPI()
#Importar modelo. Esta ruta incompleta es para que corra desde terminal; para correr la linea normal es
#necesario poner la ruta completa desde le src/models/Apis/modelos/rf.pkl
with open("modelos/rf.pkl", "rb") as f: 
    model=pickle.load(f)

# Importar columnas
COLUMNS_PATH = "modelos/categories_ohe.pickle"
with open(COLUMNS_PATH, 'rb') as handle:
    ohe_tr = pickle.load(handle)

class Answer(BaseModel): #Especificamos que deben ser enteros
    ph : float
    Hardness : float 
    Solids : float
    Chloramines : float
    Sulfate : float
    Conductivity : float
    Organic_carbon : float
    Trihalomethanes : float
    Turbidity : float
    

@app.get("/")
def read_root():
    return {"message":"Modelo de prediccion"}


@app.post("/prediccion")
def predict_water_portability(answer:Answer):
    answer_dict=jsonable_encoder(answer) #De json a diccionario y de diccionario a data frame

    for key, value in answer_dict.items():
        answer_dict[key]=[value]

    single_instance=pd.DataFrame(answer_dict)
    # Reformat columns. NO ASIGNA EL DATO NUEVO A LA COLUMNA CORRESPONDIENTE
    single_instance_ohe = pd.get_dummies(single_instance).reindex(columns = ohe_tr).fillna(0)
    prediction=model.predict(single_instance_ohe)
    response={"Indice académico":prediction[0]}
    return response

    
if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
