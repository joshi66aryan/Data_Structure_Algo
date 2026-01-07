# The function takes three arguments:
# set: a list of numbers (e.g., [3, 4, 5])
# n: the number of elements in the set (e.g., 3)
# sum: the target sum we want to achieve (e.g., 7)
def isSubsetSum(set, n, sum): 
      
    # We create a 2D array (like a spreadsheet) called 'subset'.
    # It will have (n + 1) rows and (sum + 1) columns.
    # subset[i][j] will be True if a sum of 'j' can be made 
    # using the first 'i' numbers from our set. Otherwise, it will be False.
    subset =([[False for i in range(sum + 1)]  
            for i in range(n + 1)]) 
      
    # --- Initialization Step 1 ---
    # If the target sum is 0, the answer is always True because 
    # we can just pick no numbers (an empty set) to get a sum of 0.
    # This fills the entire first column (where j=0) with True.
    for i in range(n + 1): 
        subset[i][0] = True
          
    # --- Initialization Step 2 ---
    # If we have no numbers from the set (the first row, where i=0), 
    # we can't make any sum greater than 0.
    # This fills the rest of the first row (where i=0 and j>0) with False.
    for i in range(1, sum + 1): 
         subset[0][i]= False
              
    # --- The Main Logic: Filling the rest of the table ---
    # We loop through each number in our set (from i=1 to n).
    for i in range(1, n + 1): 
        # And for each number, we loop through each possible sum (from j=1 to sum).
        for j in range(1, sum + 1): 
            # Get the current number we are considering. Note: set[i-1] because lists are 0-indexed.
            current_number = set[i-1]
            
            # Case 1: The current number is larger than the target sum 'j'.
            # If so, we can't include it. The only way to make sum 'j' is by
            # using the numbers *before* this one. So, we just copy the value from the cell directly above.
            if j < current_number: 
                subset[i][j] = subset[i-1][j] 
                
            # Case 2: The current number is less than or equal to the target sum 'j'.
            # Here, we have two choices:
            #   Choice A: Don't include the current number.
            #   Choice B: Include the current number.
            # If either choice leads to a True, then we can make the sum.
            if j >= current_number: 
                # subset[i-1][j] is Choice A (Exclude the current number).
                # subset[i-1][j - current_number] is Choice B (Include the current number).
                #   If we include it, we need to check if the *remaining sum* could be made with the previous numbers.
                subset[i][j] = (subset[i-1][j] or 
                                subset[i-1][j - current_number]) 
 
    # The final answer is in the bottom-right corner of our table,
    # which tells us if the total 'sum' can be made using all 'n' numbers.
    return subset[n][sum]

# This is the standard way to make a Python script runnable
if __name__ == '__main__':
    # Define your set of numbers and the target sum
    my_set = [3, 34, 4, 12, 5, 2]
    target_sum = 9
    
    # Get the number of elements in the set
    n = len(my_set)
    
    # Call the function and check its return value (True or False)
    if isSubsetSum(my_set, n, target_sum) == True:
        print(f"✅ Found a subset in {my_set} with sum {target_sum}")
    else:
        print(f"❌ No subset found in {my_set} with sum {target_sum}")
        
    # --- You can test another case! ---
    another_sum = 30
    if isSubsetSum(my_set, n, another_sum) == True:
        print(f"✅ Found a subset in {my_set} with sum {another_sum}")
    else:
        print(f"❌ No subset found in {my_set} with sum {another_sum}")
        

# DP Table for set = {3, 4, 5}, sum = 7
#
# Rows: Items considered | Columns: Target Sum
# ---------------------------------------------------------------------
#            S=0    S=1    S=2    S=3    S=4    S=5    S=6    S=7
# ---------------------------------------------------------------------
# {}      |  True   False  False  False  False  False  False  False
# {3}     |  True   False  False  True   False  False  False  False
# {3,4}   |  True   False  False  True   True   False  False  True
# {3,4,5} |  True   False  False  True   True   True   False  True
# ---------------------------------------------------------------------