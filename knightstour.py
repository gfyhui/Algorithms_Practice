from graph import Graph
from graph import Vertex

#Knight that visits every square on a chessboard exactly once.
#Can vary dimensions of the chessboard. 

def buildGraph(n):
	g = Graph()
	for r in range(1,n+1):
		for c in range(1,n+1):
			cursquare = locToNum(n,(r,c))
			newVertex = Vertex(cursquare)
			g.vertices[cursquare] = newVertex
			validsquares = getValidSquares(n,r,c)
			for square in validsquares:
				vnum = locToNum(n,square)
				g.vertices[cursquare].addNeighbor(vnum,0)
	return g

def getValidSquares(n,row,col):
	squareList = []
	if col+1 <= n: #Knight not on last row
		if row-2 >= 1:
			squareList.append((row-2,col+1))
		if row+2 <= n:
			squareList.append((row+2,col+1))
	if col+2 <=n:
		if row-1 >= 1:
			squareList.append((row-1,col+2))
		if row+1 <= n:
			squareList.append((row+1,col+2))
	if col-1 >= 1:
		if row-2 >= 1:
			squareList.append((row-2,col-1))
		if row+2 <= n:
			squareList.append((row+2,col-1))
	if col-2 >= 1:
		if row-1 >= 1:
			squareList.append((row-1,col-2))
		if row+1 <= n:
			squareList.append((row+1,col-2))
	return squareList

def locToNum(n,tup):
	r = tup[0]
	c = tup[1]
	col = 1 + (c-1)*n
	return col + (r-1)

def dfs(g,n,path,cur,numSquares):
	print cur.hasVisited
	cur.hasVisited = True
	print cur
	print n
	cur.color = 'grey'
	path.append(cur)
	if n < numSquares:
		nbrList = cur.getConnections()
		i = 0
		done = False
		while i < len(nbrList) and not done:
			if g.vertices[nbrList[i]].color == 'white':
				done = dfs(g,n+1,path,g.vertices[nbrList[i]],numSquares)
			i = i + 1
		if not done:
			path.pop()
			cur.color = 'white'
	else:
		done = True
	return done

g = buildGraph(8)
for vertKey in g.vertices:
	g.vertices[vertKey].color = 'white'
dfs(g,1,[],g.vertices[1],57)