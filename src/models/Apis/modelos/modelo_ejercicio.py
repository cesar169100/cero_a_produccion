import pandas as pd
from funpymodeling.exploratory import status

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