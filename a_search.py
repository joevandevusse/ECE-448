from makemaze import makeMaze 
from makemaze import meet_neighbors
from priorityqueue import PriorityQueue
def heuristic(a,b):
	x1 = a.x
	y1 = a.y

	x2 = b.x
	y2 = b.y
	return abs(x1 - x2) + abs(y1 - y2)


def a_search(graph, start, goal):
	my_heap = PriorityQueue()  #not really a heap just easier to call it that than queue
	my_heap.push(start, 0)
	pathway = []
	
	
	while not my_heap.empty():
		current = my_heap.pop()
		if current == goal:
				break
		for i in current.edges:
			new_score = current.gscore + 1 #increment g(n)
			if i.gscore == 0 or new_score < i.gscore:
				i.gscore = new_score
				i.hscore = heuristic(i,goal)
				i.fscore = i.gscore + i.hscore
				my_heap.push(i, i.fscore)
				i.parent = current
				pathway.append(i.parent)
	return pathway



graph, start, goal = makeMaze('mediumMaze.txt')
meet_neighbors(graph)
solution = a_search(graph, start, goal)
print(solution)



