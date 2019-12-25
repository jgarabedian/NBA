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
        matchDate = match.find('a', {'class': 'base-versus'})['href']
        # parse and format the date
        matchDate = getMatchDate(matchDate)

        matchVs = str(matchDate) + ' ' + str(matchTime) + ': ' + str(matchTop) + ' vs ' + str(matchBottom)
        
        # print(matchDate)
        matchTeamList.append(matchVs) 

    return matchTeamList

def getMatchDate(string):
    import datetime
    import dateutil.parser as dparser
    # parse the link to just get the date
    strLeft = string.find('odds')
    strRight = string.rfind('-')

    string = string[strLeft + 5 : strRight]
    
    #format date
    string = dparser.parse(str(string), fuzzy=True).strftime('%B %d %Y')
    
    return string
