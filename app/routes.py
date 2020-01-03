from flask import render_template
from app import app
from app.scripts import *


@app.route('/')
def Home():
    title = 'Home'
    return render_template('index.html.j2', title = title)

@app.route('/players')
def index():
    title = 'Players'
    return render_template('players/players.html.j2', title = title)

@app.route('/betting')
def betting():
    matchupList = matchups.getMatchups()
    oddsList = spreads.getSpreads()
    companyList = spreads.getCompanies()
    title = 'Betting'
    return render_template('betting/betting.html.j2',
        matchups=matchupList, odds=oddsList, companies=companyList, title=title)
    
# @app.route('/teams')
# def teams():
#     title = 'Teams'
#     teamList = teamSelection.getTeams()
#     return render_template('teams/teamSelection.html.j2', teams = teamList)

@app.route('/<matchup>')
def matchup(matchup):
    one = teamSelection.getTeamOne(matchup)
    two = teamSelection.getTeamTwo(matchup)
    oneKey = teamDictionary.getTeamKey(one)
    twoKey = teamDictionary.getTeamKey(two)
    return render_template('betting/teams.html.j2', one = one, two = two, title = oneKey)