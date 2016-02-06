def main(word):
	if len(word) == 1:
		return word
	else:
		return word[len(word)-1:] + main(word[:len(word)-1])