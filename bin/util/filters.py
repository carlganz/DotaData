from bin.db.db_schema import *
from bin.db.db_actions import *
from werkzeug import MultiDict

ValidFilters = ['hero_id', 'account_id', 'game_mode', 'page']

def GamesFromArgs (args):
  return BuildQueryFromFilters(GetValidFilters(args))


def GetValidFilters (args):
  filters = MultiDict()
  for arg, val in args.iteritems(True):
    if arg in ValidFilters:
      filters.add(arg, val)

  return filters

def BuildQueryFromFilters(filters):
  q = GameQuery()

  #Game Mode Filter
  gm = filters.get('game_mode')
  if not gm == None:
    q.FilterByMode(gm)

  for arg, val in filters.iteritems(True):
    if arg == 'hero_id':
      q.FilterByHeroID(val)

    elif arg == 'account_id':
      q.FilterByAccountID(val)

  page = filters.get('page') or 1
  return q.GetQuery(page)
