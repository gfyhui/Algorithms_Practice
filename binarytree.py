class BinaryTree:
	def __init__(self,inputKey):
		self.key = inputKey
		self.leftChild = None
		self.rightChild = None
	def addLeft(self,inputKey):
		newChild = BinaryTree(inputKey)
		temp = self.leftChild
		self.leftChild = newChild
		newChild.leftChild = temp
	def addRight(self,inputKey):
		newChild = BinaryTree(inputKey)
		temp = self.rightChild
		self.rightChild = newChild
		newChild.rightChild = temp
	def isLeaf(self):
		return (self.leftChild == None) and (self.rightChild == None)
	def getRight(self):
		return self.rightChild
	def getLeft(self):
		return self.leftChild
	def setRootVal(self,value):
		self.key = value
	def getRootVal(self):
		return self.key
	def preorder(self):
		print self.getRootVal()
		if self.getLeft() != None:
			preorder(self.getLeft())
		if self.getRight() != None:
			preorder(self.getRight())
	def inorder(self):
		if self.getLeft() != None:
			inorder(self.getLeft())
		print self.getRootVal()
		if self.getRight() != None:
			inorder(self.getLeft())
	def postorder(self):
		if self.getLeft() != None:
			inorder(self.getLeft())
		if self.getRight() != None:
			inorder(self.getLeft())	
		print self.getRootVal()
	def __str__(self):
		toprint = str(self.getRootVal()) + '\n'
		if self.getLeft() != None:
			toprint = toprint + str(self.getLeft().getRootVal())
		if self.getRight() != None:
			toprint = toprint + str(self.getRight().getRootVal())
		return toprint