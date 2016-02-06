# DOESNT WORK!!!!
# THIS DOES NOT WORK...
def main(array):
	helper(array,0,len(array)-1)

def helper(array,first,last):
	print first,last 
	print array
	if last > first:
		midpoint = partition(array,first,last)
		helper(array,first,midpoint-1)
		helper(array,midpoint+1,last)

def partition(array,first,last):
	midpoint = (first+last)//2
	pivtype = None
	if median(array[first],array[midpoint],array[last]) == array[midpoint]:
		pivot = midpoint
		leftmark = first
		rightmark = last
		# pivtype = 'middle'
	elif median(array[first],array[midpoint],array[last]) == array[first]:
		pivot = first
		leftmark = first+1
		rightmark = last
		# pivtype = 'first'
	else:
		pivot = last
		leftmark = first
		rightmark = last-1
		# pivtype = 'last'
	while True:
		while (leftmark <= rightmark) and array[leftmark] <= array[pivot]:
			leftmark = leftmark + 1
		while (leftmark <= rightmark) and array[rightmark] >= array[pivot]:
			rightmark = rightmark - 1
		if leftmark > rightmark:
			if rightmark > pivot:
				temp = array[rightmark]
				array[rightmark] = array[pivot]
				array[pivot] = temp
				after = True
			else:
				temp = array[leftmark]
				array[leftmark] = array[pivot]
				array[pivot] = temp
				after = False
			# if pivtype = 'middle':
			# 	if leftmark > pivot:
			# 		temp = array[leftmark]
			# 		array[leftmark] = array[pivot]
			# 		array[pivot]  = temp
			# 	else:
			# 		temp = array[rightmark]
			# 		array[rightmark] = array[pivot]
			# 		array[pivot] = temp
			# elif pivtype = 'first':

			break
		else:
			temp = array[rightmark]
			array[rightmark] = array[leftmark]
			array[leftmark] = temp
	if after:
		return rightmark
	else: 
		return leftmark

def median(a,b,c):
	if (c>=a and b<=a) or (c<=a and b>=a):
		return a
	elif (a<=c and b>=c) or (b<=a and a>=c):
		return c
	else:
		return b