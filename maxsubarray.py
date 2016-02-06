def bruteForce(array):
	leftindex = 0
	rightindex = 0
	largest = array[0]
	count = 0
	for i in range(len(array)):
		for j in range(i,len(array)):
			count = count + 1
			# print array[j]
			total = 0
			# print array[i:j+1]
			for k in range(i,j+1):
				total = total + array[k]
			if total > largest:
				largest = total
				leftindex = i
				rightindex = j
	# print len(array)
	# print (len(array))**2
	# print count
	# if (largest > 0):
	# 	return (leftindex,rightindex,largest)
	# else:
	# 	return (-1,-1,0)
	return (leftindex,rightindex,largest)

# print bruteForce([-5,-3,-3,-1])
# thing = [10,1,-5,4,-2,3,1,-20,2,6,-2,3,-5,2,-100,2,3,4]
# (start,finish,total) = bruteForce(thing)
# print thing
# print thing[start:finish+1]

def divAndConquer(array):
	return findMaxSubarray(array,0,len(array)-1)

def findMaxCrossingSubarray(array,left,mid,right):
	leftmax = array[mid]
	leftindex = mid
	leftsum = array[mid]
	for i in range(mid-1,left-1,-1):
		leftsum = leftsum + array[i]
		if leftsum > leftmax:
			leftmax = leftsum
			leftindex = i
	rightmax = array[mid+1]
	rightindex = mid + 1
	rightsum = array[mid+1]
	for j in range(mid+2,right+1):
		rightsum = rightsum + array[j]
		if rightsum > rightmax:
			rightmax = rightsum
			rightindex = j
	totalmax = leftmax + rightmax
	return (leftindex,rightindex,totalmax)

def findMaxSubarray(array,left,right):
	# print str(left)
	# print str(right) + '\n'
	if left == right:
		return (left,right,array[left])
	else:
		mid = (left+right)//2
		(leftfirst,leftlast,leftmax) = findMaxSubarray(array,left,mid)
		(rightfirst,rightlast,rightmax) = findMaxSubarray(array,mid+1,right)
		(crossfirst,crosslast,crossmax) = findMaxCrossingSubarray(array,left,mid,right)
		if leftmax >= rightmax and leftmax >= crossmax:
			return (leftfirst,leftlast,leftmax)
		elif rightmax > leftmax and rightmax >= crossmax:
			return (rightfirst,rightlast,rightmax)
		else:
			return (crossfirst,crosslast,crossmax)

# thing = [10,1,-5,4,-2,3,1,-20,2,6,-2,3,-5,2,7,4,-10,7,3,-5,4]
# thing = [1,3,-4,5,-2,5,-2,-3,6,1,-2,3]
# print thing
# (start,finish,total) = divAndConquer(thing)
# print thing[start:finish+1]

def linearTime2(array):
	
	return (maxLeft,maxRight,maxSum)

test = [5,10,3,4,7,11,12,3,5,4,16,15]
print test
print linearTime2(test)

def linearTime(array):
	allleft = 0
	allright = 0
	allmax = array[0]
	lastleft = 0
	lastright = 0
	lastmax = array[0]
	for i in range(1,len(array)):
		# print array[allleft:allright+1]
		# print array[lastleft:lastright+1]
		if lastmax > 0:
			lastmax = lastmax + array[i]
		else:
			lastleft = i
			lastmax = array[i]
		lastright = lastright + 1
		if lastmax > allmax:
			allleft = lastleft
			allright = lastright
			allmax = lastmax
	return (allleft,allright,allmax)


# thing = [10,1,-5,4,-2,3,1,-20,2,6,-2,3,-5,2,7,4,-10,7,3,-5,4]
# thing = [1,3,-4,5,-2,5,-2,-3,6,1,-2,3]
# print thing
# (start,finish,total) = linearTime(thing)
# print thing[start:finish+1]
