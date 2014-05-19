from bin.db.db_schema import *
from bin.db.db_actions import *
from bin.data.json_data import _hero_data
import csv

def LinearRegression (test_name, test_f, games, *test_args):

  test_array = []
  wins = []
  for g in games:
    res = int (test_f(g.GetRadiantTeam(), *test_args))
    test_array.append(res)
    wins.append((int)(g.radiant_win == True))

    res = int (test_f(g.GetDireTeam(), *test_args))
    test_array.append(res)
    wins.append((int)(g.radiant_win == False))

  x = 0
  for i in test_array:
    if i == 1:
      x = x + 1

  if not x == 0:
    with open('tests/' + str(test_name) + '.csv', 'w') as csvfile:
      sw = csv.writer(csvfile, delimiter=',')
      sw.writerow(['hyp', 'win', x])

      for i in range(0, len(wins)):
        sw.writerow([test_array[i], wins[i]])

def HeroIDTest (players, hID):
  ids = list(p.hero_id for p in players)
  return hID in ids

def MultiHeroIDTest (players, h_ids):
  ids = list(p.hero_id for p in players)

  for h in h_ids:
    if h not in ids:
      return False
  return True

def TestAllHeroes (games):
  for h in _hero_data:
    test_name = 'hero/single/' + _hero_data[str(h)]['localized_name']
    LinearRegression(test_name, HeroIDTest, games, int(h))

def TestAllPairs (games):
  for h in _hero_data:
    for j in _hero_data:
      if not h == j:

        test_name = 'hero/dual/' + _hero_data[str(h)]['localized_name'] + '_' + _hero_data[str(j)]['localized_name']
        args = [h, j]
        LinearRegression(test_name, MultiHeroIDTest, games, args)

def TestAllTrips (games):
  for h in _hero_data:
    for j in _hero_data:
      if not h == j:
        for k in _hero_data:
          if k != j and k != h:
            test_name = 'hero/trip/' + _hero_data[str(h)]['localized_name'] + '_' + _hero_data[str(j)]['localized_name'] + '_' + _hero_data[str(k)]['localized_name']
            args = [h, j, k]
            LinearRegression(test_name, MultiHeroIDTest, games, args)

def TestAllQuads (games):
  for h in _hero_data:
    for j in _hero_data:
      if not (h == j):
        for k in _hero_data:
          if not (k == h or k == j):
            for i in _hero_data:
              if not (i == k or i == j or i == h):
                test_name = 'hero/quad/' + _hero_data[str(h)]['localized_name'] + '_' + _hero_data[str(j)]['localized_name'] + '_' + _hero_data[str(k)]['localized_name'] + '_' + _hero_data[str(i)]['localized_name']
                args = [h, j, k, i]
                LinearRegression(test_name, MultiHeroIDTest, games, args)

def TestAllPentas (games):
  for h in _hero_data:
    for j in _hero_data:
      if not (h == j):
        for k in _hero_data:
          if not (k == h or k == j):
            for i in _hero_data:
              if not (i == k or i == j or i == h):
                for l in _hero_data:
                  if not (l == i or l == k or l == j or l == h):
                    test_name = 'hero/pent/' + _hero_data[str(h)]['localized_name'] + '_' + _hero_data[str(j)]['localized_name'] + '_' + _hero_data[str(k)]['localized_name'] + '_' + _hero_data[str(i)]['localized_name'] + '_' + _hero_data[str(l)]['localized_name']
                    args = [h, j, k, i, l]
                    LinearRegression(test_name, MultiHeroIDTest, games, args)

games = GameData.query.all()

TestAllHeroes(games)
TestAllPairs(games)
TestAllTrips(games)
TestAllQuads(games)
TestAllPentas(games)
