teamDictionary = {
    'Atlanta': 'atlanta-hawks',
    'Boston': 'boston-celtics',
    'Brooklyn': 'brooklyn-nets',
    'Charlotte': 'charlotte-hornets',
    'Chicago': 'chicago-bulls',
    'Dallas': 'dallas-mavericks',
    'Denver': 'denver-nuggets',
    'Detroit': 'detroit-pistons',
    'Golden State': 'golden-state-warrior',
    'Indiana': 'indiana-pacers',
    'LA Clippers': 'los-angeles-clippers',
    'LA Lakers': 'los-angeles-lakers',
    'Memphis': 'memphis-grizzlies',
    'Miami': 'miami-heat',
    'Milwaukee': 'milwaukee-bucks',
    'New Orleans': 'new-orleans-pelicans',
    'New York': 'new-york-knicks',
    'Oklahoma City': 'oklahoma-city-thunder',
    'Orlando': 'orlando-magic',
    'Philadelphia': 'philadelphia-76ers',
    'Phoenix': 'phoenix-suns',
    'Portland': 'portland-trail-blazers',
    'Sacramento': 'sacramento-kings',
    'San Antonio': 'san-antonio-spurs',
    'Toronto': 'toronto-raptors',
    'Utah': 'utah-jazz',
    'Washington': 'washington-wizards'
}

def getTeamKey(team):
    teamKey = teamDictionary[team]
    return(teamKey)


print(teamDictionary['Toronto'])
print(teamDictionary['Utah'])