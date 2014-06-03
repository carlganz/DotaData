import os, sys
import time

logs_folder = str(os.path.expanduser('~')) + '/Logs/'
logger = None

def SetOutputFile (filename):
  file = logs_folder + str(filename)

  if not os.path.exists(os.path.dirname(file)):
    os.makedirs(os.path.dirname(file))

  root, ext = os.path.splitext(file)
  file = str(root) + '-' + str(time.strftime('%d-%H-%M-%S')) + str(ext)


  logger = open(file, 'w')

  sys.stdout = logger
  sys.stderr = logger


def SyncLogger ():
  if not logger == None:
    logger.flush()
    os.fsync(logger.fileno())


def Logg(o):
  print(o)
  SyncLogger()
