#!/usr/bin/python
from bin.util.logs import *

SetOutputFile('update_all.txt')

from bin.db.db_schema import *
from bin.api.api_requests import *
from bin.db.db_actions import *

# This program queries the Dota API for the last 500 games and stores the data.
def GrabAllGames ():
  GrabGamesForSkillLevel(1)
  GrabGamesForSkillLevel(2)
  GrabGamesForSkillLevel(3)


def GrabGamesForSkillLevel (l):
  req = GameRequest()
  req.SetMatchesRequested(500)
  req.SetSkillLevel(l)

  games = req.MakeRequest()
  AddGames(games, l)

GrabAllGames()
