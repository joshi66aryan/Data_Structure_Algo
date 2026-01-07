import math
def BinarySearch(array, value):
    start = 0
    end = len(array) - 1
    mid = math.floor((start + end)/2)
    while not (array[mid] == value) and start <= end:
        if value < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = math.floor((start+end)/2)
    if array[mid] == value:
        return mid
    else:
        return -1 

# array = [8, 9, 12, 15, 17, 19, 20, 21, 28]
# print(BinarySearch(array, 15))


def LinearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return f"The value {value} is found at index {i}"
    return f"Not found."

array = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(LinearSearch(array, 15))