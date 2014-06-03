from bin.db.db_schema import *
from bin.data.json_data import *
from collections import Counter


class Report:
  def __init__(self, games):
    self.count = len(games)

    self.game_time = 0
    self.r_win = 0
    self.first_bld_time = 0
    self.player_count = 0

    self.kills = 0
    self.deaths = 0
    self.assists = 0

    self.lh = 0
    self.denies = 0

    self.gold = 0
    self.gold_spent = 0
    self.gpm = 0

    self.h_damage = 0
    self.t_damage = 0

    self.healing = 0

    self.xpm = 0

    for g in games:
      self.game_time += g.duration
      self.r_win += int(g.radiant_win)
      self.first_bld_time += g.first_blood_time

      for p in g.players:
        self.player_count += 1
        self.kills += p.kills
        self.deaths += p.deaths
        self.assists += p.assists
        self.lh += p.lh
        self.denies += p.denies
        self.gold += p.gold
        self.gold_spent += p.gold_spent
        self.gpm += p.gpm
        self.h_damage += p.hero_damage
        self.t_damage += p.tower_damage
        self.healing += p.hero_healing
        self.xpm += p.xpm


    self.hero_report = HeroReport(games)
    self.mode_report = ModeReport(games)
    return

  def __repr__(self):
    return 'Report for ' + str(self.count) + ' games'

  def GetDictionary (self):
    d = {}
    d.update({'count':self.count})
    d.update({'time':self.game_time})
    d.update({'r_win':self.r_win})
    d.update({'p_count':self.player_count})
    d.update({'kills':self.kills})
    d.update({'deaths':self.deaths})
    d.update({'assists':self.assists})
    d.update({'gold':self.gold})
    d.update({'gold_spent':self.gold_spent})
    d.update({'gpm':self.gpm})
    d.update({'lh':self.lh})
    d.update({'h_damage':self.h_damage})
    d.update({'t_damage':self.t_damage})
    d.update({'healing':self.healing})
    d.update({'fst_bld_time':self.first_bld_time})
    d.update({'xpm':self.xpm})
    d.update({'heroes_played':self.hero_report.GetDictionary()})
    d.update({'modes_played':self.mode_report.GetDictionary()})
    return d


class HeroReport:
  def __init__(self, games):
    c = Counter()
    for h in hero_data:
      c[int(h)] = 0

    for g in games:
      for p in g.players:
        if not int(p.hero_id) in c:
          print('Not fount: ' + str(p.hero_id))
        else:
          c[int(p.hero_id)] += 1

    self.report = c

  def GetDictionary (self):
    d = {}
    for key in self.report:
      d.update({str(GetHeroNameFromID(key)):self.report[key]})
    return d

class ModeReport:
  def __init__(self, games):
    c = Counter()
    for gm in gm_data:
      c[int(gm)] = 0

    for g in games:
      if not int(g.game_mode) in c:
        print('Not fount: ' + str(g.game_mode))
      else:
        c[int(g.game_mode)] += 1

    self.report = c

  def GetDictionary (self):
    d = {}
    for key in self.report:
      if self.report[key] > 0:
        d.update({GetGMFromID(key):self.report[key]})
    return d
