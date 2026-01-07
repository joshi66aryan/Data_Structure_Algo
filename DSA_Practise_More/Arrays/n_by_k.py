# Given Array of size n and a number k, find all elements that appear more than n/k times

# Examples:

# Input: arr[ ] = [3, 4, 2, 2, 1, 2, 3, 3], k = 4
# Output: [2, 3]
# Explanation: Here n/k is 8/4 = 2, therefore 2 appears 3 times in the array that is 
# greater than 2 and 3 appears 3 times in the array that is greater than 2

# Input: arr[ ] = [9, 10, 7, 9, 2, 9, 10], k = 3
# Output: [9]
# Explanation: Here n/k is 7/3 = 2, therefore 9 appears 3 times in the array that is greater than 2.


def findElements(arr, k):
    """
    Algorithm Used: Extended Boyer–Moore Majority Vote Algorithm
    ------------------------------------------------------------
    Goal: Find all elements appearing more than n/k times.
    Fact: At most (k-1) elements CAN appear more than n/k times.

    Why?
    If an element appears > n/k times, only (k-1) such elements can fit
    into an array of size n.
    """

    n = len(arr)

    # Edge case: If k < 2, invalid scenario
    if k < 2:
        return []

    # ============================================================
    # STEP 1 — FIRST PASS: IDENTIFY POTENTIAL CANDIDATES
    # ============================================================
    # We maintain a dictionary of at most (k-1) candidates.
    # Each candidate has a counter.
    # If we try to add a new candidate but already have (k-1),
    # we decrement counts of all. This "cancels out" frequencies.
    #
    # Time Complexity (first pass): O(n * (k-1)) worst case
    # Space Complexity: O(k) for storing candidates
    # ============================================================

    candidates = {}  # Will store: number → tentative count

    # ------------------------------------------------------------
    # Example Walkthrough for arr = [3,4,2,2,1,2,3,3], k = 4
    # k-1 = 3 candidates allowed
    # ------------------------------------------------------------

    for num in arr:
        # If the number is already a candidate, increase its count
        if num in candidates:
            candidates[num] += 1

        # If we still have space (< k-1 candidates), add it
        elif len(candidates) < k - 1:
            candidates[num] = 1

        else:
            # No space for new candidate, decrement all
            keys_to_delete = []

            for key in candidates:
                candidates[key] -= 1

                # If count becomes zero, mark to remove
                if candidates[key] == 0:
                    keys_to_delete.append(key)

            # Delete zero-count candidates
            for key in keys_to_delete:
                del candidates[key]

        # ------------------- Iteration Example -------------------
        # For the first example:
        # Iteration 1: num = 3 → candidates = {3:1}
        # Iteration 2: num = 4 → candidates = {3:1, 4:1}
        # Iteration 3: num = 2 → candidates = {3:1, 4:1, 2:1}
        # Iteration 4: num = 2 → candidates = {3:1, 4:1, 2:2}
        # Iteration 5: num = 1 → already full (3 keys)
        #              decrement all → {3:0,4:0,2:1} → remove 3,4
        #              candidates = {2:1}
        # Iteration 6: num = 2 → candidates = {2:2}
        # Iteration 7: num = 3 → candidates = {2:2, 3:1}
        # Iteration 8: num = 3 → candidates = {2:2, 3:2}
        # ----------------------------------------------------------

    # ============================================================
    # STEP 2 — VERIFY CANDIDATES BY COUNTING THEIR REAL FREQUENCY
    # ============================================================
    # The first pass only gives POTENTIAL candidates.
    # Now we reset counts and recount them in the array.
    # ============================================================

    # Reset counts to 0
    for key in candidates:
        candidates[key] = 0

    # Count actual occurrences
    for num in arr:
        if num in candidates:
            candidates[num] += 1

    # ============================================================
    # STEP 3 — COLLECT VALID ANSWERS
    # ============================================================
    # Check which candidates actually appear > n/k times
    # ============================================================

    result = []
    threshold = n // k

    for key, count in candidates.items():
        if count > threshold:
            result.append(key)

    return result

    
    
if __name__ == '__main__':
    arr = [3, 4, 2, 2, 1, 2, 3, 3]
    ans = findElements(arr,4)
    print("The result:",ans)