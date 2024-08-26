def Transpose_Matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
  # Initialize the result matrix with zeros (dimensions are swapped)
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
      for j in range(cols):
        transposed[j][i] = matrix[i][j]
    return transposed

# call the function to test
x = [[8,8,8],[9,9,9]]
# Perform matrix transposition
transposed = Transpose_Matrix(x)
for row in transposed:
    print(row)
 
