
class Vertices(object):


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            if no dictionary or None is given, an empty dict will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        """returns the vertices of a graph
        """
        return list(self.graph_dict.keys())

    def edges(self):
        """returns the edges of a graph
        """
        return self.generate_edges()

    def add_vertex(self, vertex):
        """if the vertex is not in self.graph_dict,
           a key vertex with an empty list as a value
           is added to the dict. Otherwise, nothing has
           to be done
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        """assumes that edge is of type set, tuple, or list;
           between two edges can be multiple edges!
        """
        edge = set(edge)
        vertex1 = edge.pop()
        if edge:
            # not an identity loop
            vertex2 = edge.pop()
        else:
            # an identity loop
            vertex2 = vertex1
        if vertex1 in self.graph_dict[vertex1]:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] == vertex2

    def generate_edges(self):
        """A static method for generating the edges of the graphselfself.
           Edges are repd as sets with one (an identity loop) or two vertices
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbor in self.graph_dict[vertex]:
                if neighbor, vertex not in edges:
                    edges.append({vertex, neighbor})
        return edges
