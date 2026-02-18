class Graph:
    def __init__(self):
        self.adjList = {}
    
    def add_vertex(self, vertex):
        if(vertex not in self.adjList):
            self.adjList[vertex] = []

    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        self.adjList[src].append(dest)
        self.adjList[dest].append(src)


    def printGraph(self):
        for vertex in self.adjList:
            print(vertex, " -> ", self.adjList[vertex])

g = Graph()
g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.printGraph()


class Graph:
    def __init__(self):
        self.adjList = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
    
    def add_Edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        self.adjList[src].append(dest)
        self.adjList[dest].append(src)

    def printGraph(self):
        for vertex in self.adjList:
            print(vertex, " -> ", self.adjList[vertex])


G = Graph()
G.add_Edge(1,2)
G.add_Edge(1,4)
G.add_Edge(2,3)
G.add_Edge(2,4)
G.add_Edge(3,4)
G.add_Edge(3,5)
G.add_Edge(4,5)
G.printGraph()
