import math

# ### Bubble Sort Recap

# Bubble Sort works by repeatedly comparing **adjacent pairs** and swapping them if they are in the wrong order.
# On each pass:

# * The **largest remaining element** "bubbles up" to its correct final position at the end of the list.
# * That means the last element of the first pass is guaranteed to be the maximum, the last two elements after the second pass are sorted, etc.

# ---

# ### Outer Loop: `for i in range(len(customList) - 1):`

# * We subtract **1** because when there’s only **1 element left**, it’s already sorted.
# * So, we only need to make **n-1 passes** (if list length is `n`).
#   Example: In a list of length 5, you need at most 4 passes.

# ---

# ### Inner Loop: `for j in range(len(customList) - i - 1):`

# * Each pass puts one element in its correct place at the end.
# * After the first pass, the last element is correct. After the second pass, the last two are correct, and so on.
# * That’s why we **don’t need to check the already sorted part**.

# So:

# * On pass `i = 0` → compare `j` from `0` to `n-2` (check all pairs).
# * On pass `i = 1` → compare `j` from `0` to `n-3` (last element already in place).
# * On pass `i = 2` → compare `j` from `0` to `n-4`.
# * … and so on.

# That’s why it’s `len(customList) - i - 1`.

# ---

# ### Example Walkthrough

# List = `[4, 3, 2, 1]`, length = 4

# * **Outer loop (i=0):** inner loop runs `range(3)` → compares indices `[0,1,2]`
#   largest element `4` moves to last index.
# * **Outer loop (i=1):** inner loop runs `range(2)` → compares indices `[0,1]`
#   next largest element `3` moves to index 2.
# * **Outer loop (i=2):** inner loop runs `range(1)` → compares index `[0]`
#   `2` moves before `3`.
# * Outer loop stops at `i=2` (because `len-1 = 3` passes total). Sorted list = `[1,2,3,4]`.

# ---

# ✅ In short:

# * `-1` in the **outer loop** avoids unnecessary final pass.
# * `-i-1` in the **inner loop** avoids checking already sorted elements at the end.

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)

# https://www.programiz.com/dsa/selection-sort
def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)

# Initial: [2, 4, 5, 6, 1]   (hole at index 4)
# After shift 6: [2, 4, 5, 6, 6]   (hole at index 3)
# After shift 5: [2, 4, 5, 5, 6]   (hole at index 2)
# After shift 4: [2, 4, 4, 5, 6]   (hole at index 1)
# After shift 2: [2, 2, 4, 5, 6]   (hole at index 0)
# Insert key →   [1, 2, 4, 5, 6]

# http://programiz.com/dsa/insertion-sort
def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    # creating bucket in the array
    for i in range(numberofBuckets):
        arr.append([])

    # finding out the index of particular number to insert into bucket
    for j in customList:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)
    
    # sorting the number within the bucket
    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])
    
    # recombining
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

def merge(customList, l, m, r):
    n1 = m - l + 1        # size of left half [l..m]
    n2 = r - m            # size of right half [m+1..r]

    L = [0] * n1          # temp arrays
    R = [0] * n2

    # copy the two sorted halves into temps
    for i in range(n1):
        L[i] = customList[l + i]
    for j in range(n2):
        R[j] = customList[m + 1 + j]

    i = j = 0             # pointers in L and R
    k = l                 # write pointer in customList

    # merge while both halves still have elements
    while i < n1 and j < n2:
        if L[i] <= R[j]:           # <= keeps it **stable**
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1

    # copy leftovers (only one of these loops will run)
    while i < n1:
        customList[k] = L[i]
        i += 1; k += 1
    while j < n2:
        customList[k] = R[j]
        j += 1; k += 1


def mergeSort(customList, l, r):
    if l < r:                          # more than one element
        m = (l + (r - 1)) // 2         # pick a middle index
        mergeSort(customList, l, m)    # sort left half
        mergeSort(customList, m+1, r)  # sort right half
        merge(customList, l, m, r)     # merge halves
    return customList


