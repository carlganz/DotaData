from flask import Flask, render_template
from bin.dbschema import GameData, PlayerData, AbilityUpgrades
from bin.api_requests import *
from bin.api_data import *
from bin.dbactions import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/d2db01.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/games')
def games():
    games = GameData.query.all()
    ni_games = GetNiGames()
    my_ni_games = GetMyNiGames()
    return render_template('gameviewer.html', games=games)

@app.route('/about')
@app.route('/players')
@app.route('/stats')
@app.route('/aboutdb')
def tbd():
    return 'To be Created'

def MakeData():
    ResetTable()
    
    mine = RequestMyGames()
    nicks = RequestNiGames()
    _all = RequestGames()

    games = mine + nicks + _all
    for g in games:
        AddGame(g)    

if __name__ == '__main__':
    #MakeData()
    
    
    app.run(debug=True)
