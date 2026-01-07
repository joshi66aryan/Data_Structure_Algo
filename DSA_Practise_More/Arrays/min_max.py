def find_min_max(data):
    x = data[0]
    y = data[0]
    for item in data: # --> O(n)
        if x < item:  # --> O(n)
            x = item # worst case --> O(n)
    for item in data: # --> O(n)
        if item < y: # --> O(n)
            y = item # worst case --> O(n)
    return x,y

    ### Chat gpt correction
    # minimum = maximum = data[0]   
    # for item in data[1:]:
    #     if item > maximum:
    #         maximum = item
    #     if item < minimum:
    #         minimum = item
    # return maximum, minimum
  
    

if __name__ == '__main__':
    x  = input("Enter numbers \n")
    arr = list(map(int, x.split())) # --->  O(n)
    max_vlu, min_vlu = find_min_max(arr)  # --> O(n)
    print('arr------>',arr) # --> O(n)
    print('max------>',max_vlu) # --> O(1)
    print('min------>',min_vlu) # --> O(1)


    ### Chat gpt one line version


    # if __name__ == '__main__':
    # x = input("Enter numbers \n")
    # arr = list(map(int, x.split()))
    
    # # One-liner to get max and min
    # max_vlu, min_vlu = max(arr), min(arr)
    
    # print('arr------>', arr)
    # print('max------>', max_vlu)
    # print('min------>', min_vlu)
