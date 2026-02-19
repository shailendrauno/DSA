class Graph:
    def __init__(self, vertex):
        self.mat = [  [0]*vertex for i in range(vertex) ]
        self.size = vertex
    def add_edge(self, src, dest):
        if(0<= src < self.size and 0<= dest < self.size):
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("invalid input")

    def dfs(self, src):
        visited = [False]*self.size
        stack = [src]

        while(stack):
            v = stack.pop()

            if(visited[v] == False):
                print(v, end=" -> ")
                visited[v] = True
            
            for i in (self.size - 1):
                if self.mat[v][i] == 1 and visited[i] == False:
                    stack.append(i)



         
             