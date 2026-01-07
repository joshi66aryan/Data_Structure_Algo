class Heap:
    def __init__(self, size):
        self.customList = (size + 1)* [None]
        self.maxHeapSize = size + 1
        self.heapSize = 0

# peak
def peakOfHeap(rootNode):
    if not rootNode:
        return None
    return rootNode.customList[1]

# size
def heapSize(rootNode):
    if not rootNode:
        return None
    return rootNode.heapSize

# level order traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return None
    for i in range(1, rootNode.heapSize+1):
        print(rootNode.customList[i])

# heapifyTree insert
def heapifyTreeInsert(rootNode, index, heapType):
    if not rootNode:
        return None
    if index <= 1:
        return
    parentIndex = int(index/2)

    if heapType == "MIN":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

    elif heapType == "MAX":
            if rootNode.customList[index] > rootNode.customList[parentIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[parentIndex]
                rootNode.customList[parentIndex] = temp
            heapifyTreeInsert(rootNode, parentIndex, heapType)

# insertNode
def insertNode(rootNode, nodeVlu, heapType):
    if rootNode.heapSize + 1 == rootNode.maxHeapSize:
        return "The binary heap is full."
    
    rootNode.customList[rootNode.heapSize+1] = nodeVlu
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value is inserted successfully."

# heapify tree extract
def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    
    # only one child.
    elif rootNode.heapSize == leftIndex:
        if heapType == "MIN":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
                return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

    # having the both child.
    else:
        if heapType == "MIN":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp

    heapifyTreeExtract(rootNode, swapChild, heapType)


# extract node
def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode

# delete entire Binary Heap.
def deleteBH(rootNode):
    rootNode.customList = None
    return "The tree is emptied."

heap = Heap(5)
insertNode(heap, 4, "MAX")
insertNode(heap, 5, "MAX")
insertNode(heap, 2, "MAX")
insertNode(heap, 1, "MAX")
print("<----------------------->")
print(peakOfHeap(heap))
print("<----------------------->")
print(heapSize(heap))
print("<----------------------->")
levelOrderTraversal(heap)

