from random import random

def main(array):
	for i in range(1,len(array)):
		curvalue = array[i]
		j = i - 1
		while j >= 0 and curvalue > array[j]:
			array[j+1] = array[j]
			j = j - 1
		array[j+1] = curvalue
	return array

# array = [5,6,2,3,6,1,4]
array = [44,6,3,4,8,9,5,2,113,-3]
print main(array)