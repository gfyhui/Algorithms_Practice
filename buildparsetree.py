from binarytree import BinaryTree
from stack import Stack
operator = ['*','+','-','/']

def main(inputexp):
	nospaces = inputexp.replace(' ','')
	return buildtree(nospaces)

def buildtree(exp):
	parents = Stack()
	tree = BinaryTree(None)
	current = tree
	curnum = ''
	for index in range(len(exp)):
		# print parents
		if exp[index] == '(':
			current.addLeft(None)
			parents.push(current)
			current = current.getLeft()
			nextnum = False
		elif exp[index] in operator:
			current.setRootVal(exp[index])
			parents.push(current)
			current.addRight(None)
			current = current.getRight()
			nextnum = False
		elif exp[index] == ')':
			if parents.isEmpty():
				return current
			else:
				current = parents.pop()
			nextnum = False
		elif exp[index].isdigit():
			curnum = curnum + exp[index]
			if not exp[index+1].isdigit():
				current.setRootVal(curnum)
				current = parents.pop()
				curnum = ''
		else:
			raise ValueError('Contains unknown expression')

	return current

def evaltree(exp):
	if exp.isLeaf():
		return int(exp.getRootVal())
	elif exp.getRootVal() == '+':
		return int(evaltree(exp.getLeft())) + int(evaltree(exp.getRight()))
	elif exp.getRootVal() == '-':
		return int(evaltree(exp.getLeft())) - int(evaltree(exp.getRight()))
	elif exp.getRootVal() == '/':
		return int(evaltree(exp.getLeft()))//int(evaltree(exp.getRight()))
	elif exp.getRootVal() == '*':
		return int(evaltree(exp.getLeft())) * int(evaltree(exp.getRight()))
	else:
		return 'huh?'

def retrieveTree(root):
	if root != None:
		return retrieveTree(root.getLeft()) + root.getRootVal() + retrieveTree(root.getRight())
	else:
		return ''


def getOriginal(root):
	if root == None:
		return ''
	elif root.isLeaf():
		return root.getRootVal()
	else:
		return '(' + getOriginal(root.getLeft()) + root.getRootVal() + getOriginal(root.getRight()) + ')'


a = '(71*(52-(9*8)))'
print a
d = main(a)
print getOriginal(d)

