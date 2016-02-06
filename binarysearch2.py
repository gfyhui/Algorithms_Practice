def main(array,value):
	if len(array) == 0:
		return False
	else:
		if array[len(array)//2] == value:
			return True
		elif array[len(array)//2] < value:
			return main(array[(len(array)//2)+1:len(array)],value)
		else:
			return main(array[0:len(array)//2],value)

def iterative(array,value):
	found = False
	temp = array
	while True:
		if len(temp) == 0:
			break
		midpoint = len(temp)//2
		if temp[midpoint] == value:
			found = True
			break
		elif temp[midpoint] < value:
			temp = temp[midpoint+1:]
		else:
			temp = temp[:midpoint]
	return found

def noslice(array,value):
	return helper(array,value,0,len(array)-1)

def helper(array,value,first,last):
	if last<first:
		return False
	else:
		midpoint = (first+last)//2
		if array[midpoint] == value:
			return True
		elif array[midpoint] < value:
			return helper(array,value,midpoint+1,last)
		else:
			return helper(array,value,first,midpoint-1)

thing = [1,2,3,5,6,7,8,8]
print noslice(thing,5)