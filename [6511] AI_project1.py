#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/9 19:26 
# @Author : Patrick 
# @File : [6511] AI_project1.py 
# @Software: PyCharm

import time


# traverse whole list to get the current min cost node
# (actual a list contains node)
# visited_dic is like [{cost:[visited_list for start node]}]
# [{142:[0, 18, 67, 31, 16]},{413:[0,17,57,21,42,49,10]}]
def get_min_cost(visited_dic):
    # initial variables
    min_cost = float('INF')
    need_del = 0

    for idx, i in enumerate(visited_dic):
        # get current cost and visited_list from single one
        # [{cost:[visited_list for a single node]}]
        for present_cost, visited_queue in i.items():
            if present_cost < min_cost:
                # record queue
                next_visit = visited_queue

                # record cost
                min_cost = present_cost

                # record dequeue index
                need_del = idx
    # Dequeue the one with min cost
    visited_dic.remove(visited_dic[need_del])
    # return visited queue and current cost
    return next_visit, min_cost


# Due to A* need to consider the Heuristic
# need to input the end_node
def a_get_min_cost(visited_dic, end_node):
    # initial variables
    min_cost = float('INF')
    need_del = 0
    tmp_h = 0
    for idx, i in enumerate(visited_dic):
        for present_cost, visited_queue in i.items():

            # get the Heuristic
            h = heuristic(visited_queue[len(visited_queue) - 1], end_node)

            # add the Heuristic to the current cost
            hc = h + present_cost
            if hc < min_cost:
                next_visit = visited_queue
                min_cost = hc

                # record present h for later delete it from cost+Heuristic
                tmp_h = h

                need_del = idx
    visited_dic.remove(visited_dic[need_del])
    return next_visit, min_cost - tmp_h


# heuristic function
# The idea of heuristic function is to find the min distance of two node
# if the first node is (1,4) second one is (7,10)
# so there are 7-1-1 = 5 nodes between horizontally
# there are 10-4-1 = 5 nodes between vertically
# Then calculate the diagonal of the 5(*100 pixels)*5(*100 pixels) square
def heuristic(start, end):
    x1, y1 = vertices_list[start]
    x2, y2 = vertices_list[end]
    return (((abs(x1 - x2) - 1) * 100) ** 2 + ((abs(y1 - y2) - 1) * 100) ** 2) ** 0.5


def uniform_cost_search(start_node, end_node, edges):
    # initial the visited list with edges that include start_node
    # edges is like [start,end,cost]: [[0,1,3],[0,2,4],[0,5,1],[0,6,1]]
    # the visited list is like [{cost:[visited list]}]: [{142:[0, 18, 67, 31, 16]},{413:[0,17,57,21,42,49,10]}]
    visited = [{i[2]: [start_node, i[0] if i[0] != start_node else i[1]]} for i in edges if start_node in i[:2]]

    # initial node and next visited list
    next_visit_node = -1
    next_visit = [-1]

    # start loop
    while True:
        # if the visited list is empty
        # shows that there's no path from start to end
        if not visited:
            return 0, 0

        # get next_visit node which is at the end of next_visit list
        # and present cost from the dequeue function
        next_visit, cost = get_min_cost(visited)

        # next_visit_node is at the end of next_visit list
        next_visit_node = next_visit[len(next_visit) - 1]

        # if next_visit node is the end_node
        # that means the end_node is dequeue
        # return current cost and the path
        if next_visit_node == end_node:
            return cost, next_visit

        # loop for finding next_visit_node's children
        for edge in edges:

            # if next_visit_node is 7
            # edges could be [7,10,41] or [3,7,10]
            # so if next_visit_node == edge[0] child would be edge[1]
            # vice versa
            child_node = edge[0] if edge[0] != next_visit_node else edge[1]

            # To ensure the edge include the next_visit_node
            # To ensure the child node haven't been visited
            if next_visit_node in edge[:2] and child_node not in next_visit:
                # visited list insert child node with its cost + previous cost
                visited.append({edge[2] + cost: next_visit + [child_node]})


