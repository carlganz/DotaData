from bin.db.db_schema import *
from bin.api.api_requests import *
import json

# This program queries the Dota API for the last 500 games and stores the data.

# Takes an array of Json game data
def AddGames(games):
  games_added = 0

  for g in games:
    if len(GameData.query.filter(GameData.match_id == g['match_id']).all()) == 0 :
      db.session.add(GameData(g))
      games_added = games_added + 1

  db.session.commit()
  print('Complete, Added ' + str(games_added) + ' Games!')

def GrabGamesForAccID (acc_id):
  req = GameRequest()
  req.SetMatchesRequested(500)
  req.ConstrainByAccountID(acc_id)

  games = req.MakeRequest()

  AddGames(games)

def UpdateAllAccounts ():
  accounts = json.load(open('bin/data/account_ids.json'))
  for a in accounts:
    GrabGamesForAccID(a)

UpdateAllAccounts()
