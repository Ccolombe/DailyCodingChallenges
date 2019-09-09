#dailyCodingChallenge168.py

import copy

'''
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
'''


# Below is the O(N^2) time and space naive algorithm

def rotate90Deg(matrix):
	"""
	Rotates an N x N matrix by 90 degrees clockwise
	"""
	n = len(matrix)

	newMatrix = [ n * [0] for i in range(n) ]

	for i in range(1, n + 1):

		# Get the rows of the original matrix
		currentRow = matrix[i - 1]

		# set the columns of the newMatrix equal to the 
		#rows of the original matrix moving left to right
		for j in range(n):
			newMatrix[j][-i] = currentRow[j]

	# Copy the newMatrix over into the original matrix
	for i in range(n):
		for j in range(n):

			matrix[i][j] = newMatrix[i][j]



def displayMatrix(matrix):
	"""
	Displays a matrix in a more readable way
	"""

	for row in matrix:
		print(row)

def constantSpaceRotate(A):
	"""
	Perform a 90 deg clockwise rotation of matrix A in constant space and quadratic time.

	"""
	n = len(A)

	rowNum = 0
	colNum = 0

	while rowNum < n / 2:
		for i in range(colNum,n - 1 - colNum):

			fourwaySwap(A,rowNum,i)

		rowNum += 1
		colNum += 1

def fourwaySwap(A,i,j):
	"""
	shfits the four elements of a 90 deg rotation cycle 
	in place. The cycle of A[i][j] is computed and then shifted
	by one 90 deg rotation.	
	"""	

	n = len(A)
	mid = n //2
	# We check that the entry is not the invariant middle entry in a 
	# odd length matrix 
	if  not(n % 2 == 1 and i == mid and j == mid):

		# Calculate the rotation cycles of A[i][j]
		t1 = A[i][j]

		t2 = A[j][ (n - 1) - i]

		t3 = A[ (n - 1) - i][(n - 1) - j]

		t4 = A[ (n - 1) - j][i]


		# update each location to its next value in the cycle
		A[j][ (n - 1) - i] = t1

		A[(n - 1) -i][n - 1 -j] = t2

		A[(n - 1) - j][i] = t3

		A[i][j] = t4

		

def makesSeqSquareMatrix(N):
	"""
	Make an N x N matrix with consequtive integer entries for testing
	"""

	# Initilize empty N x N matrix
	matrix = [ N * [0] for i in range(N)]

	# Fill the matrix row by row with sequentially increasing integers
	for i in range(N ** 2):

		row = i // N
		col = i % N

		matrix[row][col] = i

	return matrix



if __name__ == '__main__':

	test = makesSeqSquareMatrix(5)

	
	
	displayMatrix(test)
	constantSpaceRotate(test)

	
	displayMatrix(test)

	





