from bin.db.db_schema import *
from bin.data.json_data import *
from collections import Counter
import json

# This file contains definitions for database cleaning and querying

def ResetTable():
    db.drop_all()
    db.create_all()

def TestQuery():
    q = GameQuery(1)
    return q.GetQuery()

class GameQuery():
  def __init__(self, page):
    self.baseq = GameData.query
    self.page = page

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
  def GetQuery(self):
    return self.baseq.paginate(1, 5).items
