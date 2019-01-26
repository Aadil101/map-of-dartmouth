#load_graph.py
#Aadil Islam
#March 3, 2018

from vertex import *

# take each line from file individually
def parse_line(line):

    # divide up line into sections determined by semicolon
    # save each section into variables/lists
    section_split = line.split(";")
    vertex_name = section_split[0].strip()
    adjacent_vertices = section_split[1].strip().split(",")
    coordinates = section_split[2].strip().split(",")

    # strip spaces
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    # strip spaces
    coords = []
    for a in coordinates:
        if a:
            coords.append(a.strip())

    # return information for the vertex described in this line
    return vertex_name, adjacent, coords[0], coords[1]

def load_graph(filename):

    # create dictionary
    vertex_dict = {}

    # load text file to be read
    file = open(filename, "r")

    # take text file line by line
    for l in file:

        # check if line is even valid
        if len(l.split(";")) == 3:

            # obtain information for new vertex using parse_line
            vertex_name, adjacent_vertices, x, y = parse_line(l)

        # add vertex to dictionary
        vertex_dict[vertex_name] = Vertex(vertex_name, int(x), int(y), adjacent_vertices)

    file.close()

    return vertex_dict
