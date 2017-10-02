from my_graph import my_node
import pprint
pp = pprint.PrettyPrinter(indent=2)


def makeMaze(filename):
    nodes = []
    maze_file = open(filename)
    lines = maze_file.readlines()
    end = []
    for i, line in enumerate(lines):
        row = []
        for j, char in enumerate(line):
            if char != '%' and char != '\n':
                node = my_node()
                node.x = j
                node.y = i
                if char == 'P':
                    node.start = True
                    start = node
                if char == '.':
                    node.goal = True
                    end.append(node)
                nodes.append(node)
    all_line = ""
    for line in lines:
        all_line += line
    print(all_line)
    maze_file.close()  #this is cool
    return nodes, start, end, all_line

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
