from QueueLinkedList import QueueUsingLL as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNodeBST(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNodeBST(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNodeBST(rootNode.rightChild, nodeValue)
    return f"The {nodeValue} is inserted successfully."

def preOrderTraversal(rootNode):
    if not rootNode:
        return "The binary tree is empty."
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return "The binary tree is empty."
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def inOrderTraversal(rootNode):
    if not rootNode:
        return "The binary tree is empty."
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    preOrderTraversal(rootNode.rightChild)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return "The binary tree is empty."
    else:
        customQueue = queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if not rootNode:
        return "The binary search tree is empty."
    else:
        if nodeValue == rootNode.data:
            return "The data is found at root node."
        elif nodeValue <= rootNode.data:
            if nodeValue == rootNode.leftChild:
                return "The data found at left child."
            else:
                searchNode(rootNode.leftChild, nodeValue)
        else:
            if nodeValue ==  rootNode.rightChild:
                return "The value is found at the right child."
            else:
                searchNode(rootNode.rightChild, nodeValue)

def minValue(rootNode):
    curr = rootNode
    while (curr.leftChild is not None):
        curr = curr.leftChild
    return curr

def deleteNode(rootNode, dNode):
    if rootNode is None:
        return rootNode
    if dNode < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, dNode)
    elif dNode > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, dNode)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode
        

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The binary search tree is deleted."



newBST = BSTNode(None)
insertNodeBST(newBST, 70)
insertNodeBST(newBST,50)
insertNodeBST(newBST,90)
insertNodeBST(newBST, 30)
insertNodeBST(newBST,60)
insertNodeBST(newBST,80)
insertNodeBST(newBST,100)
insertNodeBST(newBST,20)
insertNodeBST(newBST,40)
levelOrderTraversal(newBST)
print("<------------------>")
inOrderTraversal(newBST)
print("<----------------->")
postOrderTraversal(newBST)
print(deleteNode(newBST,80))
