def min_Heapify(array,index):
	left = index*2
	right = index*2+1
	if left <= len(array)-1 and array[left] < array[index] and array[left] <= array[right]:
		temp = array[left]
		array[left] = array[index]
		array[index] = temp
		min_Heapify(array,left)
	elif right <=len(array)-1 and array[right] < array[index] and array[right] < array[left]:
		temp = array[right]
		array[right] = array[index]
		array[index] = temp
		min_Heapify(array,right)

# array = [0,5,7,1,0,0,4,3]
# print array
# min_Heapify(array,1)
# print array

def max_Heapify(array,index):
	while index <= len(array)-1:
		l = index*2
		r = index*2+1
		if r <= len(array)-1:
			if array[l] > array[index] and array[l] >= array[r]:
				temp = array[l]
				array[l] = array[index]
				array[index] = temp
				index = index*2
			elif array[r] > array[index] and array[r] > array[l]:
				temp = array[r]
				array[r] = array[index]
				array[index] = temp
				index = index*2+1
		elif l <= len(array)-1:
			if array[l] > array[index]:
				temp = array[l]
				array[l] = array[index]
				array[index] = temp
				index = index*2
		else:
			break;

array = [0,16,4,10,14,7,9,3,2,8,1]
print array
max_Heapify(array,2);
print array