class MinHeap:
	def __init__(self):
		self.maxNumElements = 100
		self.heapList = [0]
		self.currentSize = 0
	def insert(self,value):
		current = self.currentSize + 1
		self.heapList.append(value)
		while current > 0 and value < self.heapList[current/2]:
			temp = self.heapList[current/2]
			self.heapList[current/2] = value
			self.heapList[current] = temp
			current = current/2
		self.currentSize = self.currentSize + 1
	def isEmpty(self):
		return self.currentSize == 0
	def size(self):
		return self.currentSize
	def getList(self):
		return self.heapList
	def getMin(self):
		if not self.isEmpty():
			return self.heapList[1]
	def delMin(self):
		if self.isEmpty():
			raise ValueError('Cannot remove element from empty heap')
		elif self.currentSize == 1:
			return self.heapList.pop()
		else:
			toreturn = self.heapList[1]
			self.heapList[1] = self.heapList.pop()
			self.currentSize = self.currentSize - 1
			index = 1
			while True:
				if (index*2)+1 > self.currentSize:
					if index*2 <= self.currentSize:
						if self.heapList[index] > self.heapList[index*2]:
							temp = self.heapList[index]
							self.heapList[index] = self.heapList[index*2]
							self.heapList[index*2] = temp
					break
				else:
					if self.heapList[index*2] < self.heapList[index]:
						temp = self.heapList[index]
						if self.heapList[index*2] < self.heapList[index*2+1]:
							self.heapList[index] = self.heapList[index*2]
							self.heapList[index*2] = temp
							index = index * 2
						else:
							self.heapList[index] = self.heapList[index*2+1]
							self.heapList[index*2+1] = temp
							index = (index * 2) + 1
					elif self.heapList[index*2+1] < self.heapList[index]:
						temp = self.heapList[index]
						self.heapList[index] = self.heapList[index*2+1]
						self.heapList[index*2+1] = temp
						index = (index * 2) + 1
					else:
						break
			return toreturn



