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

def GetMyGames ():
    return GameData.query.filter(GameData.players.any(account_id = my_steam_id)).all()

def GetMyNiGames ():
    return GameData.query.filter(GameData.players.any(account_id = my_steam_id))\
           .filter(GameData.players.any(account_id = ni_steam_id)).all()

def GetNiGames ():
    return GameData.query.filter(GameData.players.any(account_id = ni_steam_id)).all()

def GetAllGames ():
    return GameData.query.all()

def GetHeroCount ():
    G = GameData.query.all()[:100]
    heroes = Counter()
    for g in G:
        heroes.update(list(GetHeroFromID(p.hero_id) for p in g.players))
    
    return heroes

def GetDistinctModes():
    return db.session.query(GameData.game_mode.distinct()).all()

def GetDistinctLobbies():
    return db.session.query(GameData.lobby_type.distinct()).all()


def GetGamesByMode(mode):
    G = GameData.query.filter(GameData.game_mode == mode)
    return G[:100]

def GetGamesByLobby(lobby):
    G = GameData.query.filter(GameData.lobby_type == lobby)
    return G[:100]

def GetUniquePlayers():
    players = list()
    q = GameQuery()
    q.FilterByMode(1)
    q.FilterByLobby(4)
    players = list(q.GetQuery())
    return sorted(list(players))

def TestQuery():
    q = GameQuery()
    q.FilterByItemID(10)
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

    def GetQuery(self):
        return self.baseq.all()



def Reg (x1, x2):

    hero_list = json.load(open('bin/data/my_heroes.json'))
    num = len(hero_list)
    
    games = GameData.query.all()
    for g in games:
        binary = [110]
        heros = list(p.hero_id for p in g.players)
        for i in range(0, 109):
            binary.append(i in heros)

        
       
