def getSpreads():
    from bs4 import BeautifulSoup
    import urllib.request
    import re

    # using odds shark
    url = 'https://www.oddsshark.com/nba/odds'

    try:
        page = urllib.request.urlopen(url)
    except:
        print("An Error Occurred opening the page")

    soup = BeautifulSoup(page, 'html.parser')

    #find the spreads
    regexSpread = re.compile('op-item-wrapper')
    spread_list = soup.find_all('div', attrs={'class': regexSpread})

    #get the spreads in a list
    spreads = []
    for li in spread_list:
        spreadData = li.getText().replace("-", " -").replace("+", " +")
        if spreadData != '':
            spreads.append(spreadData)

    # print("I found " + str(len(spreads)) + " spreads")
    return spreads
