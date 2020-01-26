def getMatchups():
    from bs4 import BeautifulSoup
    from urllib.error import HTTPError
    import urllib.request
    import re

    # using odds shark
    url = 'https://www.oddsshark.com/nba/odds'

    try:
        page = urllib.request.urlopen(url)
    except HTTPError as err:
        if err.code == 404:
            print('404 Error occurred')
        else:
            print(err)

    soup = BeautifulSoup(page, 'html.parser')

    # regex search to find the matchups
    regex = re.compile('op-matchup-wrapper basketball')
    regex2 = re.compile('op-matchup-links has-matchup-links')
    matchups_list = soup.find_all('div', attrs={'class': [regex, regex2]})
    # print(matchups_list)
    matchTeamList = []
    for match in matchups_list:
        # print(match)
        # matchTime = match.find('div', {'class': 'op-matchup-time op-matchup-text'}).getText()
        cnt = 0
        for a in match:
            if len(match) == 3:
                if cnt == 0:
                    # print(a.text)
                    matchTime = a.text
                    # cnt += 1
                    # continue
                elif cnt == 2:
                    # print(a)
                    matchTop = a.find('a', {'class': 'odds-link op-matchup-team-text'}).text
                    matchBottom = a.find('div', {'class': 'op-matchup-team op-matchup-text op-team-bottom'}).text
                    # cnt += 1
                    break
                cnt += 1
            # matchTop = a.find('a', {'class': 'odds-link op-matchup-team-text'})
            # if matchTop != None:
                # break
        # matchTop = match.find('a', {'class': 'odds-link op-matchup-team-text'})
        # matchTop = 'String'
        # print(matchTop)
        # matchBottom = match.find('div', {'class': 'op-matchup-team op-matchup-text op-team-bottom'}).getText()
        # matchDate = match.find('a', {'class': 'odds-link full-matchup'})['href']
        # print(matchDate)
        # parse and format the date
        # matchDate = getMatchDate(matchDate)
        # matchTime = 'TBD'
        matchDate = 'TBD'
        # matchBottom = 'TBD'

        matchVs = str(matchDate) + ' ' + str(matchTime) + ': ' + str(matchTop) + ' vs ' + str(matchBottom)
        # print(matchVs)
        # matchVs = str(matchTime) + ': ' + str(matchTop) + ' vs ' + str(matchBottom)

        # print(matchDate)
        if matchVs not in matchTeamList:
            matchTeamList.append(matchVs)
    print(matchTeamList)
    return matchTeamList


def getMatchDate(string):
    import dateutil.parser as dparser
    # parse the link to just get the date
    strLeft = string.find('odds')
    strRight = string.rfind('-')

    string = string[strLeft + 5:strRight]

    # format date
    string = dparser.parse(str(string), fuzzy=True).strftime('%B %d %Y')

    return string
# getMatchups()