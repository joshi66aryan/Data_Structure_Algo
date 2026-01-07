def numberFactor(n): 
  # This function counts the number of ways to express 'n' as a sum of 1s, 3s, and 4s.

  if n in (0, 1, 2): 
    # Base cases for small values of n.
    # For n=0, there's one way (sum of zero numbers).
    # For n=1, there's one way (1).
    # For n=2, there's one way (1+1).
    return 1 

  if n == 3: 
    # A special case for n=3.
    # There are two ways to get 3: (1+1+1) and (3).
    return 2 

  else: 
    # For any other n, we use a recursive approach.
    # This is based on the idea that the last number added to the sum can be 1, 3, or 4.
    
    sub1 = numberFactor(n-1) 
    # This is the number of ways to get n if the last number added was 1.
    # It's equivalent to finding the number of ways to get (n-1).
    
    sub2 = numberFactor(n-3) 
    # This is the number of ways to get n if the last number added was 3.
    # It's equivalent to finding the number of ways to get (n-3).
    
    sub3 = numberFactor(n-4) 
    # This is the number of ways to get n if the last number added was 4.
    # It's equivalent to finding the number of ways to get (n-4).
    
    return sub1 + sub2 + sub3 
    # The total number of ways to get n is the sum of all these possibilities.
    # This is a classic example of dynamic programming using recursion.

print(numberFactor(5))
# This line calls the function with n=5.
# The recursive calls will be:
# numberFactor(5) -> numberFactor(4) + numberFactor(2) + numberFactor(1)
# numberFactor(4) -> numberFactor(3) + numberFactor(1) + numberFactor(0)
# The final result will be 6.