'''Python 3'''

# 2 Dimensional Matrix 
matrix2 = [[0 for col in range(4)] for row in range(3)]  # matrix[3][4]
for i in range(len(matrix2)):
	print (matrix2[i])
print()

# 3 Dimensional Matrix
matrix3 = [[[0 for col in range(3)] for row in range(4)] for z in range(2)] # matrix3 [2][4][3]
for i in range (len(matrix3)): 
	for j in range(len(matrix3[i])):
		print (matrix3[i][j])
	print("---------------")

