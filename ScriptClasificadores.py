#Script de clasificadores

#===============================================================================================================================

#Importación de librerias

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from joblib import dump
from imblearn.over_sampling import RandomOverSampler
import matplotlib.pyplot as plt

#Importación de datasets

teams = pd.read_csv("teams_csv.csv")
matches = pd.read_csv("matches_csv.csv")

#Tratar los datos para el Clasificador

matches['Resultado'] = matches['Resultado'].astype('category')
matches['+ 2.5 Goles'] = matches['+ 2.5 Goles'].astype('category')
print(matches['Resultado'].value_counts())
print(matches['+ 2.5 Goles'].value_counts())
matches['Resultado'] = matches['Resultado'].cat.codes
matches['+ 2.5 Goles'] = matches['+ 2.5 Goles'].cat.codes
print(matches['Resultado'].value_counts())
print(matches['+ 2.5 Goles'].value_counts())
X = matches.drop(['HomeTeam','AwayTeam','Resultado', '+ 2.5 Goles'],axis=1)
yResultados = matches['Resultado']
yGoles = matches['+ 2.5 Goles']

#Especificar Temporadas

XResultados_train = X.iloc[0:1139]
yResultados_train = yResultados.iloc[0:1139]
XResultados_test = X.iloc[1140:1519]
yResultados_test = yResultados.iloc[1140:1519]
XGoles_train = X.iloc[0:1139]
yGoles_train = yGoles.iloc[0:1139]
XGoles_test = X.iloc[1140:1519]
yGoles_test = yGoles.iloc[1140:1519]

#Cogemos muestras aleatorias para entrenar y predecir

XResultados_train, XResultados_test, yResultados_train, yResultados_test = train_test_split(X, yResultados, test_size=0.3, random_state=1, stratify=yResultados)
XGoles_train, XGoles_test, yGoles_train, yGoles_test = train_test_split(X, yGoles, test_size=0.3, random_state=1, stratify=yGoles)

#Sobremuestreamos Resultados y Goles para igualar

sm = RandomOverSampler(sampling_strategy='not majority', random_state = 33)
XResultados_resampled, yResultados_resampled = sm.fit_resample(X, yResultados)
XGoles_resampled, yGoles_resampled = sm.fit_resample(X, yGoles)

#Cogemos muestras aleatoria para entrenar y predecir (sobremuestreado)

XResultados_train, XResultados_test, yResultados_train, yResultados_test = train_test_split(XResultados_resampled, yResultados_resampled, test_size=0.3, random_state=1, stratify=yResultados_resampled)
XGoles_train, XGoles_test, yGoles_train, yGoles_test = train_test_split(XGoles_resampled, yGoles_resampled, test_size=0.3, random_state=1, stratify=yGoles_resampled)

#===============================================================================================================================

#Inicialización de clasificadores para comparar

names = ["KNN5", "KNN7","KNN9","KNN11","KNN13","KNN17","KNN84","Decision Tree 4", "Decision Tree 8", "Decision Tree 16","GNB"]
classifiers = [
    KNeighborsClassifier(metric='minkowski', n_neighbors=5),
    KNeighborsClassifier(metric='minkowski', n_neighbors=7),
    KNeighborsClassifier(metric='minkowski', n_neighbors=9),
    KNeighborsClassifier(metric='minkowski', n_neighbors=11),
    KNeighborsClassifier(metric='minkowski', n_neighbors=13),
    KNeighborsClassifier(metric='minkowski', n_neighbors=17),
    KNeighborsClassifier(metric='minkowski', n_neighbors=84),
    DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=1),
    DecisionTreeClassifier(criterion='entropy', max_depth=8, random_state=1),
    DecisionTreeClassifier(criterion='entropy', max_depth=16, random_state=1),
    GaussianNB()]
   #SVC(kernel="linear") ]
#Añadir clasificador arriba si se descomenta!!!
#No hemos comparado mas clasificadores porque no computa comentar en informe

#==============================================================================================================================

#Prueba de los diferentes clasificadores y muestra de resultados 

accuracy = dict()
for name, clf in zip(names, classifiers):
    clf.fit(XResultados_train, yResultados_train)
    score = clf.score(XResultados_test, yResultados_test)
    yResultados_pred = clf.predict(XResultados_test)
    accuracy[name] = score.mean()
    print(name)
    print("Accuracy (Resultados): %0.4f " % score.mean())
    cmResultados=confusion_matrix(yResultados_test, yResultados_pred)
    print("Matriz de Confusión (Resultados):")
    print(cmResultados)
    clf.fit(XGoles_train, yGoles_train)
    score = clf.score(XGoles_test, yGoles_test)
    yGoles_pred = clf.predict(XGoles_test)
    accuracy[name] = score.mean()
    print(" Accuracy (Goles): %0.4f " % score.mean())
    cmGoles=confusion_matrix(yGoles_test, yGoles_pred)
    print("Matriz de Confusión (Goles):")
    print(cmGoles)
    
#Clasificador escogido
clfResultados = KNeighborsClassifier(metric='minkowski', n_neighbors=5) 
clfResultados.fit(XResultados_train, yResultados_train)
yResultados_pred = clfResultados.predict(XResultados_test)
cmResultados=confusion_matrix(yResultados_test, yResultados_pred)
print(cmResultados)
fig= plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(cmResultados)
plt.title('Confusion Matrix Resultados')
fig.colorbar(cax)
labels=['victoriaV','empate','victoriaL']
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

clfGoles = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=1)
clfGoles.fit(XGoles_train, yGoles_train)
yGoles_pred = clfGoles.predict(XGoles_test)
cmGoles=confusion_matrix(yGoles_test, yGoles_pred)
print(cmGoles)
fig= plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(cmGoles)
plt.title('Confusion Matrix Goles')
fig.colorbar(cax)
labels=['-2.5 Goles','+2.5 Goles']
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

dump(clfResultados, 'ClassificatorResultados.joblib') 
dump(clfGoles, 'ClassificatorGoles.joblib') 
