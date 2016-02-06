class BST:
	def __init__(self):
		self.root = None
		self.size = 0
	def size(self):
		return self.size
	def __len__(self):
		return self.size
	def __iter__(self):
		return self.root.__iter__()
	def __str__(self):
		return '{' + self._str(self.root) + '}'
	def _str(self,curNode):
		if curNode == None:
			return ''
		else:
			exp = '(' + str(curNode.key) + ':' + str(curNode.payload) + ')' 
			return self._str(curNode.leftChild) + exp + self._str(curNode.rightChild)
	def add(self,key,value):
		if self.root == None:
			self.root = TreeNode(key,value)
		else:
			self._add(self.root,key,value)
		self.size = self.size + 1
	def _add(self,curNode,key,value):
		if key < curNode.key:
			if not curNode.hasLeftChild():
				newNode = TreeNode(key,value,parent=curNode)
				curNode.leftChild = newNode
			else:
				self._add(curNode.leftChild,key,value)
		elif key > curNode.key:
			if not curNode.hasRightChild():
				newNode = TreeNode(key,value,parent=curNode)
				curNode.rightChild = newNode
			else:
				self._add(curNode.rightChild,key,value)
		else:
			curNode.replaceNodeData(key,value,curNode.leftChild,curNode.rightChild)
	def __setitem__(self,key,value):
		self.put(key,value)
	def get(self,key):
		node = self._get(self.root,key)
		if node == None:
			return None
		else:
			return self._get(self.root,key).payload
	def _get(self,curNode,key):
		if curNode == None:
			return None
		elif key == curNode.key:
			return curNode
		elif key < curNode.key:
			return self._get(curNode.leftChild,key)
		else:
			return self._get(curNode.rightChild,key)
	def __getitem__(self,key):
		return self.get(key)
	def __contains__(self,key):
		return self._get(self.root,key) != None
	def delete(self,key):
		todelete = self._get(self.root,key)
		if todelete == None:
			raise KeyError('Key not in BST')
		else:
			if todelete.isRoot():
				if todelete.hasBothChildren():
					toreplace = self._findSuccessor(todelete)
					todelete.key = toreplace.key
					todelete.payload = toreplace.payload
					if toreplace.isLeftChild():
						if toreplace.hasRightChild():
							toreplace.rightChild.parent = toreplace.parent
							toreplace.parent.leftChild = toreplace.rightChild
						else:
							toreplace.parent.leftChild = None
					else:
						if toreplace.hasRightChild():
							toreplace.rightChild.parent = toreplace.parent
							toreplace.parent.rightChild = toreplace.rightChild
						else:
							toreplace.parent.rightChild = None
				elif todelete.hasLeftChild():
					self.root = self.root.leftChild
					self.root.parent = None 
				elif todelete.hasRightChild():
					self.root = self.root.rightChild
					self.root.parent = None
				else:
					self.root = None
			else:
				if todelete.hasBothChildren():
					toreplace = self._findSuccessor(todelete)
					todelete.key = toreplace.key
					todelete.payload = toreplace.payload
					if toreplace.isLeftChild():
						if toreplace.hasRightChild():
							toreplace.rightChild.parent = toreplace.parent
							toreplace.parent.leftChild = toreplace.rightChild
						else:
							toreplace.parent.leftChild = None
					else:
						if toreplace.hasRightChild():
							toreplace.rightChild.parent = toreplace.parent
							toreplace.parent.rightChild = toreplace.rightChild
						else:
							toreplace.parent.rightChild = None
				elif todelete.hasLeftChild():
					if todelete.isLeftChild():
						todelete.leftChild.parent = todelete.parent
						todelete.parent.leftChild = todelete.leftChild
					elif todelete.isRightChild():
						todelete.leftChild.parent = todelete.parent
						todelete.parent.rightChild = todelete.leftChild
				elif todelete.hasRightChild():
					if todelete.isLeftChild():
						todelete.rightChild.parent = todelete.parent
						todelete.parent.leftChild = todelete.rightChild
					elif todelete.isRightChild():
						todelete.rightChild.parent = todelete.parent
						todelete.parent.rightChild = todelete.rightChild
				else:
					if todelete.isLeftChild():
						todelete.parent.leftChild = None
					elif todelete.isRightChild():
						todelete.parent.rightChild = None
			self.size = self.size - 1

	def _findSuccessor(self,inputNode):
		curNode = inputNode.rightChild
		while curNode.hasLeftChild():
			curNode = curNode.leftChild
		return curNode


class TreeNode:
	def __init__(self,key,val,left=None,right=None,parent=None):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		self.parent = parent
	def hasLeftChild(self):
		return self.leftChild != None
	def hasRightChild(self):
		return self.rightChild != None
	def isLeftChild(self):
		return self.parent != None and self == self.parent.leftChild
	def isRightChild(self):
		return self.parent != None and self == self.parent.rightChild
	def isRoot(self):
		return self.parent == None
	def isLeaf(self):
		return self.leftChild == None and self.rightChild == None
	def hasAnyChildren(self):
		return self.leftChild != None or self.rightChild != None
	def hasBothChildren(self):
		return self.leftChild != None and self.rightChild != None
	def replaceNodeData(self,key,value,lc,rc):
		self.key = key
		self.payload = value
		self.leftChild = lc 
		self.rightChild = rc
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent = self



# a = BST()
# print a
# a.add(5,'a')
# a.add(3,'b')
# a.add(6,'c')
# a.add(65,'c')
# a.add(-14,'d')
# a.add(4,'c')
# a.add(2,'d')
# a.delete(3)
# a.add(3,'e')
# a.add(7,'f')
# a.add(8,'1')
# a.delete(5)
# a.delete(6)
# print a