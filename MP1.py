
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
    start = None
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
                start = (i, j)
                #row.append('P')
            elif char == '.':
                row.append('goal')
                #row.append('.')
        graph.append(row)

    #print(lines)
    #pp.pprint(graph)
    maze_file.close()  #this is cool
    return graph, start



def DFS(graph, start):
    stack = []
    visited = []
    #start_x = start[0]
    #start_y = start[1]
    stack.append(start)
    #for i in range(graph):
        #for j in range(graph[i]):
    while stack is not None:
        print('Stack:', stack)
        node = stack[0]
        stack.pop(0)
        if node not in visited:
            visited.append(node)
            print('Visited:', visited)
            # Check if any neighbors are goal states
            # Right
            if int(node[0]) < len(graph)-1 and graph[node[0]+1][node[1]] == 'goal':
                return (node[0]+1, node[1])
            # Up
            elif int(node[1]) < len(graph[0])-1 and graph[node[0]][node[1]+1] == 'goal':
                return (node[0], node[1]+1)
            # Left
            elif int(node[0]) > 0 and graph[node[0]-1][node[1]] == 'goal':
                return (node[0]-1, node[1])
            # Down
            elif int(node[1]) > 0 and graph[node[0]][node[1]-1] == 'goal':
                return (node[0], node[1]-1)
            # Check if neighbors haven't been visited
            # Right
            if int(node[0]) < len(graph)-1 and graph[node[0]+1][node[1]] == 'path':
                stack.append((node[0]+1, node[1]))
            # Up
            if int(node[0]) < len(graph)-1 and graph[node[0]][node[1]+1] == 'path':
                stack.append((node[0], node[1]+1))
            # Left
            if int(node[1]) > 0 and graph[node[0]-1][node[1]] == 'path':
                stack.append((node[0]-1, node[1]))
            # Down
            if int(node[1]) > 0 and graph[node[0]][node[1]-1] == 'path':
                stack.append((node[0], node[1]-1))

#makeMaze('mediumMaze.txt')
#graph, start = makeMaze('openMaze.txt')
graph, start = makeMaze('smallMaze.txt')
#print(graph)
dest = DFS(graph, start)
print(dest)
