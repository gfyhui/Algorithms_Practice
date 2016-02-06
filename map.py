from linkedlist import LinkedList 

class Map:
	def __init__(self,inputsize):
		self.size = inputsize
		self.data = []
		self.keys = []
		for i in range(self.size):
			self.data.append(LinkedList())
			self.keys.append(LinkedList())

	def hashfunction(self,key,tablesize):
		if type(key) == str:
			total = 0
			for index in range(len(key)):
				total = total + (index+1)*ord(key[index])
				return total%tablesize
		elif type(key) == int:
			return key%tablesize

	def __contains__(self,key):
		index = self.hashfunction(key,self.size)
		return self.keys[index].search(key) 

	def get(self,key):
		hashval = self.hashfunction(key,self.size)
		count = self.keys[hashval].index(key)
		return self.data[hashval].peek(count)

	def put(self,key,value):
		hashval = self.hashfunction(key,self.size)
		index = self.keys[hashval].index(key)
		if index == -1: #It is a new key
			self.keys[hashval].add(key)
			self.data[hashval].add(value)
		else:
			self.data[hashval].replace(index,value)

	def __len__(self):
		count = 0
		for elem in self.keys:
			count = count + elem.size()
		return count

	def __delitem__(self,key):
		hashval = self.hashfunction(key,self.size)
		index = self.keys[hashval].index(key)
		if index >= 0: #the key is in the map
			self.data[hashval].pop(index)
			self.keys[hashval].pop(index)

	def __str__(self):
		toprint = 'KEYS:\n'
		for elem in self.keys:
			if elem.isEmpty():
				toprint = toprint + '##' + '\n'
			else:
				toprint = toprint + elem.__str__() + '\n'
		toprint = toprint + '\nDATA:\n'
		for elem in self.data:
			if elem.isEmpty():
				toprint = toprint + '##' + '\n'
			else:
				toprint = toprint + elem.__str__() + '\n'
		return toprint
