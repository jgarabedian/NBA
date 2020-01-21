import pandas as pd

companies = []
spreads = []
matchups = []

errorData = {
    'GP': 0,
    'W': 0,
    'L': 0,
    'W_PCT': 0,
    'FGM': 0,
    'FGA': 0,
    'FG_PCT': 0,
    'FG3M': 0,
    'FG3A': 0,
    'FG3_PCT': 0,
    'FTM': 0,
    'FTA': 0,
    'FT_PCT': 0,
    'OREB': 0,
    'DREB': 0,
    'REB': 0,
    'AST': 0,
    'TOV': 0,
    'STL': 0,
    'BLK': 0,
    'BLKA': 0,
    'PF': 0,
    'PFD': 0,
    'PTS': 0,
    'PLUS_MINUS': 0
}

errorFrame = pd.DataFrame(data = errorData, index=[0])