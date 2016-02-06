#main(array) returns the number of inversions in that array
def main(array):
	return mergesort(0,array,0,len(array)-1)

def mergesort(count,array,p,r):
	if r > p:
		newcount = mergesort(count,array,p,(p+r)//2) + mergesort(count,array,((p+r)//2)+1,r)
		return count + newcount + merge(array,p,(p+r)//2,r)
	else:
		return 0

def merge(array,p,q,r):
	# print p
	# print r
	# print array[p:q+1]
	# print array[q+1:r+1]
	# print array
	numleft = q-p+1
	numright = r-q
	left = []
	right = []
	for i in range(numleft):
		left.append(array[p+i])
	for j in range(numright):
		right.append(array[q+1+j])
	i = 0
	j = 0
	k = 0
	count  = 0
	while i < numleft and j < numright:
		if left[i] <= right[j]:
			array[p+k] = left[i]
			i = i + 1
		else:
			array[p+k] = right[j]
			j = j + 1
			count = count + numleft - i
		k = k + 1
	while i < numleft:
		array[p+k] = left[i]
		i = i + 1
		k = k + 1
	while j < numright:
		array[p+k] = right[j]
		j = j + 1
		k = k + 1
	# print array
	return count

array = [7,4,2,5,7,2,4]
print array
print main(array)

# test = [2,4,5,7,2,4,7]
# print merge(test,0,len(test)//2,len(test)-1)

# test2 = [3,6,4,5]
# print merge(test2,0,len(test2)//2,len(test2)-1)




