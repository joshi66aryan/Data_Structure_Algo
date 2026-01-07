from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
        
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
        
    
    # remove edge
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    #remove vertex
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for otherVertex in self.adjacency_list[vertex]:
                self.adjacency_list[otherVertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    
    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    visited.add(adjacency_vertex)
                    queue.append(adjacency_vertex)




    def dfs(self, vertex):
        visited = set()
        stack = [vertex]

        while stack:
#            print("stack -->",stack)
            current_vertex = stack.pop()
            if current_vertex not in visited: 
                print("Current Vertex --> ", current_vertex)
                visited.add(current_vertex)

            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    stack.append(adjacency_vertex)


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "E")
graph.add_edge("C", "D")
graph.add_edge("D", "E")

graph.print_graph()
graph.dfs("A")

##### <---------------------------------Another Way to do same thing -------------------------------->
# import json
# from collections import deque

# class Graph:
#     def __init__(self, adjacency_list=None):
#         self.adjacency_list = adjacency_list if adjacency_list else {}

#     def bfs(self, start_vertex):
#         if start_vertex not in self.adjacency_list:
#             print(f"Start vertex {start_vertex} not in graph.")
#             return

#         visited = set([start_vertex])
#         queue = deque([start_vertex])

#         print("BFS Traversal:", end=" ")
#         while queue:
#             current = queue.popleft()
#             print(current, end=" ")
#             for neighbor in self.adjacency_list[current]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append(neighbor)
#         print()

#     def dfs(self, start_vertex):
#         if start_vertex not in self.adjacency_list:
#             print(f"Start vertex {start_vertex} not in graph.")
#             return

#         visited = set()
#         stack = [start_vertex]

#         print("DFS Traversal:", end=" ")
#         while stack:
#             current = stack.pop()
#             if current not in visited:
#                 print(current, end=" ")
#                 visited.add(current)
#                 # push neighbors
#                 for neighbor in self.adjacency_list[current]:
#                     if neighbor not in visited:
#                         stack.append(neighbor)
#         print()


# # ----------- Utility functions -----------

# def matrix_to_adjlist(vertices, matrix):
#     """Convert adjacency matrix to adjacency list."""
#     adj_list = {v: [] for v in vertices}
#     n = len(vertices)
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] == 1:  # edge exists
#                 adj_list[vertices[i]].append(vertices[j])
#     return adj_list


# # ----------- Main Program -----------

# if __name__ == "__main__":
#     file_input = input("Load graph from file? (y/n): ").strip().lower()
    
#     if file_input == "y":
#         filename = input("Enter filename (e.g., graph.json): ").strip()
#         with open(filename, "r") as f:
#             data = json.load(f)
#     else:
#         print("Enter graph in JSON format (adjacency list or matrix):")
#         data = json.loads(input().strip())

#     # Detect input type
#     if "matrix" in data and "vertices" in data:  
#         # Adjacency matrix provided
#         adjacency_list = matrix_to_adjlist(data["vertices"], data["matrix"])
#     else:
#         # Assume adjacency list provided
#         adjacency_list = data

#     g = Graph(adjacency_list)

#     # Choose traversal method
#     start_vertex = input("Enter starting vertex: ").strip()
#     method = input("Enter traversal method (bfs/dfs): ").strip().lower()

#     if method == "bfs":
#         g.bfs(start_vertex)
#     elif method == "dfs":
#         g.dfs(start_vertex)
#     else:
#         print("Invalid method. Choose 'bfs' or 'dfs'.")
