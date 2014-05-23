import json
import sys, os
import urllib2
from pprint import pprint

real_path = os.path.dirname(os.path.realpath(__file__))

hero_data = json.load(open(real_path + '/hero_data_name.json'))
hero_portraits = json.load(open(real_path + '/hero_portraits.json'))
hero_portraits_sm = json.load(open(real_path + '/hero_portraits_small.json'))
skill_data = json.load(open(real_path + '/my_abilities.json'))
lobby_data = json.load(open(real_path + '/my_lobbies.json'))
gm_data = json.load(open(real_path + '/my_modes.json'))
item_data = json.load(open(real_path + '/my_items.json'))
account_ids = json.load(open(real_path + '/account_ids.json'))

_hero_data = json.load(open(real_path + '/hero_data.json'))

def LookupAccountID(aID):
	return str(account_ids[str(aID)]) if str(aID) in account_ids else aID

def GetHeroNameFromID(hID):
  return _hero_data[str(hID)]['localized_name'] if str(hID) in _hero_data else 'No Hero'

def GetHeroDataNameFromID(hID):
  return _hero_data[str(hID)]['name'] if str(hID) in _hero_data else 'No Hero'


def GetLargePortraitFromID(hID):
	return _hero_data[str(hID)]['por-lg'] if str(hID) in _hero_data else 'No Hero'

def GetSmallPortraitFromID(hID):
	return _hero_data[str(hID)]['por-sm'] if str(hID) in _hero_data else 'No Hero'

def GetAllPortraits():
	p = []
	for i in range(1, len(_hero_data) - 1):
		if str(i) in _hero_data:
			p.append(_hero_data[str(i)]['por-sm'])

	return p

def GetSkillFromID(sID):
  return str(skill_data[str(sID)]) if str(sID) in skill_data else 'UnKnown'

def GetLobbyFromID(lID):
  return str(lobby_data[str(lID)]) if str(lID) in lobby_data else 'UnKnown'

def GetGMFromID(gmID):
  return str(gm_data[str(gmID)]) if str(gmID) in gm_data else 'UnKnown'

def GetItemFromID(iID):
  return str(item_data[str(iID)]) if str(iID) in item_data else 'UnKnown'

def CompileHeroData ():
	heroes = {}

	for h in hero_data:
		hID = h['id']
		name = h['name']
		lname = h['localized_name']
		lgpor = hero_portraits[str(hID)]
		smpor = hero_portraits_sm[str(hID)]

		this_hero = {'name':name, 'localized_name':lname, 'por-lg':lgpor, 'por-sm':smpor}

		heroes.update({hID:this_hero})

	with open('bin/data/hero_data.json', 'w') as out:
		json.dump(heroes, out)
