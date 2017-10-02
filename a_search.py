from makemaze import makeMaze
from makemaze import meet_neighbors
from print_solution import printSolution
from priorityqueue import PriorityQueue
from mst import findMST

def manhattan(a,b):
	x1 = a.x
	y1 = a.y

	x2 = b.x
	y2 = b.y
	return abs(x1 - x2) + abs(y1 - y2)


def a_search(graph, start, goal):
	my_heap = PriorityQueue()  #not really a heap just easier to call it that than queue
	my_heap.push(start, 0)
	pathway = []
	cost_so_far = {}
	came_from = {}
	cost_so_far[start] = 0
	came_from[start] = None
	sum = 0
	while not my_heap.empty():
		current = my_heap.pop()
		#print("here")
		if current in goal:
			goal.remove(current)
			for i in  graph:
				if i.parent:
					sum += 1
			while current.parent:
				pathway.append(current)
				x = current.parent
				current.parent = None
				current = x
		if len(goal) == 0:
			break
		for i in current.edges:
			new_score = current.gscore + 1 #increment g(n)
			if i not in cost_so_far or new_score < i.gscore:
				cost_so_far[i] = new_score
				i.gscore = new_score
				i.hscore = findMST(i,goal)
				#print(i.hscore, current)
				i.fscore = i.gscore + i.hscore
				my_heap.push(i, i.fscore)
				if not i.parent:
					i.parent = current

	print("Nodes Expanded:", sum)
	return pathway


graph, start, goal, print_out = makeMaze('mediumSearch.txt')
meet_neighbors(graph)
solution = a_search(graph, start, goal)
print("Actual Solution:", len(solution))
solution_maze = printSolution(solution, print_out)
print(solution_maze)
