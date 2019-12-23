from flask import render_template
from app import app
from app.scripts import *


@app.route('/')
@app.route('/players')
def index():
    user = {'username': 'Jack'}
    return render_template('players/players.html.j2')

@app.route('/betting')
def betting():
    matchupList = matchups.getMatchups()
    oddsList = spreads.getSpreads()
    return render_template('betting/betting.html.j2', matchups = matchupList, odds = oddsList)