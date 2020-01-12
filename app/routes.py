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
    oneName = teamDetails.getTeamInfo(one)['full_name']
    twoName = teamDetails.getTeamInfo(two)['full_name']
    oneId = str(teamDetails.getTeamInfo(one)['id'])
    twoId = str(teamDetails.getTeamInfo(two)['id'])
    oneStats = teamDetails.getTeamByOpponent(oneId, twoId)
    twoStats = teamDetails.getTeamByOpponent(twoId, oneId)
    return render_template('betting/teams.html.j2', one = oneName, two = twoName, oneStats = oneStats, twoStats = twoStats, title = oneName)