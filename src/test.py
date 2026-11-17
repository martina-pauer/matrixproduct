from matrix import Matrix
from matrix import Product
# Define Matrix sizes
A = Matrix(2, 3)
B = Matrix(3, 2)
# Add components to first matrix
#  1 -4 2
#  -1 4 -2  
for component in [1, -4, 2, -1, 4, -2]:
  A.add_component(component)
# Add components to second matrix
#  1 2
#  -1 3
#  5 -2
for component in [1, 2, -1, 3, 5, -2]:
  B.add_component(component)
# Show result
#  15 -14
#  -15 14
C = Product(A, B)
C.get_components()

for row in range(0, C.C.matrix.__len__()):
  print(C.C.get_row(row))
