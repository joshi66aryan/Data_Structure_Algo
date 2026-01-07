# Container With Most Water
# Medium


# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the 
# two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1

def maxArea(height):
    """
    LeetCode #11 - Container With Most Water
    Given n non-negative integers representing vertical lines at x-coordinates 0 to n-1,
    find two lines that together with the x-axis form a container that holds the most water.
    
    Two-pointer technique (greedy):
        - Start with the widest possible container (left = 0, right = n-1)
        - The area is determined by:  width * min(height[left], height[right])
        - To possibly get a larger area, we must move the pointer pointing to the SHORTER line
          because moving the taller one would only decrease the width without increasing height.
        - Repeat until the pointers meet.
    
    Time Complexity : O(n) — each element is visited at most once
    Space Complexity: O(1) — only using two pointers
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    
    # Continue until the two pointers meet
    while left < right:
        # Current width (distance between the two lines)
        width = right - left
        
        # The water level is limited by the shorter of the two lines
        current_height = min(height[left], height[right])
        
        # Area of the current container
        current_area = width * current_height
        
        # Update the global maximum area if current is larger
        max_area = max(max_area, current_area)
        
        # Greedy choice:
        # Move the pointer with the smaller height inward.
        # Reason: The current height is capped by the shorter bar.
        # Keeping the taller bar and moving it would only reduce width,
        # while moving the shorter one might give us a taller bar later.
        if height[left] < height[right]:
            left += 1          # move left pointer rightward
        else:
            right -= 1         # move right pointer leftward (also covers equal case)
    
    return max_area

"""
Step-by-step iteration trace:

Step | left | right | height[left] | height[right] | width | min_h | area  | max_area | move
-----+------+-------+--------------+---------------+-------+-------+-------+----------+------
1    | 0    | 8     | 1            | 7             | 8     | 1     | 8     | 8        | left  (1 < 7)
2    | 1    | 8     | 8            | 7             | 7     | 7     | 49    | 49       | right (8 > 7)
3    | 1    | 7     | 8            | 3             | 6     | 3     | 18    | 49       | right (8 > 3)
4    | 1    | 6     | 8            | 8             | 5     | 8     | 40    | 49       | right (equal → move right)
5    | 1    | 5     | 8            | 4             | 4     | 4     | 16    | 49       | right (8 > 4)
6    | 1    | 4     | 8            | 5             | 3     | 5     | 15    | 49       | right (8 > 5)
7    | 1    | 3     | 8            | 2             | 2     | 2     | 4     | 49       | right (8 > 2)
8    | 1    | 2     | 8            | 6             | 1     | 6     | 6     | 49       | stop (left >= right)

The maximum area found is 49 (between index 1 (height 8) and index 8 (height 7)).
"""




if __name__ == "__main__":
    print(f"Result1:{maxArea([1,8,6,2,5,4,8,3,7])}")
    print(f"Result1:{maxArea([1,1])}")