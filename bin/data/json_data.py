import json
import urllib2
from pprint import pprint

hero_data = json.load(open('bin/data/hero_data_name.json'))
skill_data = json.load(open('bin/data/my_abilities.json'))
lobby_data = json.load(open('bin/data/my_lobbies.json'))
gm_data = json.load(open('bin/data/my_modes.json'))
item_data = json.load(open('bin/data/my_items.json'))
account_ids = json.load(open('bin/data/account_ids.json'))

def LookupAccountID(aID):
	return str(account_ids[str(aID)]) if str(aID) in account_ids else aID

def GetHeroNameFromID(hID):
    for h in hero_data:
        if hID == h['id']:
            return h['localized_name']
    return 'UnKnown'

def GetHeroDataNameFromID(hID):
    for h in hero_data:
        if h['id'] == hID:
            return h['name'][14:]
    return 'UnKnown'

def GetHeroPortraitFromID(hID):
    for h in hero_data:
        return 'http://cdn.dota2.com/apps/dota2/images/heroes/' + str(GetHeroDataNameFromID(hID)) + '_lg.png'
    return 'UnKnown'


def GetSkillFromID(sID):
    return str(skill_data[str(sID)]) if str(sID) in skill_data else 'UnKnown'

def GetLobbyFromID(lID):
    return str(lobby_data[str(lID)]) if str(lID) in lobby_data else 'UnKnown'

def GetGMFromID(gmID):
    return str(gm_data[str(gmID)]) if str(gmID) in gm_data else 'UnKnown'

def GetItemFromID(iID):
    return str(item_data[str(iID)]) if str(iID) in item_data else 'UnKnown'
