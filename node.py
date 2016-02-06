class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None
	def getValue(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,newdata):
		self.data = newdata
	def setNext(self,newnext):
		self.next = newnext
	def __str__(self):
		temp = self.next
		toprint = [str(self.data)]
		while temp != None:
			toprint.append(str(temp.data))
			temp = temp.next
		toprint = ' --> '.join(toprint)
		return toprint
	def append(self,newdata):
		newNode = Node(newdata)
		current = self
		while current.next != None:
			current = current.next
		current.next = newNode

class NodeWithMin:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None
		self.min = None
	def getValue(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,newdata):
		self.data = newdata
	def setNext(self,newnext):
		self.next = newnext
	def __str__(self):
		temp = self.next
		toprint = [str(self.data)]
		while temp != None:
			toprint.append(str(temp.data))
			temp = temp.next
		toprint = ' --> '.join(toprint)
		return toprint
	def append(self,newdata):
		newNode = Node(newdata)
		current = self
		while current.next != None:
			current = current.next
		current.next = newNode