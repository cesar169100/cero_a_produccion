import gradio as gr
import cv2 #Librería de computer vision. pip install opencv-python
from tensorflow.keras.applications.resnet50 import ResNet50, decode_predictions #pip install tensorflow

# Cargamos modelo
model=ResNet50(weights='imagenet')

def predict(input_image,top_number=3): #top_number son los ids con los que más identificó a la imagen
    img=cv2.resize(input_image,(224,224)) #Tamaño esperado por el modelo
    img=img.reshape(1,224,224,3) #dimensiones, color etc
    #Prediccion
    predictions=model.predict(img)
    #Reformat data: list -> tuple ->dict
    top_prediction=decode_predictions(predictions,top=top_number)[0]
    response={top_prediction[i][1]:float(top_prediction[i][2]) for i in range(top_number)}
    
    return response

title="Clasificador de objetos"
description="Un clasificador entrenado con ResNet50"
#article="<p style='text align=center'><a href='https://www.escueladedatosvivos.ai"
examples=["C:/Users/Cesar.deAlba/Pictures/delfin.png","C:/Users/Cesar.deAlba/Pictures/hoo_lee.jpg"]
gr.Interface(fn=predict,
             inputs=gr.Image(shape=(512,512)),
             outputs=gr.Label(num_top_classes=3),
             title=title,
             description=description,
             examples=examples
             ).launch()

gr.Interface(fn=predict,
             inputs=gr.Image(shape=(512,512)),
             outputs=gr.Label(num_top_classes=3),
             title=title,
             description=description,
             examples=examples
             ).launch(share=True) # Esto hace que se genere una url pública para que otros lo consulten. El link durará 72 horas
