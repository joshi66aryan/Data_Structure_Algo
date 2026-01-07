INT_MAX = 32767

def eggDrop(te,f):
    eggSheetDrop = ([[0 for i in range(f+1)] for i in range(te+1)])

    for i in range(1,te+1):
        eggSheetDrop[i][0] = 0
        eggSheetDrop[i][1] = 1


    for j in range(f+1):
        eggSheetDrop[1][j] = j

    for i in range(2,te+1):
        for j in range(2,f+1):

            eggSheetDrop[i][j] = INT_MAX
            for x in range(1,j+1):
                res  = 1 + max(eggSheetDrop[i-1][x-1], eggSheetDrop[i][j-x])

                if res < eggSheetDrop[i][j]:
                    eggSheetDrop[i][j] = res
    return eggSheetDrop[te][f]

if __name__ == "__main__":
    # You can change these values to test different scenarios
    eggs = 2
    floors = 10
    
    # Call the function with your chosen values
    result = eggDrop(eggs, floors)
    
    # Print the result in a clear, readable format
    print(f"Minimum number of trials for {eggs} eggs and {floors} floors is: {result}")



