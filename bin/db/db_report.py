from bin.db.db_schema import *

class Report:
  def __init__(self, game_query):
    self.count = game_query.count()

    games = game_query.all()

    self.game_time = 0
    self.r_win = 0
    self.avg_first_bld_time = 0

    self.player_count = 0

    self.kills = 0
    self.deaths = 0
    self.assists = 0

    self.lh = 0
    self.denies = 0

    self.gold = 0
    self.gold_spent = 0
    self.avg_gpm = 0

    self.h_damage = 0
    self.t_damage = 0

    self.healing = 0

    self.avg_xpm = 0

    for g in games:
      self.game_time += g.duration
      self.avg_first_bld_time += g.first_blood_time

      if g.radiant_win:
        self.r_win += 1

      for p in g.players:
        self.player_count += 1

        self.kills += p.kills
        self.deaths += p.deaths
        self.assists += p.assists

        self.gold += p.gold
        self.gold_spent += p.gold_spent
        self.avg_gpm += p.gpm

        self.lh += p.lh
        self.denies += p.denies

        self.h_damage += p.hero_damage
        self.t_damage += p.tower_damage

        self.healing += p.hero_healing

        self.avg_xpm += p.xpm

    self.avg_game_time = self.game_time / len(games)
    self.avg_first_bld_time /= len(games)
    self.avg_gpm /= self.player_count
    self.avg_xpm /= self.player_count


    return

  def __repr__(self):
    return 'Report for ' + str(self.count) + ' games'

  def GetDictionary (self):
    d = {}
    d.update({'count':self.count})
    d.update({'time':self.game_time})
    d.update({'avg_time':self.avg_game_time})
    d.update({'r_win':self.r_win})
    d.update({'p_count':self.player_count})
    d.update({'kills':self.kills})
    d.update({'deaths':self.deaths})
    d.update({'assists':self.assists})
    d.update({'gold':self.gold})
    d.update({'gold_spent':self.gold_spent})
    d.update({'gpm':self.avg_gpm})
    d.update({'lh':self.lh})
    d.update({'h_damage':self.h_damage})
    d.update({'t_damage':self.t_damage})
    d.update({'healing':self.healing})
    d.update({'fst_bld_time':self.avg_first_bld_time})
    d.update({'xpm':self.avg_xpm})
    return d