def A_star(start_node, end_node, edges):
    # initial the visited list with edges that include start_node
    # edges is like [start,end,cost]: [[0,1,3],[0,2,4],[0,5,1],[0,6,1]]
    # the visited list is like [{cost:[visited list]}]: [{142:[0, 18, 67, 31, 16]},{413:[0,17,57,21,42,49,10]}]
    visited = [{i[2]: [start_node, i[0] if i[0] != start_node else i[1]]} for i in edges if
               start_node in i[:2]]

    # initial node and next visited list
    next_visit_node = -1
    next_visit = [-1]

    # start loop
    while True:
        # if the visited list is empty
        # shows that there's no path from start to end
        if not visited:
            return 0, 0

        # get next_visit node which is at the end of next_visit list
        # and present cost from the dequeue function
        next_visit, cost = a_get_min_cost(visited, end_node)

        # next_visit_node is at the end of next_visit list
        next_visit_node = next_visit[len(next_visit) - 1]

        # if next_visit node is the end_node
        # that means the end_node is dequeue
        # return current cost and the path
        if next_visit_node == end_node:
            return cost, next_visit

        # loop for finding next_visit_node's children
        for edge in edges:

            # if next_visit_node is 7
            # edges could be [7,10,41] or [3,7,10]
            # so if next_visit_node == edge[0] child would be edge[1]
            # vice versa
            child_node = edge[0] if edge[0] != next_visit_node else edge[1]

            # To ensure the edge include the next_visit_node
            # To ensure the child node haven't been visited
            if next_visit_node in edge[:2] and child_node not in next_visit:
                # visited list insert child node with its cost + previous cost
                visited.append({edge[2] + cost: next_visit + [child_node]})


# input graph file name
graph_name = input(
    'Please input graph file name with absolute path \n'
    '(e.g. E:\\Python\\Courses\\ai-master\\data\\graphs\\graph2000\\graph2000_799892.txt)\n')
# File opening Exception
try:
    f = open(graph_name)
except:
    print('Error occur when opening graph file')
    exit(0)
# f = open(r'E:\Python\Courses\ai-master\data\graphs\graph1000\graph1000_100020.txt')

# read all data to list
lines = f.readlines()

# close file
f.close()

# get the line number of 'Vertices' and 'Edges' to locate range of vertices and range of edges
v_index, e_index = lines.index('Vertices\n'), lines.index('Edges\n')

# vertices list stores all vertices location in form of (x,y) in vertices_list
vertices_list = [tuple(map(int, line.strip('\n').split(',')))[1:] for line in lines[v_index + 1:e_index] if
                 '#' not in line]

# edges list stores all vertices pair and cost in form of [start, stop, cost] in edges_list
edges_list = [list(map(int, line.strip('\n').split(',')))[:] for line in lines[e_index + 1:]]

# Input start node and end node
start, end = tuple(
    list(map(int, input('Please input Start node and End node, separate with \',\' (e.g. 31,41)\n').split(','))))

# Exception for node not in vertices
if start < 0 or end > len(vertices_list):
    print('Start node or End node not in graph\'s vertices')
    exit(0)
elif start == end:
    print('Couldn\'t go back to start node')
    exit(0)

# recode timestamp
t1 = time.time()

# using UCS for finding path
u_cost, u_visited = uniform_cost_search(start, end, edges_list)

# recode timestamp
t2 = time.time()

# print Cost and whole Path
if u_cost != 0 and u_visited != 0:
    print('UCS Total Cost:' + str(u_cost) + '\nUCS Path for Start node to End node: ' + str(u_visited))
    print('Total time for UCS algorithm:' + str(t2 - t1))
else:
    print('There\'s no path from start node to end node')

# recode timestamp
t1 = time.time()

a_cost, a_visited = A_star(start, end, edges_list)

# recode timestamp
t2 = time.time()

# print Cost and whole Path
if u_cost != 0 and u_visited != 0:
    print('A* Total Cost:' + str(a_cost) + '\nA* Path for Start node to End node: ' + str(a_visited))
    print('Total time for A* algorithm:' + str(t2 - t1))
else:
    print('There\'s no path from start node to end node')
