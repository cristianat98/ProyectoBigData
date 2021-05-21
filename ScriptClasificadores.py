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
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import BaggingClassifier
from joblib import dump, load
import numpy as np
import pandas as pd
import seaborn as sns
from imblearn.over_sampling import RandomOverSampler
import matplotlib.pyplot as plt

#Importación de datasets

teams = pd.read_csv("teams_csv.csv")
matches = pd.read_csv("matches_csv.csv")

matches['Resultado'] = matches['Resultado'].astype('category')
print(matches['Resultado'].value_counts())
matches['Resultado'] = matches['Resultado'].cat.codes
print(matches['Resultado'].value_counts())


X = matches.drop(['HomeTeam','AwayTeam','Resultado'],axis=1)
y = matches['Resultado']


sm = RandomOverSampler(sampling_strategy='not majority', random_state = 33)
X_resampled, y_resampled = sm.fit_resample(X, y)
print(len(X_resampled), len(y_resampled))

print('Class labels:', np.unique(y_resampled))
print('Labels counts in y_resampled:', np.bincount(y_resampled))

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=1, stratify=y_resampled)
#knn_model = KNeighborsClassifier(metric='minkowski', n_neighbors=5)
#knn_model.fit(X_train, y_train)

#
# test prediction
#y_pred = knn_model.predict(X_test)
#print('Misclassified samples: %d' % (y_test != y_pred).sum())
#print('Accuracy: %.2f%%' % (100.0 * knn_model.score(X_test, y_test)))

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
    #   One metric: score (accuracy)
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    accuracy[name] = score.mean()
    print(name)
    print(" Accuracy: %0.4f " % score.mean())
    
clf = KNeighborsClassifier(metric='minkowski', n_neighbors=5) 
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
cm=confusion_matrix(y_test, y_pred)
print(confusion_matrix(y_test, y_pred))
cm=confusion_matrix(y_test, y_pred)
fig= plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(cm)
plt.title('Confusion matrix')
fig.colorbar(cax)
labels=['victoriaL','victoriaV','empate']
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()


dump(clf, 'Classificator.joblib') 
