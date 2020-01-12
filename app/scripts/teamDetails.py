def getTeamInfo(team):
    from nba_api.stats.endpoints import teaminfocommon
    from nba_api.stats.static import teams
    team = team.replace('-', ' ')
    teamInfo= teams.find_teams_by_full_name(team)[0]
    return teamInfo

def getTeamByOpponent(team1, team2):
    from nba_api.stats.endpoints import teamdashboardbyopponent
    teamDash = teamdashboardbyopponent.TeamDashboardByOpponent(team_id=team1,opponent_team_id=team2)
    return teamDash.get_data_frames()[0]