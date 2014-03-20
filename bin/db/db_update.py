from dbschema import *
from dbactions import *
from api_requests import *

from pprint import pprint

# Adds the most recent (maybe) 500 games to the database
# skips games already added
def UpdateGames ():
    last_game_id = GameData.query.order_by(GameData.match_id.desc()).first()

    ids = list(g.match_id for g in GameData.query.all())
    
    _id = None
    games = []
    
    for i in range(0, 5):
        r = Request(1)
        r.StartAtMatchID(_id)
        r.SetMatchesRequested(100)
        _r = r.MakeRequest()

        for g in _r:
            mid = g['match_id']
            if mid not in ids:
                games.append(g)
        
        _id = games[-1]['match_id']
                    

    print(str(len(games)) + ' games to add')
    for g in games:
        AddGame(g)
    print('Complete')
    return

UpdateGames()

