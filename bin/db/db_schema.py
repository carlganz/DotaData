from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from bin.api.api_requests import *
import random
from pprint import pprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../db/d2db01.db'
db = SQLAlchemy(app)

def GetMatchDetails(m_id):
  r = DetailRequest(m_id)
  return r.MakeRequest()

class GameData(db.Model):
  _id = db.Column(db.Integer, primary_key = True, unique=True)
  match_id = db.Column(db.Integer, unique = True)
  match_seq= db.Column(db.Integer, unique = True)

  skill_rating = db.Column(db.Integer)

  start_time = db.Column(db.Integer)
  duration = db.Column(db.Integer)

  lobby_type = db.Column(db.Integer)
  game_mode = db.Column(db.Integer)

  radiant_win = db.Column(db.Boolean)

  barracks_status_dire = db.Column(db.Integer)
  barracks_status_radiant = db.Column(db.Integer)

  tower_status_dire = db.Column(db.Integer)
  tower_status_radiant = db.Column(db.Integer)

  cluster = db.Column(db.Integer)
  first_blood_time = db.Column(db.Integer)
  human_players = db.Column(db.Integer)

  league_id = db.Column(db.Integer)

  pos_votes = db.Column(db.Integer)
  neg_votes = db.Column(db.Integer)

  def __init__(self, jres, sr = 0):
    jres = GetMatchDetails(jres['match_id'])
    self.match_id = jres['match_id']
    self.match_seq = jres['match_seq_num']
    self.skill_rating = sr
    self.start_time = jres['start_time']
    self.duration = jres['duration']
    self.lobby_type = jres['lobby_type']
    self.game_mode = jres['game_mode']
    self.radiant_win = jres['radiant_win']
    self.barracks_status_dire = jres['barracks_status_dire']
    self.barracks_status_radiant = jres['barracks_status_radiant']
    self.tower_status_dire =jres['tower_status_dire']
    self.tower_status_radiant =jres['tower_status_radiant']
    self.league_id = jres['leagueid']
    self.cluster = jres['cluster']
    self.first_blood_time = jres['first_blood_time']
    self.human_players = jres['human_players']
    self.pos_votes = jres['positive_votes']
    self.neg_votes = jres['negative_votes']

    for player in jres['players']:
        db.session.add(PlayerData(player, self))

    return

  def __repr__(self):
    return 'Match ID: ' + str(self.match_id)

class PlayerData(db.Model):
  _id = db.Column(db.Integer, primary_key = True, unique = True)
  match = db.relationship('GameData', backref = db.backref('players', lazy = 'dynamic'))

  hero_id = db.Column(db.Integer)
  account_id = db.Column(db.Integer)

  match_id = db.Column(db.Integer, db.ForeignKey('game_data.match_id'))
  unique_pm_id = db.Column(db.Integer, unique = True)

  kills = db.Column(db.Integer)
  deaths = db.Column(db.Integer)
  assists = db.Column(db.Integer)

  lh = db.Column(db.Integer)
  denies = db.Column(db.Integer)

  gold = db.Column(db.Integer)
  gold_spent = db.Column(db.Integer)
  gpm = db.Column(db.Integer)

  hero_damage = db.Column(db.Integer)
  hero_healing = db.Column(db.Integer)
  tower_damage = db.Column(db.Integer)

  item0 = db.Column(db.Integer)
  item1 = db.Column(db.Integer)
  item2 = db.Column(db.Integer)
  item3 = db.Column(db.Integer)
  item4 = db.Column(db.Integer)
  item5 = db.Column(db.Integer)

  level = db.Column(db.Integer)
  xpm = db.Column(db.Integer)

  slot = db.Column(db.Integer)

  def __init__(self, data, game):
    self.match = game
    self.hero_id = data['hero_id']

    if 'account_id' in data:
      self.account_id = data['account_id']
      if self.account_id != 4294967295:
        self.unique_pm_id = int(str(game.match_id) + str(self.account_id))
      else:
        self.unique_pm_id = int(str(game.match_id) + str(random.randint(10000, 100000)))
    else:
      self.account_id = 0
      self.unique_pm_id = int(str(game.match_id) + str(random.randint(10000, 100000)))

    self.assists = data['assists']
    self.deaths = data['deaths']
    self.denies = data['denies']
    self.gold = data['gold']
    self.gpm = data['gold_per_min']
    self.gold_spent = data['gold_spent']
    self.hero_damage = data['hero_damage']
    self.hero_healing = data['hero_healing']
    self.item0 = data['item_0']
    self.item1 = data['item_1']
    self.item2 = data['item_2']
    self.item3 = data['item_3']
    self.item4 = data['item_4']
    self.item5 = data['item_5']
    self.kills = data['kills']
    self.lh = data['last_hits']
    if 'leaver_status' in data:
      self.leaver_status = data['leaver_status']
    self.level = data['level']
    self.slot = data['player_slot']
    self.tower_damage = data['tower_damage']
    self.xpm = data['xp_per_min']

    if 'ability_upgrades' in data:
      for ab in data['ability_upgrades']:
        db.session.add(AbilityUpgrades(ab, self))

  def __repr__(self):
    return 'Player ' + str(self.account_id)


class AbilityUpgrades(db.Model):
  _id = db.Column(db.Integer, primary_key = True)
  ability = db.Column(db.Integer)
  level = db.Column(db.Integer)
  time = db.Column(db.Integer)

  player = db.relationship('PlayerData', backref = db.backref('abilities', lazy='dynamic'))
  player_id = db.Column(db.Integer, db.ForeignKey('player_data.unique_pm_id'))

  def __init__(self, data, player):
    self.ability = data['ability']
    self.level = data['level']
    self.time = data['time']
    self.player = player

  def __repr__(self):
    return 'Ability: ' + str(self.ability)
