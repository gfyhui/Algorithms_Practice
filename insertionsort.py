from copy import copy

def main(array):
	temp = array
	count = 0
	for iteration in range(1,len(array)):
		# print temp
		# print temp
		value = temp[iteration]
		index = iteration-1
		while value < array[index] and index >= 0:
			array[index+1] = array[index]
			index = index - 1
			count = count + 1
		array[index+1] = value
	# print count
	#COUNT IS EQUAL TO THE NUMBER OF INVERSIONS!
	#EVERY SWITCH REMOVES AN INVERSION! 
	#NO INVERSIONS --> SORTED
	return temp
thing = [5,7,9,2,4,1]
print thing
print main(thing)
thing2 = [3,6,5,4]
print thing2
print main(thing2)
thing3 = [7,4,2,5,7,2,4]
print thing3
print main(thing3)

def main2(array):
	temp = copy(array)
	for iteration in range(1,len(array)):
		value = temp[iteration]
		for index in range(iteration-1,-2,-1):
			# print index
			# print temp[index]
			if value < temp[index]:
				temp[index+1] = temp[index]
			else:
				break
		temp[index+1] = value
	return temp

# print main2(thing)