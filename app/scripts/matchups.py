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
    # TODO: get date of matchup
    matchups = []
    for li in matchups_list:
        matchups.append(li.getText().replace("\n", "").replace("\t", "_").replace("Matchup", "Matchup: "))
    # print("I found " + str(len(matchUps)) + " matchups")
    return matchups

