# No corre hasta añadir el modelo y guardarlo como en la carpeta de Apis.

import gradio as gr
import pandas as pd
import pickle

params_name=["age", "failures", "goout", "health"]
#Load model
with open("model.pkl","rb") as f:
    model=pickle.load(f)

def predict(*args):
    answer_dict={}
    for i in range(params_name):
        answer_dict[params_name[i]]=[args[i]]

    single_instance=pd.DataFrame.from_dict(answer_dict)
    prediction=model.predict(single_instance)
    response=format(prediction[0], '.2f')
    return response


with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Predicción de rendimiento escolar
        """
    )

    with gr.Row():
        with gr.Column():
            #Ojo, si es subtítulo se usan dos #
            gr.Markdown(
                """
                ## Predecir las notas en función al comportamiento
                """
                )

            age=gr.Slider(label='Edad', minimum=15, maximum=22, step=1, randomize=True)
            failures=gr.Slider(label='Saltos de clase', minimum=1, maximum=5, step=1, randomize=True)
            goout=gr.Radio(label='Salidas amigos', choices=[1,2,3,4,5], value=1) #Valor defecto al arranque de la app
            health=gr.Dropdown(label='Salud', choices=[1,2,3,4,5], multiselect=False, value=1)

        with gr.Column():
            gr.Markdown(
                """
                ## GPA: Índice académico
                """
                )

            label=gr.Label(label="GPA")
            predict_button=gr.Button(value='Predicción')
            predict_button.click(predict, inputs=[age,failures,goout,health,], outputs=[label,], )

demo.launch()
