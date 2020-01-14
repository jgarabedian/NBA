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

@app.route('/<matchup>')
def matchup(matchup):
    one = teamSelection.getTeamOne(matchup)
    two = teamSelection.getTeamTwo(matchup)
    one = teamDetails.getTeamInfo(one)
    two = teamDetails.getTeamInfo(two)
    oneName = one['full_name']
    twoName = two['full_name']
    oneStats = teamDetails.getTeamByOpponent(str(one['id']), str(two['id']))
    twoStats = teamDetails.getTeamByOpponent(str(two['id']), str(one['id']))
    oneOverall = teamDetails.getTeamStats(str(one['id']))
    twoOverall = teamDetails.getTeamStats(str(two['id']))
    return render_template('betting/teams.html.j2', one = oneName, two = twoName, 
        oneStats = oneStats, twoStats = twoStats, PCT_COL = constant.PCT_COL, 
        oneOverall = oneOverall, twoOverall = twoOverall, title = 'Matchup')