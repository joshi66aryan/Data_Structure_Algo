# In Python, the heapq module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. It uses a binary heap under the hood and maintains the smallest element at index 0 (a min-heap).
# Key Points about heapq:

    # It only supports min-heaps (smallest element at the root).
    # A heap is just a list, but structured to satisfy the heap property.
    # The time complexity for heappush and heappop is O(log n).
    # The time complexity for accessing the smallest element is O(1).

import heapq
class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")
    
    # we neee this to compare the minimum distance of the node
    # In Python, __lt__ is a "magic method" or "dunder method" 
    # that allows you to define the behavior of the less-than 
    # operator (<) for objects of a custom class. 
    # Purpose:
        # When you compare two objects of a class using the < 
        # operator (e.g., object_a < object_b), Python internally 
        # calls the __lt__ method of the first object (object_a.__lt__(object_b)).
        # This method should return True if the first object is considered "less than" 
        # the second object, and False otherwise.
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self,weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)
    
## Dijkstra Algorithm
class dijkstra:
    def __init__(self):
        self.heap = []
    
    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap,start_vertex)
        while self.heap:
            # pop element with the lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider the neighbors
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex 
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start

                    # update the heap
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True
        
    def get_shortest_path(self, vertex):
        print(f"The shortest path to the vertex is: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor
        print()
            
# step 1 - create node

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# step 2 - create edge
nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)

nodeC.add_edge(6, nodeF)
nodeC.add_edge(5, nodeF)
nodeC.add_edge(21, nodeF)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeF)




    



