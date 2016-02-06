def main(array):
	bestCase = True
	for q in range(len(array)-1): #Best case scenario hard-coded
		if array[q] > array[q+1]:
			bestCase = False
			break
	if bestCase:
		print bestCase
		return array
	for i in range(len(array)-1):
		print 'hi'
		minindex = i
		found = False
		for j in range(i+1,len(array)):
			if array[j] < array[minindex]:
				found = True
				minindex = j
		if found:
			temp = array[i]
			array[i] = array[minindex]
			array[minindex] = temp
	return array

# array = [-3,9,-2,6,2,4,5,1,3,6]
# print main(array)
array = [5,6,5,7,8,9,9]
print main(array)