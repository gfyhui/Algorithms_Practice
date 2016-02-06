class Queue:
	def __init__(self):
		self.items = []
	def enqueue(self,elem):
		self.items.insert(0,elem)
	def isEmpty(self):
		return self.items == []
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def __str__(self):
		return str(self.items)


class QueueOpposite:
	def __init__(self):
		self.items = []
	def dequeue(self):
		return self.items.pop(0)
	def isEmpty(self):
		self.items == []
	def enqueue(self,item):
		self.items.append(item)
	def size():
		return len(self.items)
	def __str__(self):
		return str(self.items)

