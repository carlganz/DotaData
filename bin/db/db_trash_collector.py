from bin.db.db_schema import *
from pprint import pprint

def IsTrash (game):
  if FailTimeCheck(game):
    return True

  if FailTowerCheck(game):
    return True

  if FailRaxCheck(game):
    return True

  for p in game.players:
    if FailRealCheck(p):
      return True
    if FailKDACheck(p):
      return True
    if FailLHDCheck(p):
      return True
    if FailExperienceCheck(p):
      return True
    if FailGoldCheck(p):
      return True
    if FailDamageCheck(p):
      return True

  return False


# Game Checks
def FailTimeCheck (game):
  if game.duration < 600:
      return True
  return False

def FailTowerCheck (game):
  # Fails if all towers are still up
  if game.tower_status_radiant == 2047 and game.tower_status_dire == 2047:
    return True
  return False

def FailRaxCheck (game):
  # Fails if Both sets of Rax are still up
  if game.barracks_status_radiant == 63 and game.barracks_status_dire == 63:
    return True
  return False

# Player Checks
def FailRealCheck(player):
  # Checks if it was a real hero
  if player.hero_id == 0:
    return True
  return False

def FailKDACheck (player):
  # Fails if 0 kills, deaths and assists
  if player.kills == 0 and player.deaths == 0 and player.assists == 0:
    return True
  return False

def FailLHDCheck (player):
  # Fails if 0 last hits and denies
  if player.lh == 0 and player.denies == 0:
    return True
  return False

def FailExperienceCheck (player):
  # Fails if the player doesn't skill or gain xp
  if player.level == 0 or player.xpm == 0:
    return True
  return False

def FailGoldCheck (player):
  # Fails if no gold was spent or obtained
  if player.gold_spent == 0:
    # No Gold Spent, Probably Trash
    if player.gold == 0:
      return True

    # 1799 and 2500 are common afk gpm values, and can be used to indicate trash
    if player.gpm == 1799 or player.gpm == 2500:
      return True

  return False

def FailDamageCheck (player):
  # Fails if player does no damage to other players or towers
  if player.hero_damage == 0 and player.tower_damage == 0:
    return True
  return False

def IsLeaverCheck (player):
  if hasattr(player, 'leaver_status'):
    print('LEAVER: ' + str(player.leaver_status))
    return True
  return False
