import random

def main(array):
	QS(array,0,len(array)-1)

def main2(array):
	QS2(array,0,len(array)-1)

def QS(array,p,r):
	if r>p:
		q = partition(array,p,r)
		QS(array,p,q-1)
		QS(array,q+1,r)

def partition(A,p,r):
	# print A[p:r]
	if r>p:
		a = random.randrange(p,r)
		temp = A[a]
		A[a] = A[r]
		A[r] = temp
	pivot = A[r]
	i = p - 1
	for j in range(p,r):
		if A[j] <= pivot:
			i = i + 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
	i = i + 1
	A[r] = A[i]
	A[i] = pivot
	return i

def QS2(array,p,r):
	if r>p:
		q,t = partition2(array,p,r)
		# print array[p:q+1],array[t:r+1]
		QS2(array,p,q)
		QS2(array,t,r)

def partition2(A,p,r):
	a = random.randrange(p,r)
	temp = A[a]
	A[a] = A[r]
	A[r] = temp
	pivot = A[r]
	t = p - 1
	i = p - 1
	for j in range(p,r):
		if A[j] < pivot:
			t = t + 1
			temp = A[t]
			A[t] = A[j]
			A[j] = temp
			temp2 = A[t]
			i = i + 1
			A[t] = A[i]
			A[i] = temp2
		elif A[j] == pivot:
			t = t + 1
			A[j] = A[t]
			A[t] = pivot
	t = t + 1
	A[r] = A[t]
	A[t] = pivot
	t = t + 1;
	return i,t

# array = [6,3,4,1,6,3,4,6,8,4,1,3,4]
# array = [5,6,1,3,4,7,5,1,3,7,3,-1,3,4]
# print array
# main2(array)
# print array