def isAnagram(a,b):
	D = dict()
	for letter in a:
		if letter in D:
			D[letter] = D[letter] + 1
		else:
			D[letter] = 1
	for letter in b:
		if letter in D:
			D[letter] = D[letter] - 1
			if D[letter] == 0:
				del D[letter]
		else:
			return False
	if len(D)==0:
		return True
	else:
		return False

def main(array):
	anagramList = []
	for word in array:
		# print anagramList
		inserted = False
		for anagram in anagramList:
			if anagram and isAnagram(word,anagram[0]):
				anagram.append(word)
				inserted = True
				break
		if not inserted:
			anagramList.append([word])
	return anagramList

array = ["ehlol","cab", "cz", "abc", "bca", "zc",'hello']
print array
print main(array)