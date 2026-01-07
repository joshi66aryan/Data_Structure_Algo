from QueueLinkedList import QueueUsingLL as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.leftChild = None
        self.rightChild = None

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
    inOrderTraversal(rootNode.rightChild)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    customQueue = queue()
    customQueue.enqueue(rootNode)
    while not (customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, srcValue):
    if rootNode is None:
        print("Not Found")
        return
    if srcValue == rootNode.data:
        print("The value is found at root node.")
    elif srcValue < rootNode.data:
        if rootNode.leftChild == srcValue:
            print("The value found at left subtree.")
        else:
            searchNode(rootNode.leftChild, srcValue)
    else:
        if rootNode.rightChild == srcValue:
            print("The value found at right subtree.")
        else:
            searchNode(rootNode.rightChild, srcValue)

def getHeight(rootNode):
    if not rootNode:
        return 0 
    return rootNode.height

## left-left heavy --> rotate right
def rotateRight(disBalancedNode):
    newRoot = disBalancedNode.leftChild
    disBalancedNode.leftChild = disBalancedNode.leftChild.rightChild
    newRoot.rightChild = disBalancedNode
    disBalancedNode.height = 1+ max(getHeight(disBalancedNode.leftChild), getHeight(disBalancedNode.rightChild))
    newRoot.height = 1+ max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

## right-right heavy --> rotate left
def rotateLeft(disBalancedNode):
    newRoot = disBalancedNode.rightChild
    disBalancedNode.rightChild = disBalancedNode.rightChild.leftChild
    newRoot.leftChild = disBalancedNode
    disBalancedNode.height = 1 + max(getHeight(disBalancedNode.leftChild), getHeight(disBalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalanceFactor(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)
    
def insertNode(rootNode, newNode):
    if not rootNode:
        return AVLNode(newNode)
    elif newNode < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, newNode)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, newNode)
    
    balanceFactor = getBalanceFactor(rootNode)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))

    if balanceFactor > 1 and newNode < rootNode.leftChild.data:
        return rotateRight(rootNode)
    if balanceFactor < -1 and newNode > rootNode.rightChild.data:
        return rotateLeft(rootNode)
    if balanceFactor > 1 and newNode  > rootNode.leftChild.data:
        rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode)
    if balanceFactor < -1 and newNode < rootNode.rightChild.data:
        rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)
    return rootNode

def getMinValue(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValue(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        elif rootNode.leftChild is None:
            temp = rootNode.rightChild is None
            rootNode = None
            return temp
        
        minValue = getMinValue(rootNode.rightChild)
        rootNode.data = minValue.data
        rootNode.rightChild =  deleteNode(rootNode.rightChild, minValue.data)

    balanceFactor = getBalanceFactor(rootNode)
    if balanceFactor > 1 and getBalanceFactor(rootNode.leftChild) >= 0:
        return rotateRight(rootNode)
    if balanceFactor < -1 and getBalanceFactor(rootNode.rightChild) <= 0:
        return rotateLeft(rootNode)
    if balanceFactor > 1 and getBalanceFactor(rootNode.leftChild) < 0:
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode)
    if balanceFactor < -1 and getBalanceFactor(rootNode.rightChild) > 0:
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)
    return rootNode

def deleteAVLTree(rootNode):
    rootNode.height = 0
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL Tree is deleted."



newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
#deleteAVL(newAVL)
print("<------------------------>")
levelOrderTraversal(newAVL)
print("<------------------------>")
preOrderTraversal(newAVL)
print("<------------------------>")
searchNode(newAVL, 15)
print("<------------------------>")
print(deleteNode(newAVL, 20))
print("<------------------------>")
searchNode(newAVL, 20)
