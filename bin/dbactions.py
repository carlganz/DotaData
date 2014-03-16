from dbschema import *
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
    return GameData.query.filter(GameData.players.any(account_id = my_steam_id)).filter(GameData.players.any(account_id = ni_steam_id)).all()

def GetNiGames ():
    return GameData.query.filter(GameData.players.any(account_id = ni_steam_id)).all()


def Reg (x1, x2):

    hero_list = json.load(open('bin/data/my_heroes.json'))
    num = len(hero_list)
    
    games = GameData.query.all()
    for g in games:
        binary = [110]
        heros = list(p.hero_id for p in g.players)
        for i in range(0, 109):
            binary.append(i in heros)

        
       
