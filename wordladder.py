from graph import Graph
from graph import Vertex

def buildGraph(wordList):
	d = {}
	g = Graph()
	text = open(wordList,'r')
	for line in text:
		word = line[:-1]
		g.vertices[word] = Vertex(word)
		for i in range(len(word)):
			newKey = word[:i] + '_' + word[i+1:]
			if newKey in d:
				d[newKey].append(word)
			else:
				d[newKey] = [word]
	# print d
	for key in g.vertices:
		# print key
		for bucket in d:
			if key in d[bucket]:
				for thing in d[bucket]:
					# print thing
					if thing != key:
						g.vertices[key].addNeighbor(thing,0)
	return g

# d = buildGraph('expressions.txt')
# print d