# Longest Prefix Suffix
# Difficulty: Hard 
# Given a string s, of lowercase english alphabets, find the length of the longest proper prefix which is also a suffix.
# Note: Prefix and suffix can be overlapping but they should not be equal to the entire string.

# Examples :

# Input: s = "abab"
# Output: 2
# Explanation: The string "ab" is the longest prefix and suffix. 

# Input: s = "aabcdaabc"
# Output: 4
# Explanation: The string "aabc" is the longest prefix and suffix.

# Input: s = "aaaa"
# Output: 3
# Explanation: "aaa" is the longest prefix and suffix. 

# Constraints:
# 1 ≤ s.size() ≤ 106
# s contains only lowercase English alphabets.


class Solution:
    def getLPSLength(s):
        # Constants for Double Hashing (Reduces collision probability)
        base1, base2 = 31, 37
        mod1, mod2 = int(1e9 + 7), int(1e9 + 9)
        
        # p1 tracks (base1^i). Used to add characters to the "end" of the prefix.
        # Ex: i=0 -> p1=1 | i=1 -> p1=31 | i=2 -> p1=961
        p1 = p2 = 1
        n = len(s)
        
        hash1 = [0, 0] # Tracks Prefix Hash
        hash2 = [0, 0] # Tracks Suffix Hash
        ans = 0

        # We loop up to n-1 because a 'proper' prefix cannot be the whole string.
        for i in range(n - 1):
            # --- PREFACE FOR EXAMPLE s = "ababab" at i = 1 ---
            
            # UPDATE PREFIX: Add new char to the right side (highest power)
            # Logic: hash = current_hash + (new_char * base^i)
            # Example (i=1, char='b'): hash1 = ('a'*31^0) + ('b'*31^1)
            val_front = ord(s[i]) - ord('a') + 1
            hash1[0] = (hash1[0] + val_front * p1) % mod1
            hash1[1] = (hash1[1] + val_front * p2) % mod2

            # UPDATE SUFFIX: Add new char to the left side (lowest power)
            # Logic: hash = (old_suffix_hash * base) + new_char
            # This "pushes" existing chars to higher powers and puts new char at base^0.
            # Example (i=1, char='a'): hash2 = ('b'*31^0) -> ('b'*31^1 + 'a'*31^0)
            val_back = ord(s[n - i - 1]) - ord('a') + 1
            hash2[0] = (hash2[0] * base1 + val_back) % mod1
            hash2[1] = (hash2[1] * base2 + val_back) % mod2

            # CHECK MATCH: If hashes are equal, prefix of length (i+1) == suffix
            # i=0: "a" vs "b" (No)
            # i=1: "ab" vs "ab" (MATCH!) -> ans = 1 + 1 = 2
            # i=3: "abab" vs "abab" (MATCH!) -> ans = 3 + 1 = 4
            if hash1 == hash2:
                ans = i + 1

            # UPDATE POWERS: Increase p1 to base^(i+1) for the next prefix char
            # Example: after i=0 (p1=1), p1 becomes 31. Next prefix char uses 31.
            p1 = (p1 * base1) % mod1
            p2 = (p2 * base2) % mod2

        return ans
            

if __name__ == "__main__":
    x = input("Enter text")
    s = Solution()
    print(f"Longest proper suffix length: {s.getLPSLength(x)}")