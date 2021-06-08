# =============================================================================
# CREAR COLUMNAS
#
# teams["GMC"]= 0
# teams["GRC"]= 0
# ...
#
# =============================================================================

# =============================================================================
# ESTADÍSTICAS
# 
# GMC: Goles Marcados en Casa
# GRC: Goles Recibidos en Casa
# GMF: Goles Marcados Fuera
# GRF: Goles Recibidos Fuera
# GMT: Goles Marcados Totales
# GRT: Goles Recibidos Totales
# GMCPP: Goles Marcados en Casa Por Partido
# GRCPP: Goles Recibidos en Casa Por Partido
# GMFPP: Goles Marcados Fuera Por Partido
# GRFPP: Goles Recibidos Fuera Por Partido
# GMTPP: Goles Marcados Totales Por Partido
# GRTPP: Goles Recibidos Totales Por Partido
# VC: Victorias en Casa
# VF: Victorias Fuera
# VT: Victorias Totales
# EC: Empates en Casa
# EF: Empates Fuera
# ET: Empates Totales
# DC: Derrotas en Casa
# DF: Derrotas Fuera
# DT: Derrotas Totales
# PTC: Partidos Totales en Casa
# PTF: Partidos Totales Fuera
# PT: Partidos Totales
# RCPP: Remates en Casa Por Partido
# RRCPP: Remates Recibidos en Casa Por Partido
# RFPP: Remates Fuera Por Partido
# RRFPP: Remates Recibidos Fuera Por Partido
# RPP: Remates Por Partido
# RRPP: Remates Recibidos Por Partido
# RPCPP: Remates a Puerta en Casa Por Partido
# RPRCPP: Remates a Puerta Recibidos en Casa Por Partido
# RPFPP: Remates a Puerta Fuera Por Partido
# RPRFPP: Remates a Puerta Recibidos Fuera Por Partido
# RPPP: Remates a Puerta Por Partido
# RRPPP: Remates Recibidos a Puerta Por Partido
# CCPP: Córners en Casa Por Partido
# CRCPP: Córners Recibidos en Casa Por Partido
# CFPP: Córners Fuera Por Partido
# CRFPP: Córners Recibidos Fuera Por Partido
# CPP: Córners Por Partido
# CRPP: Córners Recibidos Por Partido
#
# =============================================================================

import pandas as pd


#Importar Tablas de Datos
season1516 = pd.read_csv("season-1516_csv.csv")
season1617 = pd.read_csv("season-1617_csv.csv")
season1718 = pd.read_csv("season-1718_csv.csv")
season1819 = pd.read_csv("season-1819_csv.csv")
teams = pd.read_csv("teams_csv.csv")
matches = pd.read_csv("matches_csv.csv")
seasons = pd.concat([season1516, season1617, season1718, season1819, season1819], ignore_index=True)
partidos = pd.concat([season1516, season1617, season1718, season1819], ignore_index=True)

#Datos Para Resultados
print("Cuota media Victoria Local: %0.2f " % partidos['B365H'].mean())
print(partidos['B365H'].sort_values(ascending=False))
print("Cuota media Empate: %0.2f " % partidos['B365D'].mean())
print(partidos['B365D'].sort_values(ascending=False))
print("Cuota media Victoria Visitante: %0.2f " % partidos['B365A'].mean())
print(partidos['B365A'].sort_values(ascending=False))
print("Cuota media -2.5 Goles: %0.2f " % partidos['BbAv<2.5'].mean())
print(partidos['BbAv<2.5'].sort_values(ascending=False))
print("Cuota media +2.5 Goles: %0.2f " % partidos['BbAv>2.5'].mean())
print(partidos['BbAv>2.5'].sort_values(ascending=False))

#EQUIPOS: ALAVÉS, ATH BILBAO, ATL MADRID, BARCELONA, BETIS, CELTA, DEPORTIVO, EIBAR, ESPAÑOL, 
#GETAFE, GIRONA, GRANADA, HUESCA, LAS PALMAS, LEGANÉS, LEVANTE, MÁLAGA, OSASUNA, VALLECANO, MADRID, REAL SOCIEDAD, 
#SEVILLA, SPORTING, VALENCIA, VALLADOLID, VILLARREAL (26 equipos)

