from QueueLinkedList import QueueUsingLL as queue

class TreeNode:
    def __init__(self, data, ):
        self.data = data
        self.leftChild = None 
        self.rightChild = None 

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
leftChild.leftChild = TreeNode("Tea")
leftChild.rightChild  = TreeNode("Coffee")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightNode)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue() #.QueueUsingLL()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode, value):
    if not rootNode:
        return "The binary tree doesn't exists." 
    else:
        customQueue = queue() #.QueueUsingLL()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root  = customQueue.dequeue()
            if root.value.data == value:
                return f"The value {value} is found."
            if rootNode.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if rootNode.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not Found"

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue()#.QueueUsingLL()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted as left child."
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted as right child."
            
def getDeepestNode(rootNode):
    if not rootNode:
        return "The binary tree is empty."
    else:
        customQueue = queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepest_vlu = root.value
        return deepest_vlu
    
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return "The binary tree is empty."
    else:
        customQueue = queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value == dNode: 
                root.value = None
                return
            if root.value.leftChild:
                if root.value.leftChild == dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                if root.value.rightChild == dNode:
                    root.value.rightChild == None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)



def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The binary tree is empty."
    else:
        customQueue = queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode,dNode )
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild  = None
    return "The binary tree is emptied."
    


def displayTree(node, level=0, label="Root"):
    """Display the binary tree in a tree-like diagram with slashes"""
    indent = " " * (level * 6)  # adjust space per level
    print(f"{indent}{label}: {node.data}")
    
    if node.leftChild or node.rightChild:
        # Print left and right children
        if node.leftChild:
            displayTree(node.leftChild, level + 1, "L")
        else:
            print(" " * ((level + 1) * 6) + "L: None")
        
        if node.rightChild:
            displayTree(node.rightChild, level + 1, "R")
        else:
            print(" " * ((level + 1) * 6) + "R: None")


            
newNode = TreeNode("Cola")
newNode1 = TreeNode("Chai")
newNode2 = TreeNode("BlackChai")
insertNodeBT(newBT, newNode)
insertNodeBT(newBT, newNode1)
insertNodeBT(newBT, newNode2)
displayTree(newBT)
deleteNodeBT(newBT,"BlackChai")
displayTree(newBT)