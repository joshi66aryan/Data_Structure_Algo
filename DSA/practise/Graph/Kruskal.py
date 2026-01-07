import Disjointset as dst
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
        self.node = []
        self.MST = []
    
    def addNode(self,node):
        self.node.append(node)
    
    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])

    def print_solution(self,s,w,d):
        for s,d,w in self.MST:
            print("%s-%s:%s" % (s,d,w))
    
    def KruskalAlgo(self):
        i,e = 0,0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        ds = dst.DisjointSet(self.node)

        while e < self.V-1:
            s,d,w = self.graph[i]

            i+=1

            x = ds.find(s)
            y = ds.find(d)

            if x!=y:
                e+=1
                self.MST.append([s,d,w])
                ds.union(x,y)

        self.print_solution(s,d,w)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")

# Add edges (undirected graph → both directions are added)
g.addEdge("A", "B", 5)   # Edge A-B with weight 5
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)