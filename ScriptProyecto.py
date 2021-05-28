#Script del Proyecto Final

#===============================================================================================================================
#Importación de librerias

import pandas as pd
from  joblib import load
import warnings
warnings.filterwarnings('ignore')


#Importación del dataset

teams = pd.read_csv("teams_csv.csv")
clfResultados = load('ClassificatorResultados.joblib') 
clfGoles = load('ClassificatorGoles.joblib') 
#EQUIPOS: Alaves, Ath Bilbao, Ath Madrid, Barcelona, Betis, Celta,  Eibar, Espanol, 
#Getafe, Girona, Granada, Huesca, La Coruna, Las Palmas, Leganes, Levante, Malaga, Osasuna, Real Madrid 
#Sevilla, Sociedad, Sp Gijon, Valencia, Valladolid, Vallecano, Villarreal (26 equipos)

#ESCRIBE EL NOMBRE DE LOS EQUIPOS DEL PARTIDO (TIENE QUE SER UNO DE LOS 26 ANTERIORES)
equipolocal = input("Equipo local: ")
equipovisitante = input("Equipo visitante: ")

#FORMACIÓN DEL DATASET PARA ENVIAR AL CLASIFICADOR
is_teamHome = teams.loc[:, 'Equipos'] == equipolocal
is_teamAway = teams.loc[:, 'Equipos'] == equipovisitante
estadisticasLocal = teams.loc[is_teamHome]
estadisticasVisitante = teams.loc[is_teamAway]
estadisticasLocal["indice"]=0
estadisticasVisitante["indice"]=0
partido = estadisticasLocal.merge(estadisticasVisitante, left_on='indice', right_on='indice', suffixes=('L', 'V'))
partido = partido.drop(columns=["EquiposL", "EquiposV", "indice"])
y_predResultado = clfResultados.predict(partido)
y_predGoles = clfGoles.predict(partido)
y_probResultados = clfResultados.predict_proba(partido)
y_probGoles = clfGoles.predict_proba(partido)

print("Probabilidad victoria equipo local: %0.2f" % (y_probResultados[0, 2]*100), "%")
print("Probabilidad empate: %0.2f " % (y_probResultados[0, 1]*100), "%")
print("Probabilidad victoria equipo visitante: %0.2f " % (y_probResultados[0, 0]*100), "%")
print("Predicción Programa:")

if y_predResultado == 0:
    print("Ganará el equipo visitante")
    
elif y_predResultado == 1:
    print("Quedarán empate")
     
else:
    print("Ganará el equipo local")

print("")
print("Probabilidad -2.5 Goles: %0.2f" % (y_probGoles[0,0]*100), "%")
print("Probabilidad +2.5 Goles: %0.2f" % (y_probGoles[0,1]*100), "%")
print("Predicción Programa:")
if y_predGoles == 0:
    print("No llegarán a 2.5 Goles")
     
else:
    print("Llegarán a 2.5 Goles")
