class Matrix:
  def __init__(self, rows: int, columns: int):
    '''
      Define a matrix with components
    '''
    self.matrix: list = []
    self.row: int = 0
    self.column: int = 0
    # Complete with zeros to set later the components
    for row in range(0, rows):
      self.matrix.append([])
      for column in range(0, columns):
        self.matrix[row].append(0)
        
  def add_component(self, component: float):
    '''
      Add a component in position row and column
    '''
    self.matrix[self.row][self.column] = component
    # Add Component in last space
    if self.row < (self.matrix.__len__() - 1):
      self.row += 1
    else:
      self.row = 0
    if self.column < (self.matrix[0].__len__() - 1):
      self.column += 1
    else:
      self.column = 0

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
    for row in range(0, self.matrix.__len__()):
      column.append(self.matrix[row][position])
    return column


class Product:
  def __init__(self, matrix_A, matrix_B):
    '''
      Take two matrices For Make the product
      in a third matrix
    '''
    self.A = matrix_A
    self.B = matrix_B
    # The Product Matrix has rows in first and columns in second
    self.C = Matrix(self.A.matrix.__len__(), self.B.matrix[0].__len__())
    
  def get_components(self):
    '''
      Calculate each component and save in product matrix C
    '''
    for row in range(0, self.A.matrix.__len__()):
      self.C.matrix.append([])
      for column in range(0, self.B.matrix[0].__len__()):
        sumate: float = 0
        for ro in self.A.get_row(row):
          for co in self.B.get_column(column):
            sumate += ro * co
        self.C.matrix[row].append(sumate)
