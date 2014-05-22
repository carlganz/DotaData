from bin.db.db_schema import *
from bin.api.api_requests import *
from bin.db.db_actions import *

import json

# This program queries the Dota API for the last 500 games and stores the data.
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
