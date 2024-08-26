def Matrix_Multiplication(x,y):
  xrows = len(x)
  xcols = len(x[0])
  yrows = len(y)
  ycols = len(y[0])
  if xcols!=yrows:
     print("multiplication is not happening as product is not defined")
     return None

  z =  [[ 0 for _  in range(ycols)] for _ in range(xrows)]   
  for i in range(xrows):
      for j in range(ycols):
      #total = 0
          for k in range(xcols):  
             z[i][j] += x[i][k] * y[k][j]
  return z
       
      # Define two matrices

# Perform matrix multiplication
result = Matrix_Multiplication([[1, 2, 3],[4, 5, 6]], [[7, 8],[9, 10],[11, 12]])

# Print the result
if result:
    for row in result:
        print(row) 

                 
         
 