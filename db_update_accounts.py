from bin.util.logs import *

SetOutputFile('update_accounts.txt')

from bin.db.db_schema import *
from bin.api.api_requests import *
from bin.db.db_actions import *

import json, os

# This program queries the Dota API for the last 500 games and stores the data.
def GrabGamesForAccID (acc_id):
  req = GameRequest()
  req.SetMatchesRequested(500)
  req.ConstrainByAccountID(acc_id)

  games = req.MakeRequest()

  AddGames(games)

def UpdateAllAccounts ():
  root_path = os.path.dirname(os.path.realpath(__file__))
  accounts = json.load(open(root_path + '/bin/data/account_ids.json'))
  for a in accounts:
    GrabGamesForAccID(a)

UpdateAllAccounts()
