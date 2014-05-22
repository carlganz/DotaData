from bin.db.db_schema import *

def TotalMatches ():
  return GameData.query.count()

def TotalMatchesOfGameType(t_id):
  return GameData.query.filter(GameData.game_mode == t_id).count()

def TotalTimesHeroPlayed(games, h_id):
  return GameData.query.filter(GameData.players.any(hero_id = h_id)).count()


def TotalTimesItemPurchased(games, i_id):

  count = 0
  for g in games:
    for p in g.players:
      if i_id == p.item0: count = count + 1
      if i_id == p.item1: count = count + 1
      if i_id == p.item2: count = count + 1
      if i_id == p.item3: count = count + 1
      if i_id == p.item4: count = count + 1
      if i_id == p.item5: count = count + 1

  return count

def TotalTimesRadiantWins (games):
  return GameData.query.filter(GameData.radiant_win == True).count()

def TotalGoldSpent (games):
  gs = 0
  for g in games:
    for p in g.players:
      gs += p.gold_spent
  return gs

def TotalHeroDamage (games):
  hd = 0
  for g in games:
    for p in g.players:
      hd += p.hero_damage
  return hd

def TotalTowerDamage (games):
  td = 0
  for g in games:
    for p in g.players:
      td += p.tower_damage
  return td

def TotalHeroHealing (games):
  hh = 0
  for g in games:
    for p in g.players:
      hh += p.hero_healing
  return hh

def TotalKDA (games):
  k = 0
  d = 0
  a = 0
  for g in games:
    for p in g.players:
      k += p.kills
      d += p.deaths
      a += p.assists
  return (k, d, a)

def TotalLHD (games):
  lh = 0
  d = 0
  for g in games:
    for p in g.players:
      lh += p.lh
      d += p.denies
  return (lh, d)
