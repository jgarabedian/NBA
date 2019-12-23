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
    title = 'Betting'
    return render_template('betting/betting.html.j2', matchups = matchupList, odds = oddsList, title = title)