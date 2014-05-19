from bin.db.db_schema import *
from bin.data.json_data import *
from bin.db.db_trash_collector import *
from collections import Counter
import json

# This file contains definitions for database cleaning, adding and querying

def ResetTable():
    db.drop_all()
    db.create_all()

def TestQuery():
    q = GameQuery()
    return q.GetQuery()

class GameQuery():
  def __init__(self):
    self.baseq = GameData.query

  def FilterByMode(self, mode):
    self.baseq = self.baseq.filter(GameData.game_mode == mode)

  def FilterByLobby(self, lobby):
    self.baseq = self.baseq.filter(GameData.lobby_type == lobby)

  def FilterByPlayerID(self, pID):
    self.baseq = self.baseq.filter(GameData.players.any(account_id = pID))

  def FilterByHeroID(self, hID):
    self.baseq = self.baseq.filter(GameData.players.any(hero_id = hID))

  def FilterByPlayerHero(self, pID, hID):
    self.baseq = self.baseq.filter(GameData.players.any(hero_id = hID, account_id = pID))

  def FilterByItemID(self, iID):
    self.baseq = self.baseq.filter(GameData.players.any(item0 = iID)).union(self.baseq.filter(GameData.players.any(item1=iID)))

# Returns a BaseQuery class
  def QuerySize(self):
    return self.baseq.count()

  def GetQuery(self, page=1):
    return self.baseq.paginate(int(page), 5).items



# Takes an array of Json game data
def AddGames(games, sr = 0):
  games_added = 0
  trashed_games = 0
  for g in games:
    m_id = g['match_id']

    if len(GameData.query.filter(GameData.match_id == m_id).all()) == 0 :
      dg = GameData(g, sr)

      if IsTrash(dg):
        trashed_games = trashed_games + 1
        db.session.rollback()
      else:
        db.session.add(dg)
        db.session.commit()
        games_added = games_added + 1

  print('Complete, Added ' + str(games_added) + ', Trashed ' + str(trashed_games) + ' Games!')
