from bin.db.db_schema import *
from bin.api.api_requests import *
import json

# This program queries the Dota API for the last 500 games and stores the data.

# Takes an array of Json game data
def AddGames(games):
  for g in games:
    if len(GameData.query.filter(GameData.match_id == g['match_id']).all()) == 0 :
      db.session.add(GameData(g))
    else:
      print("Skipping game with id: " + str(g['match_id']))
  db.session.commit()
  print('Complete')

def GrabGamesForAccID (acc_id):
  req = GameRequest()
  req.SetMatchesRequested(500)
  req.ConstrainByAccountID(acc_id)

  games = req.MakeRequest()

  print(str(len(games)) + ' games to add for id: ' + str(acc_id))
  AddGames(games)

def UpdateAllAccounts ():
  accounts = json.load(open('bin/data/account_ids.json'))
  for a in accounts:
    GrabGamesForAccID(a)

UpdateAllAccounts()
