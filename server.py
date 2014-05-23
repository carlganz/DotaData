from flask import Flask, render_template, request

# API
from bin.api.api_requests import *
from bin.data.json_data import *

# Database
from bin.db.db_actions import *
from bin.db.db_pretty import *
from bin.db.db_schema import GameData, PlayerData, AbilityUpgrades

# Utility
from bin.util.filters import *

# Setup App Server #

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/d2db01.db' # Relative Path
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/games')
def games():
  args = request.args
  games = GamesFromArgs(args)

  pretty_games = list(PrettyGame(g) for g in games)

  return render_template('gameviewer.html', games=pretty_games, portraits = GetAllPortraits())

@app.route('/details')
def details():
    m_id = request.args.get('id')
    game = PrettyGame(GameData.query.filter(GameData.match_id == m_id).first())
    return render_template('gamedetails.html', game = game)

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/players')
def players():
    return render_template('players.html')

@app.route('/aboutdb')
def tbd():
    return render_template('tbd.html', message = 'Details about the database')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
