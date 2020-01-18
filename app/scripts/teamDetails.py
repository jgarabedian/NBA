from . import constant
def getTeamInfo(team):
    from nba_api.stats.endpoints import teaminfocommon
    from nba_api.stats.static import teams
    team = team.replace('-', ' ').replace('LA', '').strip()
    teamInfo= teams.find_teams_by_full_name(team)[0]
    return teamInfo

def getTeamByOpponent(team1, team2):
    from nba_api.stats.endpoints import teamdashboardbyopponent
    teamDash = teamdashboardbyopponent.TeamDashboardByOpponent(team_id=team1,opponent_team_id=team2)
    df = teamDash.get_data_frames()[0]
    df = df[constant.OPPCOLUMN]
    df = multiplyColumns(df, constant.PCT_COL, 100)
    return df

def getTeamStats(team):
    from nba_api.stats.endpoints import teamdashboardbyteamperformance
    teamStats = teamdashboardbyteamperformance.TeamDashboardByTeamPerformance(team_id=team)
    df = teamStats.get_data_frames()[0]
    df = df[constant.OPPCOLUMN]
    df = multiplyColumns(df, constant.PCT_COL, 100)
    return df

def multiplyColumns(df, cols, num):
    df[cols] = round(df[cols] * num, 2)
    return df

# team1 = getTeamInfo('Miami')
# team = team1['id']
# df = getTeamStats(str(team))
# print(df)
# team2 = getTeamInfo('New-York')
# teamDash = getTeamByOpponent(team1['id'], team2['id'])
# teamDash2 = getTeamByOpponent(team2['id'], team1['id'])
# print(teamDash)
# print(teamDash2)
# print(teamDash.iterrows())

# teams = 'LA-Clippers_New-Orleans'
# one = 'LA-Clippers'
# two = 'New-Orleans'
# one = getTeamInfo(one)
# two = getTeamInfo(two)
# from nba_api.stats.endpoints import teaminfocommon
# from nba_api.stats.static import teams
# one = one.replace('-', ' ').replace('LA', '').strip()
# teamInfo= teams.find_teams_by_full_name(one)[0]
# print(teamInfo)
# print(two)
