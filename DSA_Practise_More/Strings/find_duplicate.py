# Print all the duplicate characters in a string

# Given a string s, the task is to identify all characters that appear more than once and print each as
# a list containing the character and its count.

# Examples:

# Input: s = "geeksforgeeks"
# Output: ['e', 4], ['g', 2], ['k', 2], ['s', 2]
# Explanation: Characters e, g, k, and s appear more than once. Their counts are shown in order of first occurrence.

# Input: s = "programming"
# Output: ['r', 2], ['g', 2], ['m', 2]
# Explanation: Only r, g, and m are duplicates. Output lists them with their counts.

# Input: s = "mississippi"
# Output: ['i', 4], ['s', 4], ['p', 2]
# Explanation: Characters i, s, and p have multiple occurrences. The output reflects that with count and order preserved.

class solution:
    def find_duplicate(self, arr:str):
        freq = {}
        for item in arr:
            freq[item] = freq.get(item, 0) + 1
        
        for key in freq:
            if freq[key] > 1:
                print(["{}".format(key), freq[key]], end =",")


if __name__ == "__main__":
    s = solution()
    s.find_duplicate("geeksforgeeks")
    print("\n")
    s.find_duplicate("programming")
    print("\n")
    s.find_duplicate("mississippi")