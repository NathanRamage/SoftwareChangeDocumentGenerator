from docx import Document
import sys
import getopt

class AdminDetails:
  def __init__(self, woNum='', woTitle='', devName='', build='', branch=''):
    self._woNum = woNum
    self._woTitle = woTitle
    self._devName = devName
    self._build = build
    self._branch = branch

  def getWoNum(self):
    """Gets the Work Order number.

    Retuns:
      The Work Order number as a string.
    """
    return self._woNum

  def setWoNum(self, value):
    """Sets the Work Order number.

    Args:
      value: The Work Order number as a string.
    """
    self._woNum = value

  def getWoTitle(self):
    """Gets the Work Order title.

    Retuns:
      The Work Order title as a string.
    """
    return self._woTitle

  def setWoTitle(self, value):
    """Sets the Work Order title.

    Args:
      value: The Work Order title as a string.
    """
    self._woTitle = value

  def getDevName(self):
    """Gets the Developer's name.

    Retuns:
      The Developer's name as a string.
    """
    return self._devName

  def setDavName(self, value):
    """Sets the Developer's name.

    Args:
      value: The Developer's name as a string.
    """
    self._devName = value

  def getBuild(self):
    """Gets the build number.

    Retuns:
      The build number as a string.
    """
    return self._build

  def setBuild(self, value):
    """Sets the build number.

    Args:
      value: The build number as a string.
    """
    self._build = value

  def getBranch(self):
    """Gets the development branch.

    Retuns:
      The branch as a string.
    """
    return self._branch

  def setBranch(self, value):
    """Sets the development branch.

    Args:
      value: The development branch as a string.
    """
    self._branch = value

def gen_doc(inputFile, outputFile, adminDetails):
  document = Document(inputFile)

  # Get the heading table, has two columns need to add content to the second column
  # The rows are as follows
  # Work order
  # Work order title
  # Responsible Engineer
  # Build
  # Branch
  headerTable = document.tables[0]

  columnCells = headerTable.column_cells(1)

  # Set the Work Order
  columnCells[0].text = adminDetails.getWoNum()

  # Set the Work Order title
  columnCells[1].text = adminDetails.getWoTitle()

  # Set the Developer's Name
  columnCells[2].text = adminDetails.getDevName()

  # Set the Build
  columnCells[3].text = adminDetails.getBuild()

  # Set the branch
  columnCells[4].text = adminDetails.getBranch()

  document.save(outputFile)

def main(argv):
  inputFile=""
  outputFile=""
  adminDetails = AdminDetails()

  try:
    opts, args = getopt.getopt(argv, "i:o:w:t:d:b:r")
  except getopt.GetoptError:
    print "SoftwareChangeDoc.py -i <input file> -o <output file> -w <work order> -t <work order title> -d <developer's name> -b <build number> -r <branch>"
  for opt, arg in opts:
    if opt == '-i':
      inputFile = arg
    elif opt == '-o':
      outputFile = arg
    elif opt == '-w':
      adminDetails.setWoNum(arg)
    elif opt == '-t':
      adminDetails.setWoTitle(arg)
    elif opt == '-d':
      adminDetails.setDevName(arg)
    elif opt == '-b':
      adminDetails.setBuild(arg)
    elif opt == '-r':
      adminDetails.setBranch(arg)

  gen_doc(inputFile, outputFile, adminDetails)

if __name__ == "__main__":
  main(sys.argv[1:])
