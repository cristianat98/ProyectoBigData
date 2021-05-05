import pandas as pd

# =============================================================================
# CREACIÓN DEL DATASET EQUIPOS
#
# teams = pd.DataFrame(equipos, columns=['Equipos'])
#
# =============================================================================

# =============================================================================
# CREAR COLUMNAS
#
# teams["GMC"]= 0
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
#
# =============================================================================

#Importar Tablas de Datos
season1516 = pd.read_csv("season-1516_csv.csv")
season1617 = pd.read_csv("season-1617_csv.csv")
season1718 = pd.read_csv("season-1718_csv.csv")
season1819 = pd.read_csv("season-1819_csv.csv")
teams = pd.read_csv("teams_csv.csv")
seasons = pd.concat([season1516, season1617, season1718, season1819, season1819])

#EQUIPOS: ALAVÉS, ATH BILBAO, ATL MADRID, BARCELONA, BETIS, CELTA, DEPORTIVO, EIBAR, ESPAÑOL, 
#GETAFE, GIRONA, GRANADA, HUESCA, LAS PALMAS, LEGANÉS, LEVANTE, MÁLAGA, OSASUNA, VALLECANO, MADRID, REAL SOCIEDAD, 
#SEVILLA, SPORTING, VALENCIA, VALLADOLID, VILLARREAL (26 equipos)

equipos = ['Alaves', 'Ath Bilbao', 'Ath Madrid', 'Barcelona', 'Betis', 'Celta', 'Eibar', 'Espanol', 'Getafe', 'Girona', 'Granada', 'Huesca', 'La Coruna', 'Las Palmas', 'Leganes', 'Levante', 'Malaga', 'Osasuna', 'Real Madrid', 'Sevilla', 'Sociedad', 'Sp Gijon', 'Valencia', 'Valladolid', 'Vallecano', 'Villarreal']
teams["VC"]= 0
teams["VF"]= 0
teams["VT"]= 0
teams["EC"]= 0
teams["EF"]= 0
teams["ET"]= 0
teams["DC"]= 0
teams["DF"]= 0
teams["DT"]= 0
teams["PTC"]= 0
teams["PTF"]= 0
teams["PT"]= 0

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
# =============================================================================
    i=i+1

teams.to_csv("teams_csv.csv", index = False)
