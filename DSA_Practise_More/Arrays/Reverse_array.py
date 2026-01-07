def reverse_array(data):
    # slice operation creates new list that contain all the elements of data, but in reverse order. 
    # iterates through the entire list once and copy to the new list (in reverse order). 

    # other ways to do that:
    # 1. data.reverse() --> O(1) for space complexity which was not there in data[::-1]
    # 2. manual function to reverse --> O(n) for time and O(1) for space complexity.

    x =  data[::-1]
    return x



if __name__ == '__main__':
    x = input("Enter array items")
    # splitting goes through each item in the list.
    arr = x.split()
    print(reverse_array(arr))
    
