from quicksortclrs import partition
# Returns the ith smallest element from an array
# Divide-and-conquer (uses partition from quicksort)
def iterative(array,i):
	p = 0 
	r = len(array)-1
	k = partition(array,p,r)
	while k != i:
		print array[p:r]
		if k > i:
			r = k - 1
			k = partition(array,p,r)
		else:
			p = k + 1
			k = partition(array,p,r)
	return array[k]


# array = [6,10,3,4,70,54]
# print array
# print iterative(array,4)