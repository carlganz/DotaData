from flask import Flask, render_template, request

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
    for g in TestQuery():
        games.append(PrettyGame(g))
    return render_template('gameviewer.html', games=games)

@app.route('/details')
def details():
    id = request.args.get('id')
    game = PrettyGame(GameData.query.filter(GameData.match_id == id).first())
    return render_template('gamedetails.html', game = game)


@app.route('/stats')
def stats():
    p = GetUniquePlayers()
    return render_template('tbd.html', message = str(p))

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/players')
def players():
    return render_template('tbd.html', message = 'Player information!')

@app.route('/aboutdb')
def tbd():
    return render_template('tbd.html', message = 'Details about the database')   

if __name__ == '__main__':
    #MakeData()
    app.run(debug=True)
