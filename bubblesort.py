sample = [5,7,9,2,4,1]


def main(array):
	for iteration in range(len(array)-1,0,-1):
		hasswap = False
		for index in range(iteration):
			print array
			temp = array[index]
			if array[index] > array[index+1]:
				array[index] = array[index+1]
				array[index+1] = temp
				hasswap = True
		if hasswap == False:
			return array
	return array

# print sample
main(sample)