class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parents = {}

        for v in vertices:
            self.parents[v] = v
        
        self.rank = dict.fromkeys(vertices,0)

    def find(self, item):
        if self.parents[item] == item:
            return item
        else:
            return self.find(self.parents[item])
    
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot != yRoot:
            if self.rank[xRoot] < self.rank[yRoot]:
                self.parents[xRoot] = yRoot
            elif self.rank[xRoot] > self.rank[yRoot]:
                self.parents[yRoot] = xRoot
            else:
                self.parents[yRoot] = xRoot
                self.rank[xRoot] += 1
            
# Example usage (uncomment the following lines to run)
vertices = ["A", "B", "C", "D", "E"]
ds = DisjointSet(vertices)
print("Initial state:", ds.parents)
ds.union("A", "B")
print("After union A, B:", ds.parents)
ds.union("A", "C")
print("After union A, C:", ds.parents)
print("Finding root of A:", ds.find("A"))
print("Finding root of B:", ds.find("B"))
print("Finding root of C:", ds.find("C"))
