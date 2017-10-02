from makemaze import makeMaze 
from makemaze import meet_neighbors
from print_solution import printSolution
from priorityqueue import PriorityQueue


def heuristic(a,b):
	x1 = a.x
	y1 = a.y
	x2 = b.x
	y2 = b.y
	return abs(x1 - x2) + abs(y1 - y2)

def calcDist(node1, node2):
	dist = (abs(node1.x - node2.x)**2 + abs(node1.y - node2.y)**2)**(1/2)
	#print(node1.x, node1.y, node2.x, node2.y, dist)
	return dist

def getEdges(node, other_nodes):
	# curr, neighbor, dist
	edges = []
	for o_node in other_nodes:
		 dist = calcDist(node, o_node)
		 #print(dist)
		 if dist != 0:
		 	edges.append((node, o_node, dist))
	return edges

def findMST(start, goals):
	MST = []
	visited = {x:False for x in goals}
	visited[start] = 0
	priqueue = PriorityQueue()
	if len(goals) == 0:
		return 0
	for node, was_visited in visited.items():
		#print(MST)
		#print(visited)
		if was_visited == False:
			was_visited = True
			edges_from_node = getEdges(node, visited.keys())
			#print(edges_from_node)
			for edge in edges_from_node:
				priqueue.push(edge, edge[2])
			if not priqueue.empty():
				min_edge = priqueue.pop()
				if visited[min_edge[1]] == False:
					MST.append(min_edge)
		else:
			min_edge = priqueue.pop()
			#print(min_edge)
			if visited[min_edge[1]] == False:
				MST.append(min_edge)
	mst_sum = 0
	for node_node_weight in MST:
		mst_sum += node_node_weight[2]
	return mst_sum


	
