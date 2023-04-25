import pandas as pd
from funpymodeling.exploratory import freq_tbl, status
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
# atención, asume 0.5 como umbral de decisión
from sklearn.metrics import ConfusionMatrixDisplay
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from yellowbrick.classifier import DiscriminationThreshold
from sklearn.metrics import RocCurveDisplay
import pickle

data = pd.read_csv("/Users/Cesar.deAlba/Desktop/Cursos/cero_a_produccion/materiales/marketing_campaign.csv", sep=';')
data.head(5)
status(data)
data=data.drop(['ID','Z_CostContact','Z_Revenue'], axis=1)
data['Dt_Customer']=pd.to_datetime(data['Dt_Customer'])
data['age']= pd.to_datetime("today").year - data['Year_Birth']
data['antiguedad']=(pd.to_datetime("today")-data['Dt_Customer']).dt.days/364
data=data.drop(['Year_Birth','Dt_Customer'],axis=1)
data=data[data['age']<=100]
data=data[pd.notnull(data['Income'])]
data2=pd.get_dummies(data) 
############################################# --Clasificacion
data_x = data2.drop('Response', axis=1)
data_y = data2['Response']
data_x = data_x.values
data_y = data_y.values

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.2)
rf = RandomForestClassifier(n_estimators = 1000, random_state = 99)
rf.fit(x_train, y_train)
y_pred1=rf.predict(x_train) #Directo
pred_probs=rf.predict_proba(x_train) #Con Probabilidades
y_prob_tr=pred_probs[:,1] # Probas de ser clase 1
y_prob_tr


sns.set(font_scale=1.2) #  Ajuste tamaño de letra (var global)

ConfusionMatrixDisplay.from_estimator(
    rf, x_train, y_train,
    display_labels=['no','si'],
    cmap='Blues',
    )
plt.show()

ConfusionMatrixDisplay.from_estimator( # En porcentajes
    rf, x_train, y_train,
    display_labels=['no','si'],
    cmap='Blues',
    normalize='true',
    )
plt.show()

# Se compara el y_train vs la predicción de x_train. Igual que el anterior pero de otra manera.
sns.set(font_scale=1.5)                 # Ajuste tamaño de letra (var global)
conf_mat1=pd.crosstab(index=y_train,    # filas = valor real
                     columns=y_pred1,   # columnas = valor predicho
                     rownames=['Actual'], 
                     colnames=['Pred'], 
                     normalize='index')
sns.heatmap(conf_mat1, annot=True, cmap='Blues', fmt='g')
plt.show()

# Aquí un ejemplo burdo de como cambiar el umbral de decisión
y_pred2=np.where(y_prob_tr > 0.35, 1, 0)
conf_mat2=pd.crosstab(index=y_train, 
                      columns=y_pred2,      # ¡cambio!
                      rownames=['Actual'], 
                      colnames=['Pred'], 
                      normalize='index')
sns.heatmap(conf_mat2, annot=True, cmap='Blues', fmt='g')
plt.show()
 
# Antes y después
sns.set(font_scale=1)       # Ajuste tamaño de letra (var global)
fig, ax = plt.subplots(1,2)  

sns.heatmap(conf_mat1, annot=True, cmap='Blues', fmt='g', ax=ax[0])
sns.heatmap(conf_mat2, annot=True, cmap='Blues', fmt='g', ax=ax[1])

fig.show(warn=False)

# Encuentra el mejor umbral, el parámetro fbeta es para darle más peso a uno de los dos que se toma en cuenta
# en el Fscore
visualizer = DiscriminationThreshold(rf)
visualizer.fit(x_train, y_train)        # Ajustar data al visualizador
visualizer.show()                       # Mostrar figura

#ROC 
tr_disp = RocCurveDisplay.from_estimator(rf, x_train, y_train)
ts_disp = RocCurveDisplay.from_estimator(rf, x_test, y_test, ax=tr_disp.ax_)
ts_disp.figure_.suptitle("ROC curve comparison")
plt.show()

# Guardar modelo
pickle.dump(rf, open('rf.pkl', 'wb'))
# Load
pickled_model = pickle.load(open('rf.pkl', 'rb'))
pickled_model.predict(x_test)

############################### --Regresión