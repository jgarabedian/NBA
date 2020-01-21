from . import constant
from . import data
import time
from eventlet import Timeout
timeout = Timeout(5)
def getTeamInfo(team):
    from nba_api.stats.endpoints import teaminfocommon
    from nba_api.stats.static import teams
    team = team.replace('-', ' ').replace('LA', '').strip()
    with timeout:
        try:
            teamInfo= teams.find_teams_by_full_name(team)[0]
        except:
            teamInfo = 'timeout'
    return teamInfo

def getTeamByOpponent(team1, team2):
    # start = time.time()
    from nba_api.stats.endpoints import teamdashboardbyopponent
    with timeout:
        try:
            teamDash = teamdashboardbyopponent.TeamDashboardByOpponent(team_id=team1,opponent_team_id=team2, timeout=1)
            # eventlet.sleep(5)
            df = teamDash.get_data_frames()[0]
            df = df[constant.OPPCOLUMN]
            df = multiplyColumns(df, constant.PCT_COL, 100)
            print('finished the try')
        except:
            timeout.cancel()
            df = 'timeout'
            print('got exception')
        finally:
            timeout.cancel()
            print('got finally')
    
    # print('It took ' + str(runTime) + ' seconds to run getTeamByOpponent')
    return df

def getTeamStats(team):
    from nba_api.stats.endpoints import teamdashboardbyteamperformance
    try:
        teamStats = teamdashboardbyteamperformance.TeamDashboardByTeamPerformance(team_id=team, timeout=5)
        df = teamStats.get_data_frames()[0]
        df = df[constant.OPPCOLUMN]
        df = multiplyColumns(df, constant.PCT_COL, 100)
    except:
        df = 'timeout'
    print(df)
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
