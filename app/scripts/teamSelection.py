def getTeams():
    import requests

    headers= {
            'Authorization': 'Bearer f4ed397f-34d3-4e2d-b83d-65c0a39a67ee',
            'User-Agent': 'My User Agent 1.0',
            'From': 'jgarabedian96@gmail.com'
        }

    response = requests.get('https://erikberg.com/nba/teams.json', headers=headers)
    return response.json()

def getTeamOne(matchup):
    teamOne = matchup[: matchup.find('_')]
    return (teamOne)

def getTeamTwo(matchup):
    teamTwo = matchup[matchup.rfind('_') + 1 :]
    return(teamTwo)