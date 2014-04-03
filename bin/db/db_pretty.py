from bin.db.db_schema import *
from bin.data.json_data import *
from datetime import datetime

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
        self.portrait_url = GetHeroPortraitFromID(player.hero_id)
        self.account_id = LookupAccountID(player.account_id) if player.account_id != 4294967295 else 'Private'
        self.assists = player.assists
        self.deaths = player.deaths
        self.denies = player.denies
        self.gold = player.gold
        self.gpm = player.gpm
        self.gold_spent = player.gold_spent
        self.hero_damage = player.hero_damage
        self.hero_healing = player.hero_healing
        self.item0 = GetItemFromID(player.item0)
        self.item1 = GetItemFromID(player.item1)
        self.item2 = GetItemFromID(player.item2)
        self.item3 = GetItemFromID(player.item3)
        self.item4 = GetItemFromID(player.item4)
        self.item5 = GetItemFromID(player.item5)
        self.kills = player.kills
        if hasattr(player, 'last_hits'):
            self.last_hits = player.last_hits
        if hasattr(player, 'leaver_status'):
            self.leaver_status = player.leaver_status
        self.level = player.level
        self.slot = player.slot
        self.tower_damage = player.tower_damage
        self.xpm = player.xpm
        self.abilities = list(PrettyAbility(a) for a in player.abilities)

class PrettyAbility:
    def __init__(self, ability):
        self.ability = ability.ability
        self.level = ability.level
        self.time = ability.time
        
    
