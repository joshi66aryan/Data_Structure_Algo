import math
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def __str__(self):
        if self.lastUsedIndex == 0:
            return "<empty tree>"

        # Calculate tree height (levels)
        height = math.floor(math.log2(self.lastUsedIndex)) + 1
        
        # Width of printed output
        max_width = 2 ** height * 3  # 3 spaces per node approx
        
        result = ""
        index = 1
        
        for level in range(height):
            level_nodes_count = 2 ** level
            level_nodes = []
            
            for i in range(level_nodes_count):
                if index <= self.lastUsedIndex:
                    val = str(self.customList[index]) if self.customList[index] is not None else ""
                    index += 1
                else:
                    val = ""
                level_nodes.append(val.center(3))
            
            space_between = max_width // level_nodes_count
            line = (" " * (space_between // 2)).join(level_nodes)
            
            # Center the whole line
            result += line.center(max_width) + "\n"
        
        return result
    
    # insert Node
    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The binary tree is full."
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return f"{value} inserted at {self.lastUsedIndex}."
    
    # search node
    def searchNode(self, value):
        if self.lastUsedIndex == 0: 
            return "The binary tree is empty."
        for i in range(self.customList):
            if self.customList[i] == value:
                return f"{value} found at {i}"
        return "The item not found."

    # preOrderTraversal
    def preOrderTraversal(self, index):
        if self.lastUsedIndex == 0: 
            return "The binary tree is empty."
        if index > self.lastUsedIndex:
            return 
        print(self.customList[index])
        self.preOrderTraversal(2*index)
        self.preOrderTraversal(2*index+1)

    # inOrderTraversal
    def inOrderTraversal(self, index):
        if self.lastUsedIndex == 0: 
            return "The binary tree is empty."
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(2*index)
        print(self.customList[index])
        self.inOrderTraversal(2*index+1)

    # postOrderTraversal
    def postOrderTraversal(self, index):
        if self.lastUsedIndex == 0: 
            return "The binary tree is empty."
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(2*index)
        self.postOrderTraversal(2*index+1)
        print(self.customList[index])

    # levelOrderTraversal
    def levelOrderTraversal(self, index):
        if self.lastUsedIndex == 0: 
            return "The binary tree is empty."
        if index > self.lastUsedIndex:
            return
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
          
    # deleteNode
    def deleteNode(self, value):
        if self.lastUsedIndex == 0: 
            return "The binary tree is empty."
        for i in range(1, self.lastUsedIndex):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex += 1
                return f"{value} is deleted from the binary tree."
        self.lastUsedIndex -= 1 

    # deleteBt
    def deleteBt(self):
        self.customList = []
        return "The binary tree is emptied."

# Here's the summary:

# * Your array-based binary tree needs an array size based on the maximum number of nodes it will hold.
# * A complete binary tree of height $h$ has $2^h - 1$ nodes.
# * So, choose the size as $2^h$ (array index 0 unused) where $h$ is the minimum height to fit all nodes.
# * For example, to hold 9 nodes, pick size 16 ($2^4$) because height 4 tree can hold up to 15 nodes.
# * This prevents index errors during insertions and traversals.
# * Alternatively, you can add dynamic resizing to grow the array as needed.



bt = BinaryTree(16)
bt.insertNode("Drinks")
bt.insertNode("Hot")
bt.insertNode("Cold")
bt.insertNode("Tea")
bt.insertNode("offee")
bt.insertNode("Coe")
bt.insertNode("chaiffee")
bt.insertNode("teaffee")
bt.insertNode("tooffee")

# print(bt)
# print("<----------preorder------------->")
# bt.preOrderTraversal(1)
# print("<----------inorder------------->")
# bt.inOrderTraversal(1)
# print("<----------postorder------------->")
# bt.postOrderTraversal(1)
# print("<----------levelorder------------->")
# bt.levelOrderTraversal(1)
print(bt.deleteNode("Coe"))
print(bt)
