from stack import Stack 

def checkpars(word):
	s = Stack()
	for letter in word:
		if letter == '(':
			s.push(1)
		elif letter == ')':
			if s.size() == 0:
				return False
			else:
				s.pop()
	if s.size() == 0:
		return True
	else:
		return False

ex = '3((0)(3(()33)))'
print checkpars(ex)
ex2 = '(()))'
print checkpars(ex2)
ex3 = '(()))('
print checkpars(ex3)