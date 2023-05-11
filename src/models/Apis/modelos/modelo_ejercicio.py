import pandas as pd
from funpymodeling.exploratory import status
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
import pickle


dat=pd.read_csv("/Users/Cesar.deAlba/Desktop/Cursos/cero_a_produccion/materiales/water_potability_apis.csv", sep=",")
dat.head(5)
status(dat)
dat.shape
# Discretizamos variables con NA's
dat['ph_discretizado'] = pd.qcut(dat['ph'], q=10)
dat['ph_discretizado']=dat['ph_discretizado'].cat.add_categories("desconocido")
dat['ph_discretizado']=dat['ph_discretizado'].fillna(value="desconocido")
dat=dat.drop(['ph'],axis=1)
dat['Sulfate_d'] = pd.qcut(dat['Sulfate'], q=10)
dat['Sulfate_d']=dat['Sulfate_d'].cat.add_categories("desconocido")
dat['Sulfate_d']=dat['Sulfate_d'].fillna(value="desconocido")
dat=dat.drop(['Sulfate'],axis=1)
dat['Trihalomethanes_d'] = pd.qcut(dat['Trihalomethanes'], q=10)
dat['Trihalomethanes_d']=dat['Trihalomethanes_d'].cat.add_categories("desconocido")
dat['Trihalomethanes_d']=dat['Trihalomethanes_d'].fillna(value="desconocido")
dat=dat.drop(['Trihalomethanes'],axis=1)

dat2=pd.get_dummies(dat)
dat2_x = dat2.drop('Potability', axis=1)
dat2_y = dat2['Potability']

x_train, x_test, y_train, y_test = train_test_split(dat2_x, dat2_y, test_size=0.2)
# Creamos 1000 decision trees
rf = RandomForestClassifier(n_estimators = 1000, random_state = 99)
rf.fit(x_train, y_train)
# Guardar el modelo
with open('src/models/Apis/modelos/rf.pkl', 'wb') as handle:
    pickle.dump(rf, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Guardamos las columnas x (sin Potability)
with open('src/models/Apis/modelos/categories_ohe.pickle', 'wb') as handle:
    pickle.dump(dat2_x.columns, handle, protocol=pickle.HIGHEST_PROTOCOL)