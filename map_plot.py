#map_plot.py
#Aadil Islam
#March 7, 2018

from cs1lib import *
from load_graph import *
from vertex import *
from bfs import *

# load map and dictionary
img = load_image("data/dartmouth_map.png")
vertex_dict = load_graph("data/dartmouth_graph.txt")

# global variables
mouse_x = 0
mouse_y = 0
start = None
goal = None
reset_start = False
movement = False

# job is to reset the start vertex to the user's desire
def press(mx, my):

    global mouse_x, mouse_y, reset_start
    reset_start = True
    mouse_x = mx
    mouse_y = my

# main role is to determine what vertex the user wants as the goal
def move(mx, my):

    global mouse_x, mouse_y, movement
    movement = True
    mouse_x = mx
    mouse_y = my

def graphics():

    global reset_start, start, goal

    # draw the map itself
    clear()
    draw_image(img, 0, 0)

    # only reset the starting vertex if mouse is pressed
    if reset_start:

        # check if any vertex is close to the mouse
        for vertex in vertex_dict:
            if vertex_dict[vertex].is_close(mouse_x, mouse_y):
                start = vertex

            # make sure this if statement does not run again next loop
            reset_start = False

    # determine what vertex user is pointing to if the mouse has moved
    if movement:
        for vertex in vertex_dict:
             if vertex_dict[vertex].is_close(mouse_x, mouse_y):
                 goal = vertex

    # draw edges between each vertex and each of its adjacent vertices
    for vertex in vertex_dict:
        for adj in vertex_dict[vertex].adj_verts:
            vertex_dict[vertex].draw_edge(vertex_dict[adj], 0, 0, 1)

    # as a default, all vertices should be blue
    for vertex in vertex_dict:
            vertex_dict[vertex].draw_vertex(0, 0, 1)

    # can only run BFS if we have a starting point
    if not start == None:

        (connect_the_dots, dist) = breadth_first_search(vertex_dict, start, goal)

        # path includes endpoints
        connect_the_dots.insert(0, start)
        connect_the_dots.append(goal)

        # since connect_the_dots is in order of path, each red edge is between consecutive entries in list
        for i in range(len(connect_the_dots)-1):
            vertex_dict[connect_the_dots[i]].draw_edge(vertex_dict[connect_the_dots[i+1]], 1, 0, 0)

        # each vertex should in path should be red
        for i in range(len(connect_the_dots)):
            vertex_dict[connect_the_dots[i]].draw_vertex(1, 0, 0)

start_graphics(graphics, 2400, width = 1012, height = 811, mouse_move = move, mouse_press = press)