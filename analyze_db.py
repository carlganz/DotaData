from bin.db.db_schema import *
from bin.db.db_actions import *
import csv

def HeroWinrate (h_id, games):

  in_games = []
  wins = []

  slot = None

  for g in games:
    for i in range(0, 2):
      _in = False
      for p in g.players[i*5:5*(i+1)]:
        if p.hero_id == h_id:
          _in = True;
          slot = p.slot

      if _in:
        in_games.append(1)

      else:
        in_games.append(0)

      if  i == 0:
        wins.append(int(g.radiant_win))
      else:
        wins.append(int(not g.radiant_win))



  with open('values.csv', 'wb') as csvfile:
    swriter = csv.writer(csvfile, delimiter=',')

    swriter.writerow(['in', 'win'])
    for i in range(0, len(wins)):
      swriter.writerow([in_games[i], wins[i]])


games = GameData.query.all()
HeroWinrate(5, games)
