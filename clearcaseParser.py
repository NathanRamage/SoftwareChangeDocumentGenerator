from collections import OrderedDict
import re

def CCParseChekinOutput(commandOutput):
  checkins = commandOutput.split("\n")
  changes = {}
  for checkin in checkins:
    if checkin != '':
      fileName = re.search('.+?(?=@@)', checkin).group(0)
      comment = re.search(': (.*)', checkin).group(0)[2:]
      if fileName in changes:
        changes[fileName] += comment + "\n"
      else:
        changes[fileName] = comment + "\n"

  return changes
