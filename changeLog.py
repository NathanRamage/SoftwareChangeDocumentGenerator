import subprocess
import clearcaseParser

# Reads commits and produces a dictionary with the file name as the key
# and a list of commits for that file

def RunCommand(command, versionControl="ClearCase"):
  """Runs a command to retrive a list of files and commit messages relate to that file

  Args:
    command: the command to produce commits and the related files
    versionControl: the version control software being used.  Default is ClearCase
  """
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  output, error = process.communicate();
  if error != None:
    print error
  else:
    if versionControl == "ClearCase":
      changeLog = clearcaseParser.CCParseChekinOutput(output)
      print changeLog
