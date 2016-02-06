from node import Node

class LinkedList:
	def __init__(self):
		self.head = None
	# def setTail(self):
	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
	def isEmpty(self):
		if self.head == None:
			return True
		else:
			return False
	def append(self,item):
		newNode = Node(item)
		temp = self.head
		if temp == None:
			self.head = newNode
		else:
			while temp.getNext() != None:
				temp = temp.getNext()
			temp.setNext(newNode)
	def insert(self,index,item):
		if index > self.size() or index < 0:
			raise ValueError('Index out of bounds')
		elif index == 0:
			temp = Node(item)
			temp.setNext(self.head)
			self.head = temp
		else:
			count = 0
			current = self.head
			for i in range(index-1):
				current = current.getNext()
			newNode = Node(item)
			newNode.setNext(current.getNext())
			current.setNext(newNode)
	def size(self):
		count = 0
		temp = self.head
		while temp != None:
			temp = temp.getNext()
			count = count + 1
		return count
	def search(self,item):
		temp = self.head
		while temp != None:
			if temp.getValue() == item:
				return True
			else:
				temp = temp.getNext()
		return False
	# Returns the index of the first instance of Node with value item
	def index(self,item):
		curindex = 0
		current = self.head
		while current != None and current.getValue() != item:
			current = current.getNext()
			curindex = curindex + 1
		if current == None:
			return -1
		else:
			return curindex
		return curindex
	def peek(self,index):
		curindex = 0
		current = self.head
		if index == 0:
			value = current.getValue()
		elif index < 0 or index >= self.size():
			return None
		else:
			while curindex < index:
				current = current.getNext()
				curindex = curindex + 1
			value = current.getValue()
		return value
	def pop(self,index):
		curindex = 0
		current = self.head
		previous = None
		if index == 0:
			value = current.getValue()
			self.head = current.getNext()
			return value
		elif index < 0 or index >= self.size():
			raise ValueError('Index out of bounds')
		else:
			while curindex < index:
				previous = current
				current = current.getNext()
				curindex = curindex + 1
			value = current.getValue()
			previous.setNext(current.getNext())
			return value
	def replace(self,index,item):
		current = self.head
		count = 0
		while current!=None and count<index:
			current = current.getNext()
			count = count + 1
		if current == None:
			raise ValueError('Index out of bounds')
		else:
			current.setData(item)

	def remove(self,item):
		current = self.head
		previous = None
		while current != None:
			if current.getValue() == item:
				if current == self.head:
					self.head = current.getNext()
					break
				else:
					previous.setNext(current.getNext())
					break
			else:
				previous = current
				current = current.getNext()
	def __str__(self):
		current = self.head
		toprint = ""
		while current != None:
			if current.getNext() == None:
				toprint = toprint + str(current.getValue())
			else:
				toprint = toprint + str(current.getValue()) + " --> "
			current = current.getNext()
		return toprint