def main(array):
	helper(array,0,len(array)-1)
	return array

def helper(array,first,last):
	if first < last: #If len(array) <= 1, then it's already sorted.
		splitpoint = partition(array,first,last)

		helper(array,first,splitpoint-1)
		helper(array,splitpoint+1,last)

def partition(array,first,last):
	leftmark = first+1
	rightmark = last
	pivotvalue = array[first]
	while True:
		while (leftmark <= rightmark) and (array[leftmark] <= pivotvalue):
			leftmark = leftmark + 1
		while (rightmark >= leftmark) and (array[rightmark] >= pivotvalue):
			rightmark = rightmark - 1
		if leftmark > rightmark:
			temp = array[rightmark]
			array[rightmark] = pivotvalue
			array[first] = temp
			break
		else:
			temp = array[rightmark]
			array[rightmark] = array[leftmark]
			array[leftmark] = temp
	return rightmark

# thing = [5,2,9,9,3,6,1,3,4]
# print thing
# print main(thing)