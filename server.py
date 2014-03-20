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
    games = GameData.query.all()[:10]
    return render_template('gameviewer.html', games=games)


@app.route('/stats')
def stats():
    c = GetHeroCount()
    
    
    return str(c.most_common())

@app.route('/about')
@app.route('/players')
@app.route('/aboutdb')
def tbd():
    return render_template('tbd.html')   

if __name__ == '__main__':
    #MakeData()
    app.run(debug=True)
