from flask import render_template
from app import app
from app.scripts import *


@app.route('/')
@app.route('/home')
def index():
    user = {'username': 'Jack'}
    return render_template('index.html')

@app.route('/betting')
def betting():
    matchupList = matchups.getMatchups()
    oddsList = spreads.getSpreads()
    return render_template('betting/betting.html', matchups = matchupList, odds = oddsList)