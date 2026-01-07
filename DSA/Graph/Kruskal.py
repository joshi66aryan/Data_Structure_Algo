#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Kruskal Algorithm in Python
import DisjointSet as dst   # Import Disjoint Set (Union-Find) to detect cycles efficiently

class Graph:
    def __init__(self, vertices):
        self.V = vertices       # Number of vertices in the graph, here = 5
        self.graph = []         # List of all edges (u, v, weight)
        self.nodes = []         # List of nodes (A, B, C, D, E)
        self.MST = []           # To store result edges of the Minimum Spanning Tree (MST)

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])   # Add an edge (source, destination, weight)
        # Example: ("A", "B", 5)

    def addNode(self, value):
        self.nodes.append(value)       # Add a node into graph
        # Example: "A"

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:       # Print all edges selected in MST
            print("%s - %s: %s" % (s, d, w))
        # Example Output:
        # A - B: 5
        # C - D: 6
        # B - D: 8
        # A - E: 15

    def kruskalAlgo(self):
        i, e = 0, 0                    # i = index for sorted edges, e = count of edges in MST
        ds = dst.DisjointSet(self.nodes)  # Initialize disjoint set for cycle detection

        # Step 1: Sort edges by weight (ascending)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        # Example sorted edges:
        # ("A","B",5), ("D","C",6), ("B","D",8), ("B","C",10), ("A","C",13),
        # ("A","E",15), ("C","E",20), ...

        # Step 2: Pick edges one by one
        while e < self.V - 1:   # For MST we need (V-1) edges → here 4 edges
            s, d, w = self.graph[i]    # Pick the smallest edge not yet considered
            i += 1

            # Find parents (to check if adding this edge forms a cycle)
            x = ds.find(s)  # Find root parent of s
            y = ds.find(d)  # Find root parent of d

            if x != y:      # If they are in different sets → no cycle
                e += 1
                self.MST.append([s, d, w])  # Add edge to MST
                ds.union(x, y)              # Union their sets

        self.printSolution(s, d, w)   # Print the MST result


# ---------------- Example Usage ----------------
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

# Run Kruskal's Algorithm
g.kruskalAlgo()

# Process explained with example:
# Sorted edges = [("A","B",5), ("C","D",6), ("B","D",8), ("B","C",10), ("A","C",13), ("A","E",15), ("C","E",20)]
# Step 1: Pick A-B (5) → added
# Step 2: Pick C-D (6) → added
# Step 3: Pick B-D (8) → added
# Step 4: Pick B-C (10) → forms cycle → skip
# Step 5: Pick A-C (13) → forms cycle → skip
# Step 6: Pick A-E (15) → added
# ✅ MST complete with 4 edges
# Final MST: A-B(5), C-D(6), B-D(8), A-E(15)
