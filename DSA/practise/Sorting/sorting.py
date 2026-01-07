import math

def bubbleSort(arr):
    for  i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]  = arr[j+1], arr[j]
    return arr


def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index], arr[i] 
    return arr

def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    return arr

def bucketSort(customList):
    noOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(noOfBuckets):
        arr.append([])

    # separate
    for j in customList:
        index_b = math.ceil(j * noOfBuckets / maxValue)
        arr[index_b-1].append(j)

    # insertion sort
    for i in range(noOfBuckets):
        arr[i] = insertionSort(arr[i])

    #combine
    k = 0 
    for i in range(noOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

#### Merge Sort
def merge(customList, l , m, r):
    # index for two different array
    n1 = m - l+1
    n2 = r-m

    # creating two different list
    L = [0] * (n1)
    M = [0] * (n2)

    # coping element from the original list to the temporary list
    for i in range(0,n1):
        L[i] = customList[l+i]

    for j in range(0,n2):
        M[j] = customList[m+1+j]

    # merging the two array
    i = 0 
    j = 0
    k = l 
    while i < n1 and j < n2:
        if L[i] <= M[j]:
            customList[k] = L[i] 
            i += 1
        else:
            customList[k] = M[j]
            j += 1
        k += 1

    # merging remaining element in the array.
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        customList[k] = M[j]
        j += 1
        k += 1
    return customList

def mergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(customList, l , m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)
    return customList

#### Quick Sort
def partition(customList, low, high):
    pivot = customList[high]
    i = low -1
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1 
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1],customList[high] = customList[high], customList[i+1]
    return (i+1)

def quickSort(customList, low, high):
    if low < high:
        partitionIndex = partition(customList, low, high)
        quickSort(customList, low, partitionIndex-1)
        quickSort(customList, partitionIndex+1, high)
    return customList

def heapify(customList, numberOfItem, i):
    smallest = i
    leftChild = 2*i + 1
    rightChild = 2*i + 2

    if leftChild < numberOfItem and customList[leftChild] < customList[smallest]:
        smallest = leftChild
    
    if rightChild < numberOfItem and customList[rightChild] < customList[smallest]:
        smallest = rightChild

    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, numberOfItem, smallest) 

def heapSort(customList):
    n = len(customList)

    # build heap tree
    for i in range(int(n/2)-1, -1, -1):
        heapify(customList, n, i)

    #extract from the heapify
    for i in range(n-1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)


cList = [2,1,7,6,5,3,4,9,8]
# print(mergeSort(cList, 0, 8))
# print(quickSort(cList, 0 , 8))
heapSort(cList)
print(cList)

