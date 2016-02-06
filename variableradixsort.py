# PROGRAM UNFINISHED: DOESNT WORK YET

def unevenLength(array):
	count = 0 #Number of guarenteed sorted elements
	digit = 0 #Current digit of the radix sort
	while count < len(array)-1: #The last elem will automatically be sorted
		count, array = countingsort(array,count,digit)
		digit = digit + 1

def countingsort(array,count,digit):
	C = [count] * 10
	D = [None] * len(array)
	E = [0] * len(array)
	for i in range(len(array)):
		E[i] = array[i]

	newcount = count
	for i in range(len(array)-1,count-1,-1):
		D[i] = array[i]/(10**digit)
		if D[i] == 0:
			newcount = newcount + 1
		D[i] = D[i]%10

	for j in range(count,len(array)):
		C[D[j]] = C[D[j]] + 1

	for j in range(1,10):
		C[j] = C[j] + C[j-1]

	for k in range(len(array)-1,count-1,-1):
		print array
		array[C[D[k]]-1] = E[k]
		C[D[k]] = C[D[k]] - 1

	return newcount,array

array = [674,541,78,5,7424,8521,432,4]
print array
unevenLength(array)
print array