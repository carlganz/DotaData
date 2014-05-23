from bin.db.db_actions import GetTableSize
from bin.util.logs import *

SetOutputFile('table_size.txt')

print(GetTableSize())
