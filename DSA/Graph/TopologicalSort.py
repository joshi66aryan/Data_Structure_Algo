#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

from collections import defaultdict # defaultdict allows us to create a dictionary with default list values

class Graph:
    def __init__(self, numberofVertices):
        # Initialize the graph using a defaultdict with list as the default factory.
        # This creates an adjacency list representation where keys are vertices
        # and values are lists of their adjacent vertices (neighbors).
        self.graph = defaultdict(list)  
        # Stores the number of vertices, though it's not strictly used in this specific implementation.
        self.numberofVertices = numberofVertices  
    
    def addEdge(self, vertex, edge):
        # Adds a directed edge from 'vertex' to 'edge'.
        # This means 'edge' is a neighbor of 'vertex'.
        self.graph[vertex].append(edge)         
    
    def topogologicalSortUtil(self, v, visited, stack):
        # This is a recursive helper function for the topological sort.
        # It performs a DFS traversal.

        # Mark the current vertex 'v' as visited by adding it to the 'visited' list.
        visited.append(v)

        # Iterate through all neighbors 'i' of the current vertex 'v'.
        for i in self.graph[v]:
            # Recursively call the function for any unvisited neighbors.
            if i not in visited:
                self.topogologicalSortUtil(i, visited, stack)
        
        # After a vertex and all its descendants have been visited,
        # insert the current vertex 'v' at the beginning of the 'stack'.
        # This ensures that vertices with no outgoing edges (or whose subgraphs have been fully explored)
        # are placed first, following the topological order logic.
        stack.insert(0, v)
    
    def topologicalSort(self):
        # Main function to perform the topological sort.

        # 'visited' list to keep track of visited vertices during DFS.
        visited = [] 
        # 'stack' to store the final topological order.
        stack = []   

        # Iterate through all vertices present in the graph's adjacency list.
        # We convert keys to a list to avoid issues with modifying the dictionary during iteration.
            # 🔹 Why list(self.graph)?
            # In Python, looping directly over a dictionary:
            # for k in self.graph:
            # iterates over the keys ("A", "C", "E", ...).
            # But here, the author wrote:
            # for k in list(self.graph):
            # which creates a new list of the keys before looping.

        # Normally you could just do:
            #     for k in self.graph:
            #     and it would work fine.
            #     But here’s the catch:
            #     During recursion (topogologicalSortUtil) you access self.graph[v].
            #     If v has no outgoing edges, defaultdict(list) automatically creates an empty list for it.
            #     This means the dictionary self.graph can grow while you’re iterating.
        # If you were doing:
            #  for k in self.graph:
            # and new keys are added mid-loop, it could cause runtime errors like
            # RuntimeError: dictionary changed size during iteration.
            # 👉 By wrapping in list(self.graph), you create a snapshot copy of the keys at the start, so even if the dictionary grows, your loop is safe.
        
        for k in list(self.graph):
            # If a vertex has not been visited yet, start a new DFS traversal from it.
            if k not in visited:
                self.topogologicalSortUtil(k, visited, stack)
        
        # Print the final list which now contains the topological order.
        print(stack)
    
    

# Example usage:
# Create a Graph object with 8 vertices (the number is illustrative).
customGraph = Graph(8)
# Add directed edges to the graph.
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

# Perform the topological sort and print the result.
customGraph.topologicalSort()