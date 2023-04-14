import pandas as pd
from funpymodeling.exploratory import freq_tbl, status

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

data1['comuna']=data1['comuna'].astype(str)
data1['nhogar']=data1['nhogar'].astype(str)
data1['años_escolaridad']=data1['años_escolaridad'].replace("Ningun año de escolaridad aprobado", '0')
data1['años_escolaridad']=data1['años_escolaridad'].astype(float).astype("Int32")
años_esc=pd.cut(data1['años_escolaridad'], q=5, duplicates='drop')