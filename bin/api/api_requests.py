import urllib2, json
from pprint import pprint

# API URL's #
getMatchHistory = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?&min_players=10'
getMatchDetails = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?&match_id='

# String Constants #
accID = '&account_id='
maReq = '&matches_requested='
start = '&start_at_match_id='
date = '&date_min='
game_mode = '&game_mode='
hero = '&hero_id='
skill = '&skill='

# Vars #
my_api_key = '&key=06F26E71DA72FD03C5A1304C565EAA9E'

my_steam_id = 53793164
ni_steam_id = 133942829

class GameRequest:
  def __init__(self):
    self.acc_id = []
    self.start_ma_id = None
    self.num_req = None
    self.mode = None
    self.skill = None
    self.heroes = []

  def __repr__(self):
    return self.MakeString()

  def ConstrainByAccountID(self, acc_id):
    self.acc_id.append(acc_id)

  def StartAtMatchID(self, m_id):
    self.start_ma_id = m_id

  def SetMatchesRequested(self, ma_req):
    self.num_req = ma_req

  def SetGameMode(self, gm):
    self.mode = gm

  def SetSkillLevel(self, sr):
    self.skill = sr

  def ConstrainByHero(self, hID):
    self.heroes.append(hID)

  def MakeString (self):
    r = getMatchHistory
    for id in self.acc_id:
      r += str(accID) + str(id)

    if self.num_req != None:
      r += str(maReq) + str(self.num_req)

    if self.start_ma_id != None:
      r += str(start) + str(self.start_ma_id)

    if self.mode != None:
      r += str(game_mode) + str(self.game_mode)

    if self.skill != None:
      r += str(skill) + str(self.skill)

    for id in self.heroes:
      r += str(hero) + str(id)

    return r + my_api_key


  def MakeRequest (self):
    # Will Return an [] of json games
    games = []
    n = self.num_req
    while True:
      self.num_req = n if n < 101 else 100

      response = urllib2.urlopen(self.MakeString()).read().decode('utf8')
      for g in json.loads(response)['result']['matches']:
        games.append(g)

      if n < 101:
        break;
      else:
        self.start_ma_id = games[-1]['match_id']
        n -= 100

    return games


class DetailRequest:
  def __init__(self, m_id):
    self.m_id = m_id

  def __repr__(self):
    return getMatchDetails + str(self.m_id)

  def MakeString(self):
    return getMatchDetails + str(self.m_id) + my_api_key

  def MakeRequest(self):
    response = urllib2.urlopen(self.MakeString()).read().decode('utf8')
    return json.loads(response)['result']
