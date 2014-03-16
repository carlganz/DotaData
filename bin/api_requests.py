import urllib2, json
from pprint import pprint

# API URL's #
getMatchHistory = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?'
getMatchDetails = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?&match_id='

# String Constants #
accID = '&account_id='
maReq = '&matches_requested='
start = '&start_at_match_id='
date = '&date_min='

# Vars #
my_api_key = '&key=06F26E71DA72FD03C5A1304C565EAA9E'

my_steam_id = 53793164
ni_steam_id = 133942829

class Request:
    request_type = None
    acc_id = None
    ma_id = None
    num = None
    start_ma_id = None

    def __init__(self, _type):
        self.request_type = _type

    def __repr__(self):
        return str(self.request)

    def ConstrainByAccountID(self, acc_id):
        self.acc_id = acc_id

    def AddMatchID(self, m_id):
        self.ma_id = m_id

    def StartAtMatchID(self, m_id):
        self.start_ma_id = m_id

    def SetMatchesRequested(self, ma_req):
        self.num = ma_req

    def Stringify (self):
        req = ''
        if(self.request_type == None) :
            return 'No Request Type'
        if(self.request_type == 1):
            req += getMatchHistory
        elif self.request_type == 2:
            req += getMatchDetails

        if self.acc_id != None:
            req += accID + str(self.acc_id)
        if self.ma_id != None:
            req += str(self.ma_id)
        else :
            if self.request_type == 2:
                return 'No Match ID'
        if self.num != None:
            req += maReq + str(self.num)
        if self.start_ma_id != None:
            req += start + str(self.start_ma_id)

        return req + my_api_key
        
    def MakeRequest (self):
        if self.request_type == None:
            return 'err'
        elif self.request_type == 1:
            # Will Return an [] of json games
            games = []
            n = self.num
            while True:
                self.num = n if n < 101 else 100
                
                response = urllib2.urlopen(self.Stringify()).read().decode('utf8')
                for g in json.loads(response)['result']['matches']:
                    games.append(g)

                
                if n < 101:
                    break;
                else:
                    self.start_at_match_id = games[-1]['match_id']
                    n -= 100
            
            return games
        elif self.request_type == 2:
            response = urllib2.urlopen(self.Stringify()).read().decode('utf8')
            return json.loads(response)['result']


    
class request_types:
    matchHistory = 1
    matchDetails = 2

num = 10
def RequestMyGames():
    r = Request(1)
    r.ConstrainByAccountID(my_steam_id)
    r.SetMatchesRequested(num)
    gs = r.MakeRequest()
    return gs

def RequestNiGames():
    r = Request(1)
    r.ConstrainByAccountID(ni_steam_id)
    r.SetMatchesRequested(num)
    gs = r.MakeRequest()
    return gs

def RequestGames():
    r = Request(1)
    r.SetMatchesRequested(num)
    gs = r.MakeRequest()
    return gs
    

