class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.node  = []
        self.graph = []
    
    def add_node(self,vlu):
        self.node.append(vlu)
    
    def add_edge(self, s, d, w):
        self.graph.append([s,d,w])
    
    def print_solution(self,disc):
        print("The distance from source to destination:")
        for key, value in disc.items():
            print("src:",key,"Value:",value)

    def bellmanFord(self,src):
        disc = {i:float("inf") for i in self.node}
        disc[src] = 0
        for _ in range(self.v-1):
            for s,d,w in self.graph:
                if disc[s] != float("inf") and disc[s]+w < disc[d]:
                    disc[d] = disc[s]+w
        
        for s,d,w, in self.graph:
            if disc[s] != float("inf") and disc[s]+w < disc[d]:
                print("Graph contain the negative cycle")
                return
        self.print_solution(disc)

g = Graph(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanFord("E")
