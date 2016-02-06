def preorder(root):
	if root != None:
		print root
		preorder(root.getLeft())
		preorder(root.getRight())

def inorder(root):
	if root != None:
		inorder(root.getLeft())
		print root
		inorder(root.getRight())

def postorder(root):
	if root != None:
		postorder(root.getLeft())
		postorder(root.getRight())
		print root