from __future__ import division
from bin.util.logs import *

SetOutputFile('analyze.txt')

from bin.db.db_schema import *
from bin.db.db_actions import *
from bin.db.db_observations import *
from bin.db.db_report import *
from bin.data.json_data import hero_data
import csv, os, json, time, threading
from pprint import pprint

# The one function to rule them all
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
    filename = '/home/adminuser/Logs/DotaTests/' + str(test_name) + '.csv'
    if not os.path.exists(os.path.dirname(filename)):
      os.makedirs(os.path.dirname(filename))

    with open(filename, 'w') as csvfile:
      sw = csv.writer(csvfile, delimiter=',')
      sw.writerow(['hyp', 'win', x])

      for i in range(0, len(wins)):
        sw.writerow([test_array[i], wins[i]])

## Team Tests
# Tests if hero is on team
def HeroIDTest (players, hID):
  ids = list(p.hero_id for p in players)
  return hID in ids

# Tests if all heroes are on team
def MultiHeroIDTest (players, h_ids):
  ids = list(p.hero_id for p in players)

  for h in h_ids:
    if h not in ids:
      return False
  return True

# Tests if the item appears greater than or num number of times on a team
def ItemTest (players, i_id, num = 1):
  count = 0
  for p in players:
    if i_id == p.item0: count = count + 1
    if i_id == p.item1: count = count + 1
    if i_id == p.item2: count = count + 1
    if i_id == p.item3: count = count + 1
    if i_id == p.item4: count = count + 1
    if i_id == p.item5: count = count + 1

  return count >= num

## Test Sweeps ##
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


def CreateReportForGames(games, label):
  #SetOutputFile(str(label) + '.txt')

  # report = bin.db.db_report.Report(games)
  # r_dict = report.GetDictionary()
  #
  # d = {label:r_dict}
  # print(json.dumps(d, indent=2, sort_keys=True))

  print(GameData.query.count())


x = time.time()

for i in range(1, 11):
  games = GameData.query.paginate(i, per_page=100).items
  args = (games, 'set' + str(i))
  thread.start_new_thread(CreateReportForGames, (games, args,))

print(time.time() - x)
