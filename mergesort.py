def main(array):
	if len(array) == 1:
		return array
	else:
		midpoint = len(array)//2
		lefthalf = main(array[0:midpoint])
		righthalf = main(array[midpoint:len(array)])
		i = 0
		j = 0
		k = 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				array[k] = lefthalf[i]
				i = i + 1
			else:
				array[k] = righthalf[j]
				j = j + 1
			k = k + 1
		while i < len(lefthalf):
			array[k] = lefthalf[i]
			i = i + 1
			k = k + 1
		while j < len(righthalf):
			array[k] = righthalf[j]
			j = j + 1
			k = k + 1
	return array

thing = [55,13,3,6,7,33,22,1,56,61,34,66,32,12,1,75,34,12,886,77,14,2]
# thing = [3,6,7,5,9,11]
# print main(thing)

def sortnoslice(array):
	helper(array,0,len(array)-1)
	return array

def helper(array,p,r):
	# print p
	# print r
	# print array
	if r > p:
		helper(array,p,(r+p)//2)
		helper(array,((r+p)//2)+1,r)
		# mergeNoSentinal(array,p,(r+p)//2,r)
		mergeWithInsertion(array,p,(r+p)//2,r,4)

def insertionsort(array,p,q,r):
	for i in range(q+1,r+1):
		curvalue = array[i]
		j = i - 1
		while j >= p and array[j] > curvalue:
			array[j+1] = array[j]
			j = j - 1
		array[j+1] = curvalue
	return array

# test = [3,5,7,0,2,4]
# print (len(test)-1)//2
# print insertionsort(test,0,(len(test)-1)//2,len(test)-1)

def mergeNoSentinal(array,p,q,r):
	leftlen = q-p+1
	rightlen = r-q
	left = []
	right = []
	for i in range(leftlen):
		left.append(array[p+i])
	for j in range(rightlen):
		right.append(array[q+1+j])
	i = 0
	j = 0
	k = 0
	while i < leftlen and j < rightlen:
		if left[i] <= right[j]:
			array[p+k] = left[i]
			i = i + 1
		else:
			array[p+k] = right[j]
			j = j + 1
		k = k + 1
	while i < leftlen:
		array[p+k] = left[i]
		i = i + 1
		k = k + 1
	while j < rightlen:
		array[p+k] = right[j]
		j = j + 1
		k = k + 1


def mergeWithInsertion(array,p,q,r,k):
	if (r-p+1 <= k):
		insertionsort(array,p,q,r)
	else:
		mergeNoSentinal(array,p,q,r)


def merge(array,p,q,r):
	# print array
	print p
	print q
	print r
	leftlen = q-p+1
	rightlen = r-q
	left = []
	right = []
	for i in range(leftlen):
		left.append(array[p+i])
	# right.append(array[q])
	for j in range(rightlen):
		right.append(array[q+1+j])
	if abs(len(left)-len(right)) > 1:
		raise ValueError('Left and right not partitioned correctly')
	print left
	print right
	left.append(float("inf"))
	right.append(float("inf"))
	# print left
	# print right
	i = 0
	j = 0
	k = 0
	while k < leftlen + rightlen:
		# print left[i]
		# print right[j]
		# print array
		if left[i] <= right[j]:
			array[p+k] = left[i]
			i = i + 1
		else:
			array[p+k] = right[j]
			j = j + 1
		k = k + 1
	# print array
	# return array

print thing
print sortnoslice(thing)
# print thing
# print merge(thing,0,1,3)
# print len(thing)//2
# print thing
# merge(thing,0,len(thing)//2,len(thing)-1)
# print merge(thing,0,len(thing)//2,len(thing)-1)