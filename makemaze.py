

from my_graph import my_node

import pprint

pp = pprint.PrettyPrinter(indent=2)


pp = pprint.PrettyPrinter(indent=2)
nodes = []
def makeMaze(filename):
    #with open('file.txt') as file:
        #contents = file.read()
    maze_file = open(filename)
    lines = maze_file.readlines()
    lista = [] 
    for i, line in enumerate(lines):
        row = []
        for j, char in enumerate(line):
            if char != '%' and char != '\n':
                node = my_node()
                node.x = i
                node.y = j
                if char == 'P':
                    row.append('start')
                    node.start = True
                    start = node
                if char == '.':
                    row.append('goal')
                    node.goal = True
                    end = node 
                nodes.append(node)
    all_line = ""
    for line in lines:
        all_line += line
    print(all_line)
    maze_file.close()  #this is cool
    return nodes, start, end

def meet_neighbors(nodes):
    for i in nodes:
        for j in nodes:
            if (i.x)+1 == j.x and i.y == j.y:
                (i.edges).append(j)
            if (i.x)-1 == j.x and i.y == j.y:
                (i.edges).append(j)
            if i.x == j.x and (i.y)+1 == j.y:
                (i.edges).append(j)
            if i.x == j.x and (i.y)-1 == j.y:
                (i.edges).append(j)



  