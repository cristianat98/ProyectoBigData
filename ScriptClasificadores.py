#Script de clasificadores

#===============================================================================================================================
#Importación de librerias

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.ensemble import BaggingClassifier


#Importación de datasets

teams = pd.read_csv("teams_csv.csv")
matches = pd.read_csv("matches_csv.csv")

matches['Resultado'] = matches['Resultado'].astype('category')
matches['Resultado'] = matches['Resultado'].cat.codes


X = matches.drop(['HomeTeam','AwayTeam','Resultado'],axis=1)
y = matches['Resultado']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
X_train = X.iloc[0:1139]
y_train = y.iloc[0:1139]
X_test = X.iloc[1140:1519]
y_test = y.iloc[1140:1519]

#knn_model = KNeighborsClassifier(metric='minkowski', n_neighbors=5)
#knn_model.fit(X_train, y_train)

#
# test prediction
#y_pred = knn_model.predict(X_test)
#print('Misclassified samples: %d' % (y_test != y_pred).sum())
#print('Accuracy: %.2f%%' % (100.0 * knn_model.score(X_test, y_test)))

#===============================================================================================================================

#Inicialización de clasificadores para comparar
names = ["KNN5", "KNN10", "Decision Tree 8", "Decision Tree 16", "GNB", "SVC Linear", "SVC Polynomial", "Neural Net"]
classifiers = [
    KNeighborsClassifier(metric='minkowski', n_neighbors=5),
    KNeighborsClassifier(metric='minkowski', n_neighbors=10),
    DecisionTreeClassifier(criterion='entropy', max_depth=8, random_state=1),
    DecisionTreeClassifier(criterion='entropy', max_depth=16, random_state=1),
    GaussianNB(),
    #SVC(kernel="linear"),
    #SVC(kernel="poly", gamma=0.20, C=1.0),

#==============================================================================================================================

#Prueba de los diferentes clasificadores y muestra de resultados 

accuracy = dict()
for name, clf in zip(names, classifiers):
    #   One metric: score (accuracy)
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    accuracy[name] = score.mean()
    print(name)
    print(" Accuracy: %0.4f " % score.mean())
