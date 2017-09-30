#!/usr/bin/python3
# Our heuristic, to help you out, was to make a minimal spanning tree from the current node to all other unvisited nodes
# Which basically meant adding up the number of edges in a Breadth First Search that hit every other unseen place we needed to go

import pprint

pp = pprint.PrettyPrinter(indent=2)

# Build the maze
def makeMaze(filename):
    #with open('file.txt') as file:
        #contents = file.read()
    maze_file = open(filename)
    lines = maze_file.readlines()
    graph = []
    start = None
    end = None
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
                end = (i, j)
                #row.append('.')
        graph.append(row)
    #print(lines)
    #pp.pprint(graph)
    maze_file.close()  #this is cool
    return graph, start, end

# Breadth-First Search
def BFS(graph, start):
    queue = []
    visited = []
    queue.append(start)
    while queue is not None:
        print('Queue:', queue)
        node = queue[len(queue)-1]
        queue.pop()
        if node not in visited:
            visited.append(node)
            print('Visited:', visited)
            print('Total Nodes Visited:', len(visited))
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
                queue.append((node[0]+1, node[1]))
            # Up
            if int(node[0]) < len(graph)-1 and graph[node[0]][node[1]+1] == 'path':
                queue.append((node[0], node[1]+1))
            # Left
            if int(node[1]) > 0 and graph[node[0]-1][node[1]] == 'path':
                queue.append((node[0]-1, node[1]))
            # Down
            if int(node[1]) > 0 and graph[node[0]][node[1]-1] == 'path':
                queue.append((node[0], node[1]-1))

# Depth-First Search
def DFS(graph, start):
    stack = []
    visited = []
    stack.append(start)
    while stack is not None:
        print('Stack:', stack)
        node = stack[0]
        stack.pop(0)
        if node not in visited:
            visited.append(node)
            print('Visited:', visited)
            print('Total Nodes Visited:', len(visited))
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

# Manhattan distance heuristic for GBFS
def chooseManhattan(some_list, dest):
    best_dist = 1000000
    best_index = -1
    for i in range(len(some_list)):
        dist = (abs(dest[0]-some_list[i][0])**2 + abs(dest[1]-some_list[i][1]))**(1/2)
        if dist < best_dist:
            best_dist = dist
            best_index = i
    return best_index

# Greedy Best-First Search
def GBFS(graph, start, end):
    neighbors = []
    visited = []
    neighbors.append(start)
    while neighbors is not None:
        index = chooseManhattan(neighbors, end)
        print('Neighbors:', neighbors)
        node = neighbors[index]
        neighbors.pop(index)
        if node not in visited:
            visited.append(node)
            print('Visited:', visited)
            print('Total Nodes Visited:', len(visited))
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
                neighbors.append((node[0]+1, node[1]))
            # Up
            if int(node[0]) < len(graph)-1 and graph[node[0]][node[1]+1] == 'path':
                neighbors.append((node[0], node[1]+1))
            # Left
            if int(node[1]) > 0 and graph[node[0]-1][node[1]] == 'path':
                neighbors.append((node[0]-1, node[1]))
            # Down
            if int(node[1]) > 0 and graph[node[0]][node[1]-1] == 'path':
                neighbors.append((node[0], node[1]-1))

def chooseManhattanPlusCost(some_list, destination):
    best_f = 1000000
    best_index = -1
    for i in range(len(some_list)):
        dist = (abs(end[0]-some_list[i][0])**2 + abs(end[1]-some_list[i][1]))**(1/2)
        cost = some_list[i][2]
        f = dist + cost
        if f < best_f:
            best_f = f
            best_index = i
    return best_index

# A* Search
def AStar(graph, start, end):
    neighbors = []
    visited = []
    tuple_with_cost = (start[0], start[1], 0)
    neighbors.append(tuple_with_cost)
    while neighbors is not None:
        index = chooseManhattanPlusCost(neighbors, end)
        print('Neighbors:', neighbors)
        node = neighbors[index]
        neighbors.pop(index)
        if node not in visited:
            visited.append(node)
            print('Visited:', visited)
            print('Total Nodes Visited:', len(visited))
            # Check if any neighbors are goal states
            # Right
            if int(node[0]) < len(graph)-1 and graph[node[0]+1][node[1]] == 'goal':
                return (node[0]+1, node[1], node[2]+1)
            # Up
            elif int(node[1]) < len(graph[0])-1 and graph[node[0]][node[1]+1] == 'goal':
                return (node[0], node[1]+1, node[2]+1)
            # Left
            elif int(node[0]) > 0 and graph[node[0]-1][node[1]] == 'goal':
                return (node[0]-1, node[1], node[2]+1)
            # Down
            elif int(node[1]) > 0 and graph[node[0]][node[1]-1] == 'goal':
                return (node[0], node[1]-1, node[2]+1)
            # Check if neighbors haven't been visited
            # Right
            if int(node[0]) < len(graph)-1 and graph[node[0]+1][node[1]] == 'path':
                neighbors.append((node[0]+1, node[1], node[2]+1))
            # Up
            if int(node[0]) < len(graph)-1 and graph[node[0]][node[1]+1] == 'path':
                neighbors.append((node[0], node[1]+1, node[2]+1))
            # Left
            if int(node[1]) > 0 and graph[node[0]-1][node[1]] == 'path':
                neighbors.append((node[0]-1, node[1], node[2]+1))
            # Down
            if int(node[1]) > 0 and graph[node[0]][node[1]-1] == 'path':
                neighbors.append((node[0], node[1]-1, node[2]+1))

def MST(start, goals_list):
    best = ()
    best_weight = 100000
    for i in goals_list:
        dist = (abs(end[0]-goals_list[i][0])**2 + abs(end[1]-goals_list[i][1]))**(1/2)
        sub_list = goals_list - i
        mst_dists = []
        for j in sub_list:
            mst_dists.append((abs(end[0]-goals_list[i][0])**2 + abs(end[1]-goals_list[i][1]))**(1/2))
        #neighbor_avg = sum(mst_dists)/len(mst_dists)
        neighbor_avg = sum(mst_dists)
        # h(n) = f(n) + g(n)
        weight = dist+neighbor_avg)/2)
        if weight < best_weight:
            best = (i[0], i[1])
    return best

def pacman(graph, start, goals):
    curr_start = start
    for i in range(len(goals)):
        goal_to_pursue = MST(curr_start, goals)
        new_start = AStar(graph, curr_start, goal_to_pursue)
        curr_start = new_start
        if curr_start in goals:
            goals.remove(curr_start)

if __name__ == "main":
    #graph, start, end = makeMaze('mediumMaze.txt')
    graph, start, end = makeMaze('openMaze.txt')
    #graph, start, end = makeMaze('smallMaze.txt')
    #print(graph)
    #dest = BFS(graph, start)
    #dest = DFS(graph, start)
    dest = GBFS(graph, start, end)
    #dest = AStar(graph, start, end)
    print(dest)
