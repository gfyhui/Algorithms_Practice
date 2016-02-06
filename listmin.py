# Find the minimum of a list

def quadratic(listofnums):
	minimum = listofnums[0]
	for n1 in range(len(listofnums)):
		isSmallest = True
		for n2 in range(len(listofnums)):
			if n1 != n2 and listofnums[n1]>=listofnums[n2]:
				isSmallest = False
				break
		if isSmallest:
			minimum = listofnums[n1]
	return minimum

a = [3,6,4,-5,8,2,-3];
print quadratic(a)

def linear(listofnums):
	minimum = listofnums[0]
	for n in range(len(listofnums)):
		if listofnums[n] < minimum:
			minimum = listofnums[n]
	return minimum

print linear(a)