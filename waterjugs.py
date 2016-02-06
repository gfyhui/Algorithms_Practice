from stack import Stack

def main():
	gal4 = Stack()
	gal3 = Stack()
	return helper(gal4,gal3)

def helper(g4,g3):
	if not g4.size() == 4:
		