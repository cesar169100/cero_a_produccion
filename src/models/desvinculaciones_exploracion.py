import pandas as pd
import matplotlib.pyplot as plt


dat=pd.read_csv("/Users/Cesar.deAlba/Desktop/Cursos/cero_a_produccion/materiales/desvinculaciones.csv", encoding = "ISO-8859-1")
dat.dtypes
dat['Nombre']=dat['Nombre'].astype(str)
dat['Apellido']=dat['Apellido'].astype(str)
dat['Area']=dat['Area'].astype(str)
dat['Fecha comienzo']= pd.to_datetime(dat['Fecha comienzo'], format="%m/%d/%Y")
dat['Fecha fin']= pd.to_datetime(dat['Fecha fin'], format="%m/%d/%Y")
dat['Nivel']=dat['Nivel'].astype(str)
dat['Grupo recruitment']=dat['Grupo recruitment'].astype(str)
dat['Rango Salarial']=dat['Rango Salarial'].astype(str)
dat['RS competencia']=dat['RS competencia'].astype(str)
dat['Realizo Cursos']=dat['Realizo Cursos'].astype(str)

dat['Grupo recruitment'] = dat['Grupo recruitment'].str.replace('Grupo ', '')
dat['Rango Salarial'] = dat['Rango Salarial'].str.replace('Rango ', '')
dat['Rango Salarial'] = dat['Rango Salarial'].astype(int)
dat['RS competencia'] = dat['RS competencia'].str.replace('Rango ', '')
dat['RS competencia'] = dat['RS competencia'].astype(int)
dat['Realizo Cursos'][dat['Realizo Cursos']=='NO']=0
dat['Realizo Cursos'][dat['Realizo Cursos']=='SI']=1
dat['duracion_dias']=(dat['Fecha fin']-dat['Fecha comienzo']).dt.days
dat['duracion_anios']=dat['duracion_dias']/365
dat['incremento']=0
dat['incremento'][dat['Rango Salarial']<dat['RS competencia']]=1

## No hay incrementos
plt.style.use('ggplot')
plt.hist(dat['incremento'])
plt.title('Incrementos')
plt.show()
## Da igual si realizó o no cursos
dat.groupby('Realizo Cursos')['incremento'].sum()
## No tiene que ver con grupo reclutamiento o nivel
dat[['Nivel','Grupo recruitment','Tiempo recruitment','incremento']]
## Ni antiguedad o manager
dat[['Area','Manager','duracion_anios','incremento']]
## Meses en los que se van (Diciembre)
dat['mes']=dat['Fecha fin'].dt.month
plt.style.use('ggplot')
plt.hist(dat['mes'])
plt.title('Meses para irse')
plt.show()
###################################### -- Rangos-- ######################################################################
rangos=pd.read_csv("/Users/Cesar.deAlba/Desktop/Cursos/cero_a_produccion/materiales/rangos.csv", encoding = "ISO-8859-1")
rangos.dtypes
###################################### -- Managers-- ######################################################################
managers=pd.read_csv("/Users/Cesar.deAlba/Desktop/Cursos/cero_a_produccion/materiales/managers.csv", encoding = "ISO-8859-1")