equipos = ['Alaves', 'Ath Bilbao', 'Ath Madrid', 'Barcelona', 'Betis', 'Celta', 'Eibar', 'Espanol', 'Getafe', 'Girona', 'Granada', 'Huesca', 'La Coruna', 'Las Palmas', 'Leganes', 'Levante', 'Malaga', 'Osasuna', 'Real Madrid', 'Sevilla', 'Sociedad', 'Sp Gijon', 'Valencia', 'Valladolid', 'Vallecano', 'Villarreal']

# =============================================================================
# CREACIÓN DEL DATASET EQUIPOS
#
# teams = pd.DataFrame(equipos, columns=['Equipos'])
#
# =============================================================================

# =============================================================================
#CONCATENAR LOS DATASETS DE ESTADÍSTICAS Y PARTIDOS
#
# matches = pd.DataFrame()
# matches["HomeTeam"] = partidos["HomeTeam"]
# matches["AwayTeam"] = partidos["AwayTeam"]
# matches["Resultado"] = partidos["FTR"]
# matches["indice"]= matches.index
# matches = pd.merge(matches, teams, left_on="HomeTeam", right_on="Equipos", left_index=True)
# matches = pd.merge(matches, teams, left_on="AwayTeam", right_on="Equipos", suffixes=('L', 'V'), left_index=True)
# matches = matches.set_index(matches["indice"])
# matches = matches.sort_index()
# matches = matches.drop(columns=["EquiposL", "EquiposV"])
# matches = matches.drop(columns=["indice"])
#
# =============================================================================

#Incluir la columna + 2,5 Goles (Apuesta clásica en Casas de Apuestas)
matches["+ 2.5 Goles"]=""
i = 0
while i<len(matches):
    golestotales=partidos.loc[i,"FTHG"]+partidos.loc[i,"FTAG"]
    if golestotales>2:
        matches.loc[i,"+ 2.5 Goles"] = "SÍ"
    else:
        matches.loc[i,"+ 2.5 Goles"] = "NO"
    i=i+1
    
    
#BUSCAR TODOS LOS PARTIDOS DE UN EQUIPO, SUMAR TODAS SUS ESTADÍSTICAS Y GUARDARLA EN EL DATASET CON LA SUMA TOTAL Y LA MEDIA
i=0
for equipo in equipos:
    is_teamHome = seasons.loc[:, 'HomeTeam'] == equipo
    is_teamAway = seasons.loc[:, 'AwayTeam'] == equipo
    matchsHome_team = seasons.loc[is_teamHome]
    matchsAway_team = seasons.loc[is_teamAway]
    
# =============================================================================
#     ESTADÍSTICAS DE GOLES
#
#     GMC = matchsHome_team['FTHG'].sum()
#     GRC = matchsHome_team['FTAG'].sum()
#     GMF = matchsAway_team['FTAG'].sum()
#     GRF = matchsAway_team['FTHG'].sum()
#     GMT = GMC + GMF
#     GRT = GRC + GRF
#     teams.loc[i, "GMC"] = GMC
#     teams.loc[i, "GRC"] = GRC
#     teams.loc[i, "GMF"] = GMF
#     teams.loc[i, "GRF"] = GRF
#     teams.loc[i, "GMT"] = GMT
#     teams.loc[i, "GRT"] = GRT
#     teams.loc[i, "GMCPP"] = GMC/(2*len(matchsAway_team))
#     teams.loc[i, "GRCPP"] = GRC/(2*len(matchsAway_team))
#     teams.loc[i, "GMFPP"] = GMF/(2*len(matchsAway_team))
#     teams.loc[i, "GRFPP"] = GRF/(2*len(matchsAway_team))
#     teams.loc[i, "GMTPP"] = GMT/(2*len(matchsAway_team))
#     teams.loc[i, "GRTPP"] = GRT/(2*len(matchsAway_team))
#
# =============================================================================

