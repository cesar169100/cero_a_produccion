import pandas as pd
from funpymodeling.exploratory import freq_tbl, status
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
# atención, asume 0.5 como umbral de decisión
from sklearn.metrics import ConfusionMatrixDisplay
import seaborn as sns
import datetime as dt

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
############################################# --Clasificacion
data_x = data.drop('Response', axis=1)
data_y = data['Response']
data_x = data_x.values
data_y = data_y.values

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.3)
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

ConfusionMatrixDisplay.from_estimator(
    rf, x_train, y_train,
    display_labels=['no','si'],
    cmap='Blues',
    normalize='true',
    )