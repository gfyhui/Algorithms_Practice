def main(array):
	for iteration in range(len(array)-1,-1,-1):
		print array
		maxvalue = array[0]
		maxindex = 0
		for index in range(1,iteration+1):
			if array[index] > maxvalue:
				maxindex = index
				maxvalue = array[index]
		temp = array[iteration]
		array[iteration] = maxvalue
		array[maxindex] = temp
	return array

# thing = [5,7,9,2,4,1]
# main(thing)