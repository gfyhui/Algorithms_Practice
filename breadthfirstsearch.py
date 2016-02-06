from graph import Graph
from graph import Vertex
from queue import Queue

def main(g,start):
	start.distance = 0
	start.predecessor = None
	q = Queue()
	q.enqueue(start)
	while not q.isEmpty():
		current = q.dequeue()
		print current
		for nbrkey in current.getConnections():
			if g.vertices[nbrkey].color == 'white':
				q.enqueue(g.vertices[nbrkey])
				g.vertices[nbrkey].color = 'grey'
				g.vertices[nbrkey].distance = current.distance + 1
				g.vertices[nbrkey].predecessor = current
		current.color = 'black'

from wordladder import buildGraph
d = buildGraph('expressions.txt')
vertkeys = d.vertices.keys()

print vertkeys[0]
main(d,d.vertices[vertkeys[0]])
def printroute(vertex):
	distance = 0
	while vertex.predecessor != None:
		print vertex.getID()
		distance = distance + 1
		vertex = vertex.predecessor
	print str(distance) + '\n'

for vert in vertkeys:
	printroute(d.vertices[vert])