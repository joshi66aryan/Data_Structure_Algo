# Array Subset
# Difficulty: Basic 
# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

# Examples:

# Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# Output: true
# Explanation: b[] is a subset of a[]

# Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
# Output: true
# Explanation: b[] is a subset of a[]

# Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
# Output: false
# Explanation: b[] is not a subset of a[]

# Constraints:
# 1 <= a.size(), b.size() <= 105
# 1 <= a[i], b[j] <= 106

# Expected Complexities

# Time Complexity: O(n + m)
# Auxiliary Space: O(n)





def isSubset(a, b):
    """
    Determine whether b[] is a subset of a[] using a frequency map.
    Time Complexity:  O(n + m)
        - Build frequency map of a[]  → O(n)
        - Check elements of b[]       → O(m)
    Space Complexity: O(n)
        - Frequency dictionary storing counts of a[] elements
    """

    # --------------------------------------------------------
    # STEP 1: Build a frequency map for array a[]
    # --------------------------------------------------------
    freq = {}

    for x in a:
        # Add element to freq map OR increase its count
        freq[x] = freq.get(x, 0) + 1

    """
    Example for: a = [11, 7, 1, 13, 21, 3, 7, 3]

    freq will become:
    {
        11: 1,
        7:  2,
        1:  1,
        13: 1,
        21: 1,
        3:  2
    }
    """

    # --------------------------------------------------------
    # STEP 2: Check if each element in b[] can be matched
    #         with available counts inside freq map
    # --------------------------------------------------------
    for x in b:

        # If element is missing OR count exhausted → not a subset
        if x not in freq or freq[x] == 0:
            return False

        # Otherwise, consume one occurrence
        freq[x] -= 1

        """
        -------------------------------------------------------
        Example iteration for: b = [11, 3, 7, 1, 7]

        Initial freq map:
        11:1, 7:2, 1:1, 13:1, 21:1, 3:2

        Iteration 1: x = 11
            freq[11] = 1 → OK
            After use: freq[11] = 0

        Iteration 2: x = 3
            freq[3] = 2 → OK
            After use: freq[3] = 1

        Iteration 3: x = 7
            freq[7] = 2 → OK
            After use: freq[7] = 1

        Iteration 4: x = 1
            freq[1] = 1 → OK
            After use: freq[1] = 0

        Iteration 5: x = 7
            freq[7] = 1 → OK
            After use: freq[7] = 0

        All elements matched → Return True
        -------------------------------------------------------
        """

    # All elements of b[] were found in a[] with enough counts
    return True



if __name__ == '__main__':
    print("The answer is:",isSubset([10, 5, 2, 23, 19],[19, 5, 3]))
    print("The answer is:",isSubset([1, 2, 3, 4, 4, 5, 6],[1, 2, 4]))
    print("The answer is:",isSubset([11, 7, 1, 13, 21, 3, 7, 3],[11, 3, 7, 1, 7]))