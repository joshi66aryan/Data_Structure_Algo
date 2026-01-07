#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# Disjoint Set in Python

class DisjointSet:
    def __init__(self, vertices):
        # A disjoint set data structure is a collection of sets that are non-overlapping.
        # This implementation represents each set as a tree.
        # It's useful for tasks like finding connected components in a graph.
        self.vertices = vertices
        self.parent = {}
        # The parent dictionary stores the parent of each vertex. Initially, each vertex
        # is its own parent, which means each vertex is in its own separate set.
        for v in vertices:
            self.parent[v] = v
        # The rank dictionary is used to keep track of the height of each tree.
        # This helps in optimizing the union operation to keep the trees as flat as possible.
        # Initially, all ranks are 0 because each set contains only one element.
        self.rank = dict.fromkeys(vertices, 0)
    
    def find(self, item):
        # The find operation returns the representative (root) of the set containing the given item.
        # This representative is the item whose parent is itself.
        # The path compression optimization, which is not implemented here,
        # would flatten the tree by making all nodes on the path point directly to the root.
        if self.parent[item] == item:
            return item
        else:
            # Recursively find the root of the parent.
            return self.find(self.parent[item])
    
    def union(self, x, y):
        # The union operation merges the two sets containing items x and y.
        # The goal is to connect the root of one tree to the root of the other.
        xroot = self.find(x)
        yroot = self.find(y)
        # Check if the items are already in the same set. If they are, no action is needed.
        if xroot != yroot:
            # This part of the union operation is called "union by rank".
            # It's an optimization that ensures the tree with a smaller rank is
            # attached as a child to the tree with a larger rank.
            # This helps to keep the overall tree height small, which improves
            # the efficiency of future find operations.
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            elif self.rank[xroot] > self.rank[yroot]:
                self.parent[yroot] = xroot
            else:
                # If the ranks are equal, we can attach either root to the other.
                # We'll attach yroot to xroot and then increment the rank of the new root, xroot.
                # This is because the height of the new tree will be one more than the previous height.
                self.parent[yroot] = xroot
                self.rank[xroot] += 1

# Example usage (uncomment the following lines to run)
# vertices = ["A", "B", "C", "D", "E"]
# ds = DisjointSet(vertices)
# print("Initial state:", ds.parent)
# ds.union("A", "B")
# print("After union A, B:", ds.parent)
# ds.union("A", "C")
# print("After union A, C:", ds.parent)
# print("Finding root of A:", ds.find("A"))
# print("Finding root of B:", ds.find("B"))
# print("Finding root of C:", ds.find("C"))