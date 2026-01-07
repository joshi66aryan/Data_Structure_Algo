# Defines a function to find the length of the Shortest Common Supersequence (SCS).
# X and Y are the input strings.
# m and n are the current lengths of X and Y we are considering in the recursion.
def SCSLength(X, Y, m, n):
	# This is the base case or stopping condition for the recursion.
	# If one string is empty, the SCS must contain all characters of the other string.
	if m == 0 or n == 0:
		# For example, SCS of "" and "CAT" is "CAT". Length is 0 + 3 = 3.
		return n + m
	# --- Recursive Steps ---
	
	# Case 1: The last characters of the current strings match.
	# We use m-1 and n-1 because strings are 0-indexed.
	if X[m - 1] == Y[n - 1]:
		# Since they match, we can include this character just ONCE in our supersequence.
		# Then, we find the SCS for the remaining parts of the strings (everything before the last character).
		# We add 1 to count the current matching character.
		return SCSLength(X, Y, m - 1, n - 1) + 1

	# Case 2: The last characters of the strings DO NOT match.
	else:
		# We have two choices, and we must pick the one that results in a shorter supersequence.
		# Option A: We "use" the last character of string X. We add it to our supersequence (costing 1), 
		# and then find the SCS of the rest of string X (m-1) and all of string Y (n).
		option_A = SCSLength(X, Y, m - 1, n) + 1
		
		# Option B: We "use" the last character of string Y. We add it to our supersequence (costing 1),
		# and then find the SCS of all of string X (m) and the rest of string Y (n-1).
		option_B = SCSLength(X, Y, m, n - 1) + 1

		# We return the minimum of the two options because we want the SHORTEST supersequence.
		return min(option_A, option_B)

# Example Usage:
X = "AGGTAB"
Y = "GXTXAYB"
print(f"Length of the Shortest Common Supersequence is {SCSLength(X, Y, len(X), len(Y))}")
# Expected Output: Length of the Shortest Common Supersequence is 9
# The SCS is "AGXGTXAYB"