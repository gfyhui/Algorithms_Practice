from stack import Stack
def main(word):
	s = Stack()
	for letter in word:
		s.push(letter)
	newword = ""
	while not s.isEmpty():
		newword = newword + str(s.pop())
	return newword

# s = "hello!"
# print s
# print main(s)