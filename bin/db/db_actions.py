from bin.db.db_schema import *
from bin.data.json_data import *
from collections import Counter
import json

def ResetTable():
    db.drop_all()
    db.create_all()

def AddGame (data):
    _id = data['match_id']
    if _id in list(g.match_id for g in GameData.query.all()):
        return
    db.session.add(GameData(data))
    db.session.commit()

def GetDistinctModes():
    return db.session.query(GameData.game_mode.distinct()).all()

def GetDistinctLobbies():
    return db.session.query(GameData.lobby_type.distinct()).all()

def GetUniquePlayers():
    players = db.session.query(PlayerData.account_id.distinct()).all()
    return len(players)

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
       
