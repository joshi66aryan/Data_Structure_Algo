# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 10**4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10**4 

def merge_interval(intervals):
    # Edge case: empty input
    if not intervals:
        return []
    
    # STEP 1: Sort intervals by start time
    # This ensures we process intervals from left to right
    # Time: O(n log n)
    intervals.sort(key=lambda x: x[0])
    
    merged = []                    # Final result (non-overlapping intervals)
    current = intervals[0].copy()  # Current interval being processed [start, end]
    
    # STEP 2: Traverse all intervals (starting from second)
    # Time: O(n)
    for interval in intervals[1:]:
        curr_start, curr_end = current
        next_start, next_end = interval
        
        # Check for overlap: current interval ends after next starts
        if curr_end >= next_start:
            # Overlap → merge by taking the maximum end
            current[1] = max(curr_end, next_end)
        else:
            # No overlap → finalize current interval and start new one
            merged.append(current)
            current = interval.copy()  # or list(interval)
    
    # Don't forget to add the last interval!
    merged.append(current)
    
    return merged




if __name__ == '__main__':
    arr1 = [[1,3],[2,6],[8,10],[15,18]]
    arr2 = [[1,4],[4,5]]
    arr3 = [[4,7],[1,4]]
    arr4 = [[1,2],[3,4],[5,6]]

    ans1 = merge_interval(arr1)
    ans2 = merge_interval(arr2)
    ans3 = merge_interval(arr3)
    ans4 = merge_interval(arr4)

    print("merge interval 1",ans1)
    print("merge interval 2",ans2)
    print("merge interval 3",ans3)
    print("merge interval 4",ans4)


