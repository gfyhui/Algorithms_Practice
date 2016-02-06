def positionweight(word,tablesize):
	value = 0
	for index in range(len(word)):
		value = (index+1)*ord(word[index]) + value
	return value%tablesize
