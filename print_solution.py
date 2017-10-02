goal_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
			 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def printSolution(expanded_nodes, bare_maze, goal_order=None):
	#print(expanded_nodes)
	#return
	#unique_nodes = set(expanded_nodes)
	solution_maze = []
	line_len = 0
	flag = 0
	goal_count = 0
	for i, char in enumerate(bare_maze):
		if char == '\n' and flag == 0:
			flag += 1
			line_len = i + 1
		solution_maze.append(char)
	for node in expanded_nodes:
		#print('1-D maze length', len(bare_maze))
		#print(node.x, node.y)
		#print('line_len:', line_len)
		#print('str index', (line_len*node.y) + node.x)
		if bare_maze[(line_len*node.y) + node.x] == 'P':
			continue
		elif bare_maze[(line_len*node.y) + node.x] == '.':
			if goal_order is not None:
				solution_maze[(line_len*node.y) + node.x] = goal_list[goal_count]
				goal_count += 1
			else:
				solution_maze[(line_len*node.y) + node.x] = '@'
		else:
			solution_maze[(line_len*node.y) + node.x] = '*'
	solution_maze = "".join(solution_maze)
	return solution_maze
