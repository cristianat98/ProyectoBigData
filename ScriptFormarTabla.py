import pandas as pd

# =============================================================================
# CREACIÓN DEL DATASET EQUIPOS
# teams = pd.DataFrame(equipos, columns=['Equipos'])
# =============================================================================

# =============================================================================
#CREAR COLUMNAS
# teams["GMC"]= 0
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
teams["GMC"]= 0

#BUSCAR TODOS LOS PARTIDOS DE UN EQUIPO, SUMAR TODAS SUS ESTADÍSTICAS Y GUARDARLA EN EL DATASET CON LA SUMA TOTAL Y LA MEDIA
i=0
for equipo in equipos:
    is_teamHome = seasons.loc[:, 'HomeTeam'] == equipo
    is_teamAway = seasons.loc[:, 'AwayTeam'] == equipo
    matchsHome_team = seasons.loc[is_teamHome]
    matchsAway_team = seasons.loc[is_teamAway]
    GMC = matchsHome_team['FTHG'].sum()
    GRC = matchsHome_team['FTAG'].sum()
    GMF = matchsAway_team['FTAG'].sum()
    GRF = matchsAway_team['FTHG'].sum()
    GMT = GMC + GMF
    GRT = GRC + GRF
    
    teams.loc[i, "GMC"] = GMC
    teams.loc[i, "GRC"] = GRC
    teams.loc[i, "GMF"] = GMF
    teams.loc[i, "GRF"] = GRF
    teams.loc[i, "GMT"] = GMT
    teams.loc[i, "GRT"] = GRT
    teams.loc[i, "GMCPP"] = GMC/(2*len(matchsAway_team))
    teams.loc[i, "GRCPP"] = GRC/(2*len(matchsAway_team))
    teams.loc[i, "GMFPP"] = GMF/(2*len(matchsAway_team))
    teams.loc[i, "GRFPP"] = GRF/(2*len(matchsAway_team))
    teams.loc[i, "GMTPP"] = GMT/(2*len(matchsAway_team))
    teams.loc[i, "GRTPP"] = GRT/(2*len(matchsAway_team))
    i=i+1

teams.to_csv("teams_csv.csv", index = False)
