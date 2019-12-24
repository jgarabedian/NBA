def getMatchups():
    from bs4 import BeautifulSoup
    import urllib.request
    import re

    # using odds shark
    url = 'https://www.oddsshark.com/nba/odds'

    try: page = urllib.request.urlopen(url)
    except: print("An Error Occurred opening the page")

    soup = BeautifulSoup(page, 'html.parser')

    # regex search to find the matchups
    regex = re.compile('op-matchup-wrapper basketball')
    matchups_list = soup.find_all('div', attrs={'class': regex})
    matchTeamList = []
    # TODO: get date of matchup
    for match in matchups_list:
        matchTime = match.find('div', {'class': 'op-matchup-time op-matchup-text'}).getText()
        matchTop = match.find('div', {'class': 'op-matchup-team op-matchup-text op-team-top'}).getText()
        matchBottom = match.find('div', {'class': 'op-matchup-team op-matchup-text op-team-bottom'}).getText()
        matchVs = str(matchTime) + ': ' + str(matchTop) + ' vs ' + str(matchBottom)
        matchTeamList.append(matchVs) 

    return matchTeamList

