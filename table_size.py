from bin.db.db_actions import GetTableSize
import os, sys

filename = '/home/adminuser/output2.txt'
output = open(filename, 'w')

sys.stdout = output
sys.stderr = output

print(GetTableSize())
