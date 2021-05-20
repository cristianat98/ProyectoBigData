#Script del Proyecto Final

#===============================================================================================================================
#Importación de librerias

import pandas as pd


#Importación del dataset

teams = pd.read_csv("teams_csv.csv")

#EQUIPOS: ALAVÉS, ATH BILBAO, ATL MADRID, BARCELONA, BETIS, CELTA, DEPORTIVO, EIBAR, ESPAÑOL, 
#GETAFE, GIRONA, GRANADA, HUESCA, LAS PALMAS, LEGANÉS, LEVANTE, MÁLAGA, OSASUNA, VALLECANO, MADRID, REAL SOCIEDAD, 
#SEVILLA, SPORTING, VALENCIA, VALLADOLID, VILLARREAL (26 equipos)

#ESCRIBE EL NOMBRE DE LOS EQUIPOS DEL PARTIDO (TIENE QUE SER UNO DE LOS 26 ANTERIORES)
equipolocal = "Alaves"
equipovisitante = "Barcelona"

#FORMACIÓN DEL DATASET PARA ENVIAR AL CLASIFICADOR
is_teamHome = teams.loc[:, 'Equipos'] == equipolocal
is_teamAway = teams.loc[:, 'Equipos'] == equipovisitante
estadisticasLocal = teams.loc[is_teamHome]
estadisticasVisitante = teams.loc[is_teamAway]
estadisticasLocal["indice"]=0
estadisticasVisitante["indice"]=0
partido = estadisticasLocal.merge(estadisticasVisitante, left_on='indice', right_on='indice', suffixes=('L', 'V'))
partido = partido.drop(columns=["EquiposL", "EquiposV", "indice"])
