#bfs.py
#Aadil Islam
#March 7, 2018

from collections import *

# return list of vertices that connect start and goal together, as well as distance (why not?)
def breadth_first_search(dict, start, goal):

    # BFS does not need to do hard work if start and end goal are same!
    if start == goal:
        return [start], 0

    # start two-sided queue, begin it with start, start is visited
    frontier = deque()
    frontier.append(start)
    dict[start].visited = True
    dict[start].distance = 0

    # frontier being empty indicates all nodes have been visited
    while len(frontier) > 0:

        # remove vertex that we are analyzing neighbors for
        current_vertex = frontier.popleft()

        # check neighbors for vertex
        for neighbor in dict[current_vertex].adj_verts:

            # found unexplored vertex?
            if not dict[neighbor].visited:

                # it has been visited, and its back-pointer was the parent (current) vertex
                frontier.append(neighbor)
                dict[neighbor].visited = True
                dict[neighbor].back_pointer = current_vertex
                dict[neighbor].distance = dict[current_vertex].distance + 1

            # what if neighbor is the end goal?
            if neighbor == goal:

                # time to identify all the vertices in between start and goal, not that we have backpointers to use
                save = []

                # trace back until start
                while not current_vertex == start:
                    save.insert(0, current_vertex)
                    current_vertex = dict[current_vertex].back_pointer

                # done! turn every vertex back to unvisited for reuse
                for vertex in dict:
                    dict[vertex].visited = False

                return (save, dict[neighbor].distance)