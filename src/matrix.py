class Matrix:
  def __init__(self, rows: int, columns: int):
    '''
      Define a matrix with components
    '''
    matrix: list = []
    # Complete with zeros to set later the components
    for row in range(0, rows):
      matrix.append([])
      for column in range(0, columns):
        matrix[row].append(0)
    
 def add_component(self, component: float, row: int, column: int):
   '''
     Add a component in position row and column
  '''
   self.matrix[row][column] = component

def get_row(self, position: int) -> list[float]:
  '''
    Give the row in that position
  '''
  return self.matrix[position]

def get_column(self, position: int) -> list[float]:
  '''
    Give the column in that position
  '''
  column: list[float] = []
  for row in range(0, matrix.__len__()):
    column.append(matrix[row][position])
  return clumn
