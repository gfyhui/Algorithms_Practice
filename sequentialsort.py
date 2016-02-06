def main(array,value):
	# print array
	if len(array) == 0:
		return False
	else:
		midpoint = len(array)//2
		if array[midpoint] == value:
			return True
		elif array[midpoint] < value:
			return main(array[midpoint+1:len(array)],value)
		else:
			return main(array[0:midpoint],value)