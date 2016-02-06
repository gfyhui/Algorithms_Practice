def main(A):
	smallest = A[0]
	second = A[0] + A[1]
	for i in range(1,len(A)):
		if A[i] < second:
			if A[i] < smallest:
				second = smallest
				smallest = A[i]
			else:
				second = A[i]
	return second

# A = [6,4,6,5,1]
# print A
# print main(A)