import json
from pprint import pprint

hero_data = json.load(open('bin/data/my_heroes.json'))
skill_data = json.load(open('bin/data/my_abilities.json'))

def GetHeroFromID(hID):
    return str(hero_data[str(hID)])

def GetSkillFromID(sID):
    return str(skill_data[str(sID)])
