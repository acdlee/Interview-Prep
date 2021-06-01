# O(M*N) time; O(M+N) space
def setZero(M):
	if not M: return M
	zero_row, zero_col = [], []	#indicies of zero's in M
	A, B = len(M), len(M[0])
	
	for i in range(A): 		#loop through each row
		for j in range(B):	#loop through each col
			if not M[i][j]:	#record zeros
				zero_row.append(i)
				zero_col.append(j)

	#create zero rows
	for row in zero_row:
		for j in range(B):
			M[row][j] = 0

	#create zero cols
	for col in zero_col:
		for i in range(A):
			M[i][col] = 0

	return M

#O(M*N) t; O(1) space
def betterSetZero(M):
	if not M: return M
	#create variables to record if our data row/col has zeros
	has_zero_row, has_zero_col = False, False

	#search for a zero in the first row
	for i in range(len(M[0])):
		if not M[0][i]:
			has_zero_row = True
			M[0][i] = 1 		#set non-zero default value

	#search for a zero in the first col
	for i in range(len(M)):
		if not M[i][0]:
			has_zero_col = True
			M[i][0] = 1 		#set non-zero default value

	#Matrix M's dimensions
	A, B = len(M), len(M[0])
	
	for i in range(A): 		#loop through each row
		for j in range(B):	#loop through each col
			if not M[i][j]:	#record zeros
				M[i][0] = 0
				M[0][j] = 0

	#check our data row for 0's; fill 0 rows with all 0's
	for i in range(A):
		if not M[i][0]:
			for j in range(B):
				M[i][j] = 0

	#check our data col for 0's; fill 0 cols with all 0's			
	for j in range(B):
		if not M[0][j]:
			for i in range(A):
				M[i][j] = 0


	#check if we need to fill the first row or col with 
	#zeros (our data row and col)
	if has_zero_row:
		for i in range(len(M[0])):
			M[0][i] = 0

	if has_zero_col:
		for i in range(len(M)):
			M[i][0] = 0


	return M