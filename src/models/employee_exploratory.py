import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from funpymodeling.exploratory import freq_tbl

dat=pd.read_csv("/Users/Cesar.deAlba/Desktop/Cursos/cero_a_produccion/materiales/employee.csv")

##Objetivo
#Realizar un análisis exploratorio de datos para el área de Recursos Humanos. 
#Prácticamente vas a hacer lo que se le conoce como People Analytics.

##AED 1
#Para el punto 4) de variables categóricas, analicen la columna `EducationField`
#Para el Análisis cuantitativo de variables categóricas, analicen `MaritalStatus`
#Con respecto a la consulta por query, consideren `t_country.query("frequency<=500")['MaritalStatus']`

dat.hist(figsize = (10,10))
dat.plot.hist(bins=12, alpha=0.5)
plt.show() 
dat.describe().T  
sns.countplot(y='EducationField', data=dat)
plt.show() 
sns.countplot(y=dat['EducationField'], order = dat['EducationField'].value_counts().index)
plt.show()
freq_tbl(dat['MaritalStatus'])
t_country=freq_tbl(dat.MaritalStatus)
t_country.query("frequency<=500")['MaritalStatus']

##AED 2*
#Para el punto 1) Análisis de variables categóricas, consideren la columna `BusinessTravel`
#En 2.A) Análisis de categórica vs. categórica, consideren `BusinessTravel` vrs. `MaritalStatus`. También analicen `Gender` vrs. `Department`
#En 2.B) Análisis de numérica vs. categórica, consideren `Gender` vrs. `JobSatisfaction`
#Para el Promedio de todas las variables, nuestra variable a predecir es `Gender`
#En 2.C) Análisis de numérica vs. numérica `JobLevel` vrs. `StockOptionLevel`
#Para el Promedio de todas las variables, nuestra variable a predecir es `Age`
#Para todos los puntos 3) consideren `JobSatisfaction` vrs. `Gender`

freq_tbl(dat['BusinessTravel'])
pd.crosstab(dat.BusinessTravel, dat.MaritalStatus, margins=True)
pd.crosstab(dat.BusinessTravel, dat.MaritalStatus, normalize=True)
pd.crosstab(dat.Gender, dat.Department, margins=True)
pd.crosstab(dat.Gender, dat.Department, normalize=True)
dat.groupby('Gender')['JobSatisfaction'].mean().sort_values(ascending=False)
dat.groupby('Gender')['JobSatisfaction'].describe()
dat.groupby('Gender').mean()
dat.groupby('JobLevel')['StockOptionLevel'].mean().sort_values(ascending=False)
dat.groupby('Age').mean()

sns.boxplot(y = 'JobSatisfaction', x = 'Gender', data = dat)
plt.show()
sns.violinplot(y = 'JobSatisfaction', x = 'Gender', data = dat)
plt.show()
g = sns.catplot(x="JobSatisfaction",
                col="Gender",
                data= dat,
                kind="count")
plt.show()
sns.pairplot(dat)
plt.show()

##Correlación
#Para 4) One hot encoding analicen que pasa con `data_test[['MaritalStatus_Divorced', 'MaritalStatus_Married', 'MaritalStatus_Single']]`

dat2=pd.get_dummies(dat, dummy_na=True)
dat2[['MaritalStatus_Divorced', 'MaritalStatus_Married', 'MaritalStatus_Single']]
dat2[dat2['MaritalStatus_Divorced']==1]
plt.figure(figsize=(10,5))
sns.heatmap(dat.corr(), cmap='coolwarm')
plt.show()
### Conclusiones/Insigths
# Las ciencias son el principal campo de estudio.
# Los casados viajan más que los solteros, esperaba lo contrario.
# Más hombres que mujeres en recursos humanos, esperaba lo contrario.
# Buen número de mujeres en Desarrollo e investigación.
# Las mujeres suelen durar más en su mismo puesto.
# Conforme aumenta la edad se tiende a permanecer en el rol. Suponemos que porque ya se llegó a un buen nivel.
# Alta correlación entre las variables referentes al tiempo de permanencia en la empresa.
