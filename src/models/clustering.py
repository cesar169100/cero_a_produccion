import pandas as pd
from funpymodeling.exploratory import freq_tbl, status, cat_vars
import matplotlib.pyplot as plt 
from ydata_profiling import ProfileReport
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data=pd.read_csv("/Users/Cesar.deAlba/Desktop/Cursos/cero_a_produccion/materiales/aw_fb_clusters.csv", sep=',')
data.head(5)
data=data.drop(['X1'], axis=1)
status(data)
data.hist(figsize = (15,20))
plt.show()
# Variables categóricas. Los métodos de cluster usados aquí solo admiten numéricas
cat_vars(data)
data=data.drop(cat_vars(data), axis=1)
#ProfileReport(data, minimal=True) #Ver si solo funciona en jupyter
## Estandarización de media y varianza
std_scaler = StandardScaler()
std_scaler.fit(data)
data_norm=std_scaler.transform(data)

######################### --kMEANS

cl_model = KMeans(
    n_clusters=3,     # el parámetro importante!
    init='k-means++', # k-means++ acelera la convergencia, respecto de random
    max_iter=100, 
    random_state=0,
    n_init='auto'     # Para evitar warnings más adelante
)

cl_model.fit(data_norm)
pred_cl = cl_model.predict(data_norm)
#  Número de cluster: 
pred_cl