from binheap import MinHeap
class PriorityQueue():
	def __init__(self):
		self.queue = BinHeap()
	def enqueue(self,elem):
		self.queue.insert(elem)
	def dequeue(self):
		return self.queue.delMin()
	def peek(self):
		return self.queue.getMin()
	def size(self):
		return self.queue.size()

# a = PriorityQueue()
# a.enqueue(5)
# a.enqueue(2)
# a.enqueue(7)
# a.enqueue(8)
# print a.dequeue()
# print a.dequeue()
# a.enqueue(8)
# print a.dequeue()
# print a.dequeue()
