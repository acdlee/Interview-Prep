#base code to create a graph and strucutre the program
#from geeksforgeeks and Neelam Yadav

#O(V+E) solution using BFS (time)
#O(V) space since we're storing the number
#of veritices in visited
from collections import defaultdict

#This class represents a directed graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
	
	# Use BFS to check path between s and d
	def isReachable(self, s, d):
		visited = [False] * self.V
		queue = [s]
		visited[s] = True

		while queue:
			curr = queue.pop(0)
			if curr == d:
				return True

			for adj in self.graph[curr]:
				if not visited[adj]:
					visited[adj] = True
					queue.append(adj)

		return False


# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

u =1; v = 3

if g.isReachable(u, v):
	print("There is a path from %d to %d" % (u,v))
else :
	print("There is no path from %d to %d" % (u,v))

u = 3; v = 1
if g.isReachable(u, v) :
	print("There is a path from %d to %d" % (u,v))
else :
	print("There is no path from %d to %d" % (u,v))

#This code is contributed by Neelam Yadav