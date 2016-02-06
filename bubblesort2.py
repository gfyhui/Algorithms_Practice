def main(array):
	for i in range(len(array)-1):
		for j in range(len(array)-1,i,-1):
			print array
			if array[j] < array[j-1]:
				temp = array[j]
				array[j] = array[j-1]
				array[j-1] = temp
	return array

array = [5,6,1,3,4,1,6,7,8,4]
print array
print main(array)