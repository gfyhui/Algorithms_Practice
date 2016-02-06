from node import Node

class OrderedList:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		if self.head == None:
			return True
		else:
			return False
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
	def size(self):
		count = 0
		current = self.head
		while current != None:
			current = current.getNext()
			count = count + 1
		return count
	def remove(self,item):
		previous = None
		current = self.head
		if current.getValue() == item:
			self.head = current.getNext()
		else:
			while current.getValue() != item:
				previous = current
				current = current.getNext()
				if current == None:
					break
			if current.getValue() == item:
				previous.setNext(current.getNext())
			else:
				return -1
	def search(self,item):
		current = self.head
		while current != None:
			if current.getValue() == item:
				return True
			elif current.getValue() > item:
				return False
			else:
				current = current.getNext()
		return False
	def add(self,item):
		newNode = Node(item)
		if self.head == None:
			self.head = newNode
		else:
			previous = None
			current = self.head
			if current.getValue() > newNode.getValue():
				newNode.setNext(self.head)
				self.head = newNode
			else:
				while current != None:
					if current.getValue() > item:
						previous.setNext(newNode)
						newNode.setNext(current)
						break
					else:
						previous = current
						current = current.getNext()
					if current == None:
						previous.setNext(newNode)
