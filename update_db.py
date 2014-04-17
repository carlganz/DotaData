from bin.db.db_schema import *
from bin.api.api_requests import *

# Adds the most recent (maybe) 500 games to the database
# skips games already added
def UpdateWithRequestParameters (account_ids = None, game_type = None, hero_ids = None, skill = None, min_players = None, league_id = None):
    baser = Request(1)

    for id in account_ids:
        baser.ConstrainByAccountID(id)

    if game_type:
    	baser



def UpdateGames ():
    _id = None
    games = []

    for i in range(0, 5):
        r = Request(1)
        r.StartAtMatchID(_id)
        r.SetMatchesRequested(100)
        _r = r.MakeRequest()

        for g in _r:
            mid = g['match_id']
            if len(GameData.query.filter(GameData.match_id == mid).all()) == 0:
                games.append(g)


        _id = games[-1]['match_id']


    print(str(len(games)) + ' games to add - Overall')
    AddGames(games)
    return

def UpdateGamesWithID(uid):
    _id = None
    newgames = []

    for i in range(0, 5):
        r = Request(1)
        r.ConstrainByAccountID(uid)
        r.StartAtMatchID(_id)
        r.SetMatchesRequested(100)
        _r = r.MakeRequest()

        for g in _r:
            mid = g['match_id']
            if len(GameData.query.filter(GameData.match_id == mid).all()) == 0:
                newgames.append(g)

        _id = _r[-1]['match_id']
            


    print(str(len(newgames)) + ' games to add')
    AddGames(newgames)

def AddGames(games):
    for g in games:
        if len(GameData.query.filter(GameData.match_id == g['match_id']).all()) == 0 :
            db.session.add(GameData(g))
        else:
            print("Skipping game with id: " + str(g['match_id']))
    db.session.commit()
    print('Complete')

db.drop_all()
db.create_all()
UpdateGames()
UpdateGamesWithID(my_steam_id)
UpdateGamesWithID(ni_steam_id)

