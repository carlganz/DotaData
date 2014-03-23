from flask import Flask, render_template

# API
from bin.api.api_requests import *
from bin.data.json_data import *

# Database
from bin.db.db_update import *
from bin.db.db_actions import *
from bin.db.db_pretty import *
from bin.db.db_schema import GameData, PlayerData, AbilityUpgrades

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/d2db01.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/games')
def games():
    games = []
    for g in GetGamesByLobby(7):
        games.append(PrettyGame(g))
    return render_template('gameviewer.html', games=games)


@app.route('/stats')
def stats():
    p = GetDistinctModes()
    return render_template('tbd.html', message = str(GameData.query.count()))

@app.route('/about')
def about():
    return render_template('tbd.html', message = 'About the website and us!')

@app.route('/players')
def players():
    return render_template('tbd.html', message = 'Player information!')

@app.route('/aboutdb')
def tbd():
    UpdateGames()
    return render_template('tbd.html', message = 'Details about the database')   

if __name__ == '__main__':
    #MakeData()
    app.run(debug=True)