# =============================================================================
#     ESTADÍSTICAS DE RESULTADOS
#
#     victoriasCasa = matchsHome_team.loc[:, 'FTR'] == 'H'
#     victoriasFuera = matchsAway_team.loc[:, 'FTR'] == 'A'
#     empatesCasa = matchsHome_team.loc[:, 'FTR'] == 'D'
#     empatesFuera = matchsAway_team.loc[:, 'FTR'] == 'D'
#     derrotasCasa = matchsHome_team.loc[:, 'FTR'] == 'A'
#     derrotasFuera = matchsAway_team.loc[:, 'FTR'] == 'H'
#     victoriesHome_team = matchsHome_team.loc[victoriasCasa]
#     victoriesAway_team = matchsAway_team.loc[victoriasFuera]
#     drawHome_team = matchsHome_team.loc[empatesCasa]
#     drawAway_team = matchsAway_team.loc[empatesFuera]
#     losesHome_team = matchsHome_team.loc[derrotasCasa]
#     losesAway_team = matchsAway_team.loc[derrotasFuera]
#     
#     teams.loc[i, "VC"] = len(victoriesHome_team)
#     teams.loc[i, "VF"] = len(victoriesAway_team)
#     teams.loc[i, "VT"] = len(victoriesHome_team) + len(victoriesAway_team)
#     teams.loc[i, "EC"] = len(drawHome_team)
#     teams.loc[i, "EF"] = len(drawAway_team)
#     teams.loc[i, "ET"] = len(drawHome_team) + len(drawAway_team)
#     teams.loc[i, "DC"] = len(losesHome_team)
#     teams.loc[i, "DF"] = len(losesAway_team)
#     teams.loc[i, "DT"] = len(losesHome_team) + len(losesAway_team)
#     teams.loc[i, "PTC"] = len(matchsHome_team)
#     teams.loc[i, "PTF"] = len(matchsAway_team)
#     teams.loc[i, "PT"] = len(matchsHome_team) + len(matchsAway_team)
#
# =============================================================================

# =============================================================================
#     ESTADÍSTICAS REMATES
#
#     RCPP = matchsHome_team['HS'].sum()
#     RRCPP = matchsHome_team['AS'].sum()
#     RFPP = matchsAway_team['AS'].sum()
#     RRFPP = matchsAway_team['HS'].sum()
#     RPP = RCPP + RFPP
#     RRPP = RRCPP + RRFPP
#     RPCPP = matchsHome_team['HST'].sum()
#     RPRCPP = matchsHome_team['AST'].sum()
#     RPFPP = matchsAway_team['AST'].sum()
#     RPRFPP = matchsAway_team['HST'].sum()
#     RPPP = RPCPP + RPFPP
#     RRPPP = RPRCPP + RPRFPP
#     
#     teams.loc[i, "RCPP"] = RCPP/(len(matchsAway_team))
#     teams.loc[i, "RRCPP"] = RRCPP/(len(matchsAway_team))
#     teams.loc[i, "RFPP"] = RFPP/(len(matchsAway_team))
#     teams.loc[i, "RRFPP"] = RRFPP/(len(matchsAway_team))
#     teams.loc[i, "RPP"] = RPP/(2*len(matchsAway_team))
#     teams.loc[i, "RRPP"] = RRPP/(2*len(matchsAway_team))
#     teams.loc[i, "RPCPP"] = RPCPP/(len(matchsAway_team))
#     teams.loc[i, "RPRCPP"] = RPRCPP/(len(matchsAway_team))
#     teams.loc[i, "RPFPP"] = RPFPP/(len(matchsAway_team))
#     teams.loc[i, "RPRFPP"] = RPRFPP/(len(matchsAway_team))
#     teams.loc[i, "RPPP"] = RPPP/(2*len(matchsAway_team))
#     teams.loc[i, "RRPPP"] = RRPPP/(2*len(matchsAway_team))
#
# =============================================================================

# =============================================================================
#     ESTADÍSTICAS CÓRNERS
#
#     CCPP = matchsHome_team['HC'].sum()
#     CRCPP = matchsHome_team['AC'].sum()
#     CFPP = matchsAway_team['AC'].sum()
#     CRFPP = matchsAway_team['HC'].sum()
#     CPP = CCPP + CFPP
#     CRPP = CRCPP + CRFPP
#     
#     teams.loc[i, "CCPP"] = CCPP/(len(matchsAway_team))
#     teams.loc[i, "CRCPP"] = CRCPP/(len(matchsAway_team))
#     teams.loc[i, "CFPP"] = CFPP/(len(matchsAway_team))
#     teams.loc[i, "CRFPP"] = CRFPP/(len(matchsAway_team))
#     teams.loc[i, "CPP"] = CPP/(2*len(matchsAway_team))
#     teams.loc[i, "CRPP"] = CRPP/(2*len(matchsAway_team))
#
# =============================================================================
    
    i=i+1

teams.to_csv("teams_csv.csv", index = False)
matches.to_csv("matches_csv.csv", index = False)
