class Vertex:
	def __init__(self,key):
		self.hasVisited = False
		self.id = key
		self.connectedTo = {}
		self.distance = None
		self.predecessor = None
		self.color = 'white'
	def addNeighbor(self,nbr,weight):
		self.connectedTo[nbr] = weight
	def __str__(self):
		return str(self.id) + ' Connected to: ' + self.connectedTo.__str__()
	def getConnections(self):
		return self.connectedTo.keys()
	def getID(self):
		return self.id
	def getWeight(self,nbr):
		if not nbr in self.connectedTo:
			raise KeyError('Vertex ' + str(self.id) + 'has no such neighbor')
		else:
			return self.connectedTo[nbr]

class Graph:
	def __init__(self):
		self.vertices = {}
		self.numVertices = 0
	# def addVertex(self,key):
	# 	self.numVertices = self.numVertices + 1
	# 	self.vertices[key] = Vertex(key)
	# def getVertex(self,key):
	# 	if key in self.vertices:
	# 		return self.vertices[key]
	# 	else:
	# 		return None
	# def __contains__(self,key):
	# 	return key in self.vertices
	# def addEdge(self,frm,to,cost=0):
	# 	if not frm in self.vertices:
	# 		self.vertices[frm] = Vertex(frm)
	# 	if not to in self.vertices:
	# 		self.vertices[to] = Vertex(to)
	# 	self.vertices[frm].addNeighbor(to,cost)
	# def getVertices(self):
	# 	return self.vertices.keys()
	# def __iter__(self):
	# 	return iter(self.vertices.values())
	def __str__(self):
		toprint = ''
		for key in self.vertices:
			toprint = toprint + self.vertices[key].__str__() + '\n'
		return toprint

# g = Graph()
# for i in range(1,7):
# 	g.addVertex(i)
# for c in range(2,6):
# 	# g.vertices[c].addNeighbor(c+1,c)
# 	# g.vertices[c].addNeighbor(c-1,c)
# 	g.addEdge(c,c+1,c)
# 	g.addEdge(c,c-1,c)

# print g

