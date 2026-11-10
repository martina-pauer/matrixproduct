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


class Product:
  def __init__(self, matrix_A, matrix_B):
    '''
      Take two matrices For Make the product
      in a third matrix
    '''
    self.A = matrix_A
    self.B = matrix_B
    # The Product Matrix has rows in first and columns in second
    self.C = Matrix(self.A.matrix.__len__(), self.B.matrix[0].___len__())
    
def get_components(self):
  '''
    Calculate each component and save in product matrix C
  '''
  for row in range(0, self.A.matrix.__len__()):
    self.append([])
    for column in range(0, self.B[0].__len__()):
      sumate: float = 0
      for ro in self.A.get_row(row):
        for co in self.B.get_column(column):
          sumate += ro * co
      self.C[row].append(sumate)
