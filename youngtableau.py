def extractMin(A):
	minimum = A[0][0]
	rebalance(A,0,0)
	return minimum

def rebalance(A,row,col):
	smallest = float("inf")
	if row<len(A)-1:
		smallest = A[row+1][col]
		inRow = True
	if col<len(A[0])-1:
		if A[row][col+1] < smallest:
			smallest = A[row][col+1]
			inRow = False
	if smallest < float("inf"):
		A[row][col] = smallest
		if inRow:
			A[row+1][col] = float("inf")
			rebalance(A,row+1,col)
		else:
			A[row][col+1] = float("inf")
			rebalance(A,row,col+1)

def insert(A,value):
	row = len(A)-1
	col = len(A[0])-1
	while row >= 0 and col >= 0:
		greatest = -float("inf")
		if row > 0:
			greatest = A[row-1][col]
			toUp = True
		if col > 0:
			if A[row][col-1] > greatest:
				greatest = A[row][col-1]
				toUp = False
		if greatest > value:
			A[row][col] = greatest
		else:
			A[row][col] = value
			break;
		if toUp:
			row = row - 1
		else:
			col = col - 1

def inTableau(A,value):
	row = 0
	col = 0
	

# A = [[1,2,5],[3,4,8],[7,9,10]]
# for i in range(4):
# 	print A
# 	extractMin(A)

# print A
# insert(A,2)
# print A
# insert(A,5)
# print A
# insert(A,6)
# print A
