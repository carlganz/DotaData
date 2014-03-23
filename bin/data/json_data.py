import json
import urllib2
from pprint import pprint

hero_data = json.load(open('bin/data/my_heroes.json'))
skill_data = json.load(open('bin/data/my_abilities.json'))
lobby_data = json.load(open('bin/data/my_lobbies.json'))
gm_data = json.load(open('bin/data/my_modes.json'))
item_data = json.load(open('bin/data/my_items.json'))

def GetHeroFromID(hID):
    return str(hero_data[str(hID)])

def GetSkillFromID(sID):
    return str(skill_data[str(sID)])

def GetLobbyFromID(lID):
    return str(lobby_data[str(lID)])

def GetGMFromID(gmID):
    return str(gm_data[str(gmID)])

def GetItemFromID(iID):
    return str(item_data[str(iID)])

