import os, sys
import time

logs_folder = str(os.path.expanduser('~')) + '/Logs/'

def SetOutputFile (filename):
  file = logs_folder + str(filename)

  if not os.path.exists(os.path.dirname(file)):
    os.makedirs(os.path.dirname(file))

  root, ext = os.path.splitext(file)
  file = str(root) + '-' + str(time.strftime('%d-%H-%M-%S')) + str(ext)


  output = open(file, 'w')

  sys.stdout = output
  sys.stderr = output
