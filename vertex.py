#vertex.py
#Aadil Islam
#March 7, 2018

from cs1lib import *

# constants
RADIUS_OF_VERTEX = 8
WIDTH_OF_EDGE = 3

class Vertex:

    # contructor for vertex object, with instance variables for BFS
    def __init__(self, name, x, y, adj_verts, back_pointer = None, distance = 0, visited = False):
        self.name = name
        self.x = x
        self.y = y
        self.adj_verts = adj_verts
        self.back_pointer = back_pointer
        self.distance = distance
        self.visited = visited

    def __str__(self):

        # adjacent vertices portion of the string is a little complicated with the commas...
        save = ""

        # turn elements in adjacent vertices into one whole string with commas appropriately placed
        for i in range(len(self.adj_verts)):
            save += self.adj_verts[i]
            if i != len(self.adj_verts)-1:
                save += ", "

        return(self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + save)

    # draw circle with custom color at appropriate location
    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        disable_stroke()
        draw_circle(self.x, self.y, RADIUS_OF_VERTEX)
        enable_stroke()

    # draw line between location of object and location of another object
    def draw_edge(self, new_vert, r, g, b):
        set_stroke_color(r, g, b)
        set_stroke_width(WIDTH_OF_EDGE)
        draw_line(self.x, self.y, new_vert.x, new_vert.y)

    # return true if inputted coordinates are within square of location of object (square has sides of 2 * RADIUS_OF_VERTEX)
    def is_close(self, mx, my):
        if mx < (self.x + RADIUS_OF_VERTEX) and mx > (self.x - RADIUS_OF_VERTEX) and  my < (self.y + RADIUS_OF_VERTEX) and my > (self.y - RADIUS_OF_VERTEX):
            return True
        else:
            return False
