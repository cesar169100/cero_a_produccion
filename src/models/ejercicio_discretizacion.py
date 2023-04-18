import pandas as pd
from funpymodeling.exploratory import freq_tbl, status
from sklearn.model_selection import train_test_split 
import pickle

# Para este caso nos interesa visualizar todas las columnas
pd.set_option('display.max_columns', None)
data = pd.read_csv("/Users/Cesar.deAlba/Desktop/Cursos/cero_a_produccion/materiales/encuesta_anual_hogares2019.csv", sep=',')
status(data)
data=data.drop(['id','hijos_nacidos_vivos'],axis=1)

## Discretizacion
data1=data.copy()
# Divide la data en intervalos dados por sus cuantiles, determinados por q.
# Cuando hace los intervalos, si hay muchos repetidos, los cuantiles se pueden repetir dando origen a 
# intervalos sin sentido. Por eso se usa drop.
ingresos=pd.qcut(data1['ingresos_familiares'], q=4, duplicates='drop')
ingresos_pc=pd.qcut(data1['ingreso_per_capita_familiar'], q=10, duplicates='drop')
ingreso_lab=pd.qcut(data1['ingreso_total_lab'], q=10, duplicates='drop')
ingreso_nolab=pd.qcut(data1['ingreso_total_no_lab'], q=4, duplicates='drop')
edad1=pd.cut(data1['edad'], bins=5)

data['comuna']=data['comuna'].astype(str)
data['nhogar']=data['nhogar'].astype(str)
data['años_escolaridad']=data['años_escolaridad'].replace("Ningun año de escolaridad aprobado", '0')
data['años_escolaridad']=data['años_escolaridad'].astype(float).astype("Int32")
años_esc=pd.cut(data1['años_escolaridad'], bins=5)

# Eliminar filas que contengan NAN, en las columnas especificadas
data=data.dropna(subset=['situacion_conyugal', 'sector_educativo', 'lugar_nacimiento', 'afiliacion_salud'])
data=data.reset_index(drop=True)
## Separar data set
data_tr, data_ts = train_test_split(data, test_size=0.2)
## Corte en el training
años_tr, saved_bins = pd.qcut(data_tr['años_escolaridad'],
                               q=5,
                               retbins=True) # importante!

# Usar los q guardados para discretizar el conjunto de test. ¿Porque no discretizar completo y luego separar?
años_test=pd.cut(data_ts['años_escolaridad'],bins=saved_bins,  include_lowest=True)
## En la práctica
status(data)
data['años_escolaridad']
data['años_escolaridad2'], saved_bins = pd.qcut(data['años_escolaridad'], q=5, retbins=True)
status(data['años_escolaridad2'])
data['años_escolaridad2']=data['años_escolaridad2'].cat.add_categories("desconocido")
data['años_escolaridad2']=data['años_escolaridad2'].fillna(value="desconocido")
data=data.drop(['años_escolaridad'],axis=1)
#data=data.fillna({'nivel_max_educativo':'desconocido'}, inplace=True)
#status(data['nivel_max_educativo'])
## One hot encoding
data2=pd.get_dummies(data)
status(data)
with open('categories_ohe.pickle', 'wb') as handle:
    pickle.dump(data2.columns, handle, protocol=pickle.HIGHEST_PROTOCOL)