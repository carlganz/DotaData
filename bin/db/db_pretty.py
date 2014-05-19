from bin.db.db_schema import *
from bin.data.json_data import *
from datetime import datetime

# This file Defines 'pretty' classes for displaying our data

class PrettyGame:
  def __init__(self, game):
    self.match_id = game.match_id
    self.match_seq = game.match_seq
    self.start_time = datetime.fromtimestamp(game.start_time)
    self.duration = game.duration
    self.lobby_type = GetLobbyFromID(game.lobby_type)
    self.game_mode = GetGMFromID(game.game_mode)
    self.radiant_win = game.radiant_win
    self.barracks_status_dire = game.barracks_status_dire #
    self.barracks_status_radiant = game.barracks_status_radiant #
    self.tower_status_dire = game.tower_status_dire #
    self.tower_status_radiant = game.tower_status_radiant #
    self.league_id = game.league_id
    self.cluster = game.cluster
    self.first_blood_time = game.first_blood_time
    self.human_players = game.human_players
    self.pos_votes = game.pos_votes
    self.neg_votes = game.neg_votes
    self.players = list(PrettyPlayer(p) for p in game.players)


class PrettyPlayer:
  def __init__(self, player):
    self.hero_id = GetHeroNameFromID(player.hero_id)
    self.portrait_url = GetLargePortraitFromID(player.hero_id)
    self.account_id = LookupAccountID(player.account_id) if player.account_id != 4294967295 else 'Private'
    self.assists = player.assists
    self.deaths = player.deaths
    self.denies = player.denies
    self.gold = player.gold
    self.gpm = player.gpm
    self.gold_spent = player.gold_spent
    self.hero_damage = player.hero_damage
    self.hero_healing = player.hero_healing
    self.items = []
    self.items.append(GetItemFromID(player.item0))
    self.items.append(GetItemFromID(player.item1))
    self.items.append(GetItemFromID(player.item2))
    self.items.append(GetItemFromID(player.item3))
    self.items.append(GetItemFromID(player.item4))
    self.items.append(GetItemFromID(player.item5))
    self.item_urls = []
    for i in self.items:
      if i == 'empty':
        self.item_urls.append('')
      else:
        self.item_urls.append('http://cdn-01-origin.steampowered.com/apps/dota2/images/items/' + str(i) + '_lg.png')
    self.kills = player.kills
    self.last_hits = player.lh
    if hasattr(player, 'leaver_status'):
      self.leaver_status = player.leaver_status
    self.level = player.level
    self.slot = player.slot
    self.tower_damage = player.tower_damage
    self.xpm = player.xpm

    self.abs = []
    self.abs_level = []
    self.abs_images = []

    for a in player.abilities:
      if a.ability not in self.abs:
        self.abs.append(a.ability)
      self.abs_level.append(self.abs.index(a.ability))

    for a in self.abs:
      s_name = GetSkillFromID(a)
      if s_name == 'stats':
        self.abs_images.append('https://raw.githubusercontent.com/kronusme/dota2-api/master/images/stats.png')
      else:
        self.abs_images.append('http://cdn-01-origin.steampowered.com/apps/dota2/images/abilities/' + str(s_name) + '_lg.png')

class PrettyAbility:
  def __init__(self, ability):
    self.id = ability.ability
    self.ability = GetSkillFromID(ability.ability)
    if self.ability == 'stats':
      self.ability_img_url = 'https://raw.githubusercontent.com/kronusme/dota2-api/master/images/stats.png'
    else:
      self.ability_img_url = 'http://cdn-01-origin.steampowered.com/apps/dota2/images/abilities/' + str(self.ability) + '_lg.png'
    self.level = ability.level
    self.time = ability.time
