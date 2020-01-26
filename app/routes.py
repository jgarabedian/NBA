from flask import render_template, request
from app import app
from app.scripts import *
import time
from time import sleep


@app.route('/')
def Home():
    title = 'Home'
    return render_template('home.html', title = title)

@app.route('/players')
def index():
    title = 'Players'
    return render_template('players/players.html.j2', title = title)

@app.route('/betting')
def betting():
    rule = request.path
    if rule == '/betting':
        data.matchups = matchups.getMatchups()
        data.spreads = spreads.getSpreads()
        data.companies = spreads.getCompanies()
    title = 'Betting'
    return render_template('betting/betting.html.j2',
        matchups=data.matchups, odds=data.spreads, companies=data.companies, urlMatch = rule, renderStats = None, title=title)

# TODO: Add celery tasks to reduce timeouts
@app.route('/<teams>', methods=['POST'])
def teams(teams):
    start = time.time()
    dataFound = True
    urlMatch = str(teams)
    one = teamSelection.getTeamOne(teams)
    two = teamSelection.getTeamTwo(teams)
    one = teamDetails.getTeamInfo(one)
    two = teamDetails.getTeamInfo(two)
    oneName = one['full_name']
    twoName = two['full_name']
    print(str(one['id']))
    print(str(two['id']))
    oneStats = teamDetails.getTeamByOpponent(str(one['id']), str(two['id']))
    if str(oneStats) == 'timeout':
        twoStats = False
        dataFound = False
        print('Lost at oneStats')
    else:
        sleep(10)
        twoStats = teamDetails.getTeamByOpponent(str(two['id']), str(one['id']))
    if str(twoStats) == 'timeout' or dataFound == False:
        dataFound = False
        print('Lost at two stats')
    # oneOverall = teamDetails.getTeamStats(str(one['id']))
    # twoOverall = teamDetails.getTeamStats(str(two['id']))
    runTime = time.time() - start
    print(runTime)
    print('At the end dataFround is ' + str(dataFound))
    return render_template('betting/betting.html.j2', 
        matchups=data.matchups, odds=data.spreads, companies=data.companies, 
        one = oneName, two = twoName, 
        oneStats = oneStats, twoStats = twoStats, PCT_COL = constant.PCT_COL, INVERSE_COL = constant.INVERSE_COL,
        # oneOverall = oneOverall, twoOverall = twoOverall, 
        renderStats = True, urlMatch = urlMatch, dataFound = dataFound)