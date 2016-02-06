def stable(array,k):
	C = [0] * (k+1)
	for num in array:
		C[num] = C[num] + 1
	for i in range(1,k+1):
		C[i] = C[i] + C[i-1]
	B = [None] * len(array)
	# print len(B)
	for i in range(len(array)-1,-1,-1):
		B[C[array[i]]-1] = array[i]
		C[array[i]] = C[array[i]] - 1
	return B

def unstable(array,k):
	C = [0] * (k+1)
	for num in array:
		C[num] = C[num] + 1
	for i in range(1,k+1):
		C[i] = C[i] + C[i-1]
	count = 0
	for j in range(len(array)):
		if j < C[count]:
			array[j] = count
		else:
			while j == C[count]:
				count = count + 1
			array[j] = count




array = [6,1,4,0,6,1,0,4,1,6,4,1]
print array
# print stable(array,6)
unstable(array,6)
print array