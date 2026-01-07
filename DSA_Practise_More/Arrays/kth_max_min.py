import numpy as np
import heapq

# Given an integer array arr[] and an integer k, your task is to 
# find and return the kth smallest element in the given array.

# # my first try:
# def find_kth_max_min(arr, k):
    
#     # maintain two list min_list, max_list
#     max_list = min_list = []
#     max_vlu =  min_list = arr[0]

#     for item in arr:
#         if item > max_vlu:
#             max
#         # compare and push it into the respective array max_list, min_list.

#     # take the k element from respective list
#     #  return the kth max and kth min elements.


def kth_max_min(arr,k):
    """
    Returns both the k-th smallest and k-th largest elements from the array.
    Automatically selects the most efficient algorithm based on data size.

    Time Complexities:
        -- Sorting Method: O(n logn)
        -- Numpy Partition:O(n) average introspect algorithm.
        -- Heap Fallback: O(n + k logn)
    """

    n = len(arr)
    if k < 1 or k > n:
        raise ValueError("\n K is out of range \n")
    
    
    # -- Case 1: Small or medium array
    if n < 10_000:
        arr.sort()                                      # it doesn't return the new array, O(n logn)
        return arr[-k], arr[k-1]                        # O(1)


    # -- Case 2: Large array (use introspect array) --
    try:
        # np.partition using Introselect (QuickSort + HeapSort fallback)
        kth_small = np.partition(arr, k-1)[k - 1]       # O(n)
        kth_large = np.partition(arr, n - k)[n - k]     # O(n)

        # print("kth_small_p--->",kth_small)
        # print("kth_large_p--->",kth_large)
        
        return kth_large, kth_small                     # O(1)


    # -- Case 3: Fallback if Numpy available or error occurs -- 
    except Exception:

        # find  k-th smallest element.

        # make an copy of an array to avoid modifying the array.
        min_heap = arr[:]                               # O(n)

        # convert the list into the valid min-heap (smallest element at the top).
        heapq.heapify(min_heap)                         # O(n)

        # pop the smallest element k-1 times.
        for _ in range(k-1):                            # (k-1) * O(log n)
            heapq.heappop(min_heap)
        
        # next popped element is k-th smallest.
        kth_small = heapq.heappop(min_heap)             # O(log n)



        # find k-th largest element.

        # convert all the numbers to negatives so that we can create min-heap as max-heap.
        max_heap = [-x for x in arr]                    # O(n)

        # now build the max-heap 
        heapq.heapify(max_heap)                         # O(n)

        # print("max_heap--->",max_heap)
        # print("min_heap--->",min_heap)
        
        # pop the largest which is the most negative (k-1 times)
        for _ in range(k-1):                            # (k-1) * O(log n)
            heapq.heappop(max_heap)

        # the next popped value is the k-th most largest value -- convert it to positive.
        kth_large = -heapq.heappop(max_heap)            # O(log n)

        return kth_large, kth_small                     # O(1)





    


if __name__ == '__main__':
    x = input("Enter the array")
    arr = list(map(int, x.split()))
    k  = int(input("Enter the k"))
    # print(" Array --> ",arr, "\n k --> ",k)
    kth_max, kth_min = kth_max_min(arr,k)
    print("kth-max",kth_max, "kth-min", kth_min)


