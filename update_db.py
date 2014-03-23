from bin.db.db_schema import *
from bin.api.api_requests import *

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
        tid = g['match_id']
        if tid not in list(_g.match_id for _g in GameData.query.all()):
            db.session.add(GameData(g))
    db.session.commit()
    print('Complete')
    return

UpdateGames()
