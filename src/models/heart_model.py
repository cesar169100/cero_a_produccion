import pandas as pd
import numpy as np
from funpymodeling.exploratory import status
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
import optuna

dat=pd.read_csv("/Users/Cesar.deAlba/Desktop/Cursos/cero_a_produccion/materiales/heart.csv", encoding = "ISO-8859-1")
status(dat)
class_map = {'No':0, 'Yes':1}
class_map2 = {'Female':0, 'Male':1}
dat['HeartDisease'] = dat['HeartDisease'].map(class_map)
dat['Smoking'] = dat['Smoking'].map(class_map)
dat['Sex'] = dat['Sex'].map(class_map2)
dat['AlcoholDrinking'] = dat['AlcoholDrinking'].map(class_map)
dat['Stroke'] = dat['Stroke'].map(class_map)
dat['DiffWalking'] = dat['DiffWalking'].map(class_map)
dat['Diabetic'] = dat['Diabetic'].map(class_map)
dat['PhysicalActivity'] = dat['PhysicalActivity'].map(class_map)
dat['Asthma'] = dat['Asthma'].map(class_map)
dat['KidneyDisease'] = dat['KidneyDisease'].map(class_map)
dat['SkinCancer'] = dat['SkinCancer'].map(class_map)

dat=dat.drop(['AgeCategory','GenHealth','Race','Diabetic'], axis=1)


x_dat=dat.drop('HeartDisease', axis=1)
y_dat=dat['HeartDisease']

x_train, x_test, y_train, y_test = train_test_split(x_dat, y_dat, test_size=0.2)
print(x_train.shape, y_train.shape)

############################################ Creamos 100 decision trees
rf = RandomForestClassifier()
rf.fit(x_train, y_train)

## Predicciones
# En training
pred_tr=rf.predict(x_train)
# En testing
pred_ts=rf.predict(x_test)

### Data frame realidad vs predicho
df_val_tr=pd.DataFrame({'y_train':y_train, 'pred_tr':pred_tr})
# ¿cuántos aciertos?
sum(df_val_tr.y_train==df_val_tr.pred_tr)/len(df_val_tr)
accuracy_score(df_val_tr.y_train, df_val_tr.pred_tr, normalize=True)

## Testing realidad vs predicho
df_val_ts=pd.DataFrame({'y_test':y_test, 'pred_ts':pred_ts})
# ¿cuántos aciertos?
accuracy_score(df_val_ts.y_test, df_val_ts.pred_ts, normalize=True)

############################### Creamos 500 decision trees #####################################
rf_1 = RandomForestClassifier(n_estimators=500, n_jobs=-1)
rf_1.fit(x_train, y_train)
# En testing
pred_test=rf_1.predict(x_test)
df_val_test=pd.DataFrame({'y_test':y_test, 'pred_test':pred_test})
accuracy_score(df_val_test.y_test, df_val_test.pred_test, normalize=True)
f1_score(df_val_test.y_test, df_val_test.pred_test)

############################### Tunning ##########################################################
def objective(trial):
      n_estimators=trial.suggest_int("n_estimators", 2, 600, step=50)
      max_depth = trial.suggest_int("max_depth", 3, 12, step=1)
      clf = RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth)
      return cross_val_score(clf, x_train, y_train, scoring="f1", n_jobs=-1, cv=10).mean()


study = optuna.create_study(direction='maximize')
#func = lambda trial: objective(trial)
study.optimize(objective, n_trials=3) 
f=study.best_value
params=np.array(list(study.best_params.values()))
n_estimators=params[0].astype(int)
max_depth = params[1].astype(int)

rf2=RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth, n_jobs=-1)
rf2.fit(x_train, y_train)
# En testing
pred_test=rf2.predict(x_test)
df_val_test=pd.DataFrame({'y_test':y_test, 'pred_test':pred_test})
accuracy_score(df_val_test.y_test, df_val_test.pred_test, normalize=True)
f1_score(df_val_test.y_test, df_val_test.pred_test)         