# Helper function to partition the list.
def partition(customList, low, high):
    # Initialize a pointer for the smaller element.
    i = low - 1                  # i keeps track of the "smaller than pivot" region

    # Select the pivot, here the last element is chosen.
    pivot = customList[high]     # pivot is chosen as the last element

    # Iterate through the list from 'low' to 'high - 1'.
    for j in range(low, high):   # loop through all elements except pivot
        # If the current element is smaller than or equal to the pivot,
        if customList[j] <= pivot:
            # Increment the index of the smaller element
            i += 1
            # and swap it with the current element.
            customList[i], customList[j] = customList[j], customList[i]

            # 🔹 Example:
            # Suppose pivot = 8 and current j=3 (value=5)
            # Since 5 <= 8, we increase i and swap 5 into the "smaller region".

    # Place the pivot at its correct position in the sorted list.
    customList[i+1], customList[high] = customList[high], customList[i+1]

    # 🔹 This ensures that all elements left of pivot ≤ pivot and right of pivot > pivot.

    # Return the partition index (where the pivot is placed).
    return (i+1)


def quickSort(customList, low, high):
    # Base case: if the subarray has more than 1 element
    if low < high:
        # Partition the array and get pivot index
        pi = partition(customList, low, high)

        # 🔹 Now pivot is at its correct sorted position

        # Recursively sort the left half (before pivot)
        quickSort(customList, low, pi-1)

        # Recursively sort the right half (after pivot)
        quickSort(customList, pi+1, high)


#### document to understand better:----> https://medium.com/@ishta.pal/heap-sort-explained-using-python-4f1466509521
# Helper function to heapify a subtree rooted with node 'i'.
def heapify(customList, n, i):
    # Initialize the smallest element as the root.
    smallest = i                     # index of the root of the current subtree
                                      # NOTE: this implementation enforces a MIN-heap:
                                      # the root will be the smallest element in the subtree.
    # Calculate the left child's index.
    l = 2 * i + 1                    # left child index (0-based array): if i=0 -> left=1
    # Calculate the right child's index.
    r = 2 * i + 2                    # right child index (0-based array): if i=0 -> right=2
    
    # If the left child exists and is smaller than the smallest so far,
    if l < n and customList[l] < customList[smallest]:
        # update the smallest element's index.
        smallest = l                # left child becomes the candidate smallest element
    
    # If the right child exists and is smaller than the smallest so far,
    if r < n and customList[r] < customList[smallest]:
        # update the smallest element's index.
        smallest = r                # right child becomes the candidate smallest element
    
    # If the smallest element is not the root,
    if smallest != i:
        # swap the root with the smallest element,
        customList[i], customList[smallest] = customList[smallest], customList[i]
                                      # place the smallest of the three (root, left, right)
                                      # at the root position `i`
        # and recursively heapify the affected subtree.
        heapify(customList, n, smallest)
                                      # recursively ensure the subtree rooted at `smallest`
                                      # also satisfies the MIN-heap property


def heapSort(customList):
    # Get the number of elements in the list.
    n = len(customList)              # total number of elements to sort
    
    # Build a heap.
    # The loop starts from the last non-leaf node and works its way up to the root.
    # last non-leaf index in a 0-based array is (n//2 - 1).
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i)   # ensure every subtree satisfies the heap property
                                    # after this loop, `customList` is a MIN-heap because
                                    # heapify uses '<' comparisons.
    
    # Extract elements one by one from the heap and place them at the end of the list.
    for i in range(n - 1, 0, -1):
        # Swap the current root (smallest element for a MIN-heap) with the last element.
        customList[i], customList[0] = customList[0], customList[i]
                                      # move the root (smallest) into its final position at `i`
                                      # NOTE: because this code builds a MIN-heap, this places
                                      # the smallest element at the end, so the result after
                                      # all extractions will be in DESCENDING order (largest -> smallest).
        # Heapify the reduced heap.
        heapify(customList, i, 0)    # rebuild the heap property for the array slice [0:i]
                                      # (we treat the first `i` elements as the heap)
    # Important note about ordering:
    # - If heapify builds a MAX-heap (root = largest), the sequence of swaps above
    #   produces an ascending-sorted list (smallest .. largest).
    # - In this code, `heapify` is a MIN-heap version, so the final list will be descending.
    # To obtain ascending order with the current MIN-heap `heapify`, either:
    #   1) reverse the final list: customList.reverse()
    #   2) rewrite heapify to create a MAX-heap (see alternative below).




cList = [2,1,7,6,5,3,4,9,8]
heapSort(cList)
print(cList)




        