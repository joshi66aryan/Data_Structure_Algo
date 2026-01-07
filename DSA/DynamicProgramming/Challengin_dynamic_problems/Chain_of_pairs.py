# A crucial note for this algorithm to work correctly:
# The input array of pairs 'arr' should be sorted based on the first element 
# of each pair before being passed to this function.

# ----------------------------------------------------------------------------------

# Defines a simple class to represent a pair of numbers (a, b).
# Using a class like this with '.a' and '.b' can make the code more
# readable than using an index like 'pair[0]' and 'pair[1]'.
class Pair(object): 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 

# ----------------------------------------------------------------------------------
  
# This function calculates the length of the longest possible chain of pairs.
# It uses a technique called Dynamic Programming, which solves a problem
# by breaking it down into simpler subproblems.
def maxChainLength(arr, n): 
      
    # 'max' will store our final answer. It will be the largest chain
    # length we find among all possibilities. We start it at 0.
    max = 0
  
    # This is the core of our dynamic programming solution! 🧠
    # 'mcl' (Maximum Chain Length) is a list that stores the solution to our subproblems.
    # Specifically, mcl[i] will hold the length of the longest chain ENDING with the pair arr[i].
    # We initialize every value to 1, because every pair can be a chain of length 1 by itself.
    mcl = [1 for i in range(n)] 
  
 
    # This outer loop iterates through each pair in the array, starting from the second one.
    # We'll consider each 'arr[i]' as the potential end of a chain.
    for i in range(1, n): 
        # This inner loop looks at all the pairs 'arr[j]' that came *before* the current pair 'arr[i]'.
        # We are checking if any of these previous pairs can be the second-to-last link in a chain that ends with 'arr[i]'.
        for j in range(0, i): 
            
            # This 'if' statement has two critical checks:
            #
            # 1. The "Rule Check": (arr[i].a > arr[j].b)
            #    This checks if we are allowed to form a chain by placing pair 'i' after pair 'j'.
            #    The rule is that the first number of the next pair must be greater than the
            #    second number of the previous pair.
            #
            # 2. The "Improvement Check": (mcl[i] < mcl[j] + 1)
            #    This is like asking: "Is this a new high score?".
            #    - 'mcl[i]' is the current record for the longest chain ending at pair 'i'.
            #    - 'mcl[j] + 1' is the length of the chain we could form by taking the longest
            #      chain that ends at 'j' and adding our current pair 'i' to it.
            #    So, this check asks: "If we link to pair 'j', will it create a LONGER chain
            #    for pair 'i' than the best one we've found for it so far?"
            if (arr[i].a > arr[j].b and mcl[i] < mcl[j] + 1): 
                
                # If both checks pass, it means we've found a better, longer chain that ends at 'arr[i]'.
                # So, we update our record for 'mcl[i]' to this new, higher value.
                mcl[i] = mcl[j] + 1
  
   
    # At this point, the 'mcl' array is fully calculated. For example, mcl might look like [1, 1, 2, 3].
    # This means the longest chain ending at the last pair has a length of 3.
    # However, the overall longest chain might have ended at an earlier pair.
    # This final loop simply finds the single largest value in the entire 'mcl' array.
    for i in range(n): 
        if (max < mcl[i]): 
            max = mcl[i] 
  
    # Return the overall maximum length found.
    return max

pairs_data = [(5, 24), (39, 60), (15, 28), (27, 40), (50, 90)]

# 2. Convert the list of tuples into a list of Pair objects.
arr = [Pair(p[0], p[1]) for p in pairs_data]

# 3. CRITICAL STEP: Sort the array of Pair objects.
#    This specific algorithm requires the pairs to be sorted by their first element ('a').
#    The `lambda p: p.a` tells the sort function to look at the '.a' attribute of each Pair object.
arr.sort(key = lambda p: p.a)

# 4. Get the number of pairs.
n = len(arr)

# 5. Call the function with the sorted data and print the result.
result = maxChainLength(arr, n)
print(f"The length of the longest chain is: {result}")