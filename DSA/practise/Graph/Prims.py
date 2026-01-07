import sys
class Graph:
    def __init__(self, vertex_num, nodes, edge):
        self.vertex_num = vertex_num
        self.nodes = nodes
        self.edge = edge
        self.MST = []
    
    def print_solution(self):
        for s,d,w in self.MST:
            print("%s-%s:%s" % (s,d,w))
        
    def primsAlgo(self):
        visited =[0] * self.vertex_num
        visited[0] = True
        edgeNum = 0
        while edgeNum < self.vertex_num-1:
            min = sys.maxsize
            for i in range(self.vertex_num):
                if visited[i]:
                    for j in range(self.vertex_num):
                        if ((not visited[j])) and self.edge[i][j]:
                            if min > self.edge[i][j]:
                                min = self.edge[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edge[s][d]])
            edgeNum += 1
            visited[d] = True
        self.print_solution()

edges = [[0, 10, 20, 0, 0],
		[10, 0, 30, 5, 0],
		[20, 30, 0, 15, 6],
		[0, 5, 15, 0, 8],
		[0, 0, 6, 8, 0]]
nodes = ["A","B","C","D","E"]
g = Graph(5, nodes, edges)
g.primsAlgo()