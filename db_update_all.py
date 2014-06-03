#!/usr/bin/python
from bin.util.logs import *

SetOutputFile('update_all.txt')

from bin.db.db_schema import *
from bin.api.api_requests import *
from bin.db.db_actions import *

# This program queries the Dota API for the last 500 games and stores the data.
def GrabAllGames ():
  req = GameRequest()
  req.SetMatchesRequested(100)
  GrabGamesForGameMode(req, 5)

  req = GameRequest()
  req.SetMatchesRequested(100)
  GrabGamesForGameMode(req, 4)

def GrabGamesForGameMode(req, mode):
  req.SetGameMode(mode)
  GrabGamesForSkillLevel(req, 1)
  GrabGamesForSkillLevel(req, 2)
  GrabGamesForSkillLevel(req, 3)

def GrabGamesForSkillLevel (req, l):

  req.SetSkillLevel(l)

  games = req.MakeRequest()
  AddGames(games, l)


GrabAllGames()
