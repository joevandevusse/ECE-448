
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
    for line in lines:
        row = []
        for char in line:
            if char == ' ':
                #row.append('path')
                row.append(' ')
            elif char == '%':
                #row.append('wall')
                row.append('%')
            elif char == 'P':
                #row.append('start')
                row.append('P')
            elif char == '.':
                #row.append('goal')
                row.append('.')
        graph.append(row)

    print(lines)
    #pp.pprint(graph)
    maze_file.close()

#makeMaze('mediumMaze.txt')
makeMaze('openMaze.txt')
