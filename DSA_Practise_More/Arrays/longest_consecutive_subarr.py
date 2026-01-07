# Longest Consecutive Subsequence:

# Given an array of integers, the task is to find the length of the longest subsequence 
# such that elements in the subsequence are consecutive integers, the consecutive numbers 
# can be in any order. 

# Examples:  

# Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
# Output: 6
# Explanation:  The longest consecutive subsequence [2, 6, 1, 4, 5, 3].

# Input: arr[] = [1,1,1,2,2,3]
# Output: 3
# Explanation: The subsequence [1, 2,3] is the longest subsequence of consecutive elements


def longestConsecutive(arr):
    if not arr:                     # Edge case: empty array
        return 0                    # → return 0, no sequence possible
                                    # Example: arr = [] → return 0
    
    num_set = set(arr)              # Put all elements into a set for O(1) lookup
                                    # Example: arr = [2,6,1,9,4,5,3] → num_set = {1,2,3,4,5,6,9}
                                    # Duplicates are auto-removed → [1,1,1] becomes {1}
    
    max_len = 0                     # Track the longest consecutive sequence found so far
                                    # Initially 0

    for x in arr:                   # Iterate through each number in original array
                                    # Example: x = 2 → 6 → 1 → 9 → 4 → 5 → 3
        # Only start counting a sequence if (x-1) is NOT in the set
        # This ensures we only start from the beginning of a chain
        if x - 1 not in num_set:    # Is x the start of a new sequence?
                                    # Example:
                                    # x=2 → 1 is in set → skip (not start)
                                    # x=6 → 5 is in set → skip
                                    # x=1 → 0 not in set → YES! Start sequence from 1
            curr = x                # Current number we're checking in the sequence
                                    # Example: x=1 → curr=1
            curr_len = 1            # Length of current sequence, starts at 1
                                    # Example: curr_len = 1 (just 1)
            
            # Keep extending the sequence: 1, 2, 3, 4, ...
            while curr + 1 in num_set:   # Check if next number exists
                                            # Example: curr=1 → 2 in set? Yes → enter loop
                curr += 1                # Move to next number
                                            # Example: curr=1 → 2 → 3 → 4 → 5 → 6
                curr_len += 1            # Increment length
                                            # Example: 1 → 2 → 3 → 4 → 5 → 6
                                            # curr_len = 6 when loop ends
            
            # Update global max if current sequence is longer
            max_len = max(max_len, curr_len)
                                    # Example: max_len = max(0, 6) → 6

    return max_len                  # Final answer: longest consecutive subsequence length
                                    # Example: return 6

     

if __name__ == '__main__':
    arr = [1,2,3]
    ans = longestConsecutive(arr)
    print("The result:",ans)
