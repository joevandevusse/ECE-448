
# Our heuristic, to help you out, was to make a minimal spanning tree from the current node to all other unvisited nodes
# Which basically meant adding up the number of edges in a Breadth First Search that hit every other unseen place we needed to go

import pprint

pp = pprint.PrettyPrinter(indent=2)

def makeMaze(filename):
    #with open('file.txt') as file:
        #contents = file.read()
    maze_file = open(filename)
    lines = maze_file.readlines()
    graph = []
    start = []
    for i, line in enumerate(lines):
    #for i in range(len(lines)):
        row = []
        for j, char in enumerate(line):
        #for j in range(len(line)):
            if char == ' ':
                row.append('path')
                #row.append(' ')
            elif char == '%':
                row.append('wall')
                #row.append('%')
            elif char == 'P':
                row.append('start')
                set.update(i, j)
                #row.append('P')
            elif char == '.':
                row.append('goal')
                #row.append('.')
        graph.append(row)

    print(lines)
    #pp.pprint(graph)
    maze_file.close()  #this is cool
    return graph, start



def DFS(graph, start):
    stack = []
    visited = []
    start_x = start[0]
    start_y = start[1]
    stack.append(start)
    #for i in range(graph):
        #for j in range(graph[i]):
    while stack is not None:
        node = stack.pop[0]
        if node not in visited:
            visited.append(node)
            # Check if any neighbors are goal states
            # Right
            if node[0] < len(graph)-1 and graph[node[0]+1][node[1]] == 'goal':
                return graph[node[0]+1][node[1]]
            # Up
            if node[1] < len(graph)-1 and graph[node[0]][node[1]+1] == 'goal':
                return graph[node[0]][node[1]+1]
            # Left
            if node[1] and graph[node[0]-1][node[1]] == 'goal':
                return graph[node[0]-1][node[1]]
            # Down
            if node[1] > 0 and graph[node[0]][node[1]-1] == 'goal':
                return graph[node[0]][node[1]-1]
            # Check if neighbors haven't been visited
            # Right
            if node[0] < len(graph)-1 and graph[node[0]+1][node[1]] == 'path':
                stack.append(graph[node[0]+1][node[1]])
            # Up
            if node[1] < len(graph)-1 and graph[node[0]][node[1]+1] == 'path':
                stack.append(graph[node[0]][node[1]+1])
            # Left
            if node[1] and graph[node[0]-1][node[1]] == 'path':
                stack.appen(graph[node[0]-1][node[1]])
            # Down
            if node[1] > 0 and graph[node[0]][node[1]-1] == 'path':
                stack.append(graph[node[0]][node[1]-1])

#makeMaze('mediumMaze.txt')
graph, start = makeMaze('openMaze.txt')
