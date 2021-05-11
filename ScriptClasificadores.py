#Script de clasificadores

#======================================================================
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

#=========================================================================