from docx import Document

workOrderNum = "1234"
workOrderTitle = "Test"
developerName = "Rick"
build = "22"
branch = "branch456"

def gen_doc():
  document = Document('/opt/SoftChange-template.docx')

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
  columnCells[0].text = workOrderNum

  # Set the Work Order title
  columnCells[1].text = workOrderTitle

  # Set the Developer's Name
  columnCells[2].text = developerName

  # Set the Build
  columnCells[3].text = build

  # Set the branch
  columnCells[4].text = branch

  document.save('/opt/SoftChange-test.docx')

if __name__ == "__main__":
  gen_doc()
