# ------------------------------------------------------------------------------------
#
# CONCEPTUAL OVERVIEW & KEY ANALOGIES
#
# This program finds the "diff" between two strings by first finding what they have
# in common using the Longest Common Subsequence (LCS) algorithm.
#
# --- The Two-Step Process ---
# 1. Build a Map (`LCSLength` function) 🗺️:
#    First, we build a grid (`lookup` table) using dynamic programming. Each cell
#    `lookup[i][j]` stores the length of the LCS for the prefixes of the strings.
#    This table acts as a complete map of all optimal sub-solutions.
#
# 2. Follow the Map (`diff` function) 👣:
#    Once the map is built, we trace a path backward from the end. The direction
#    we move tells us if a character was a match, an addition, or a removal.
#
# --- The Recipe Analogy (Why Additions/Removals Work) 🍳 ---
# Think of S1 as an "old recipe" and S2 as a "new recipe". The LCS is the set
# of common ingredients.
#  - An ingredient in the new recipe (S2) but not the common set is an ADDITION (+).
#    The LCS algorithm finds this by "ignoring" the character from S2 to keep the
#    common sequence going.
#  - An ingredient in the old recipe (S1) but not the common set is a REMOVAL (-).
#    The LCS algorithm finds this by "ignoring" the character from S1.
#
# --- The Maze Analogy (How the Algorithm "Knows" the Path) ---
# The `lookup` table is like a solved maze where every intersection has a number
# indicating the best path length from the start. The `diff` function starts at
# the exit and works backward. At any point, it looks at the numbers on the
# paths behind it to know which way it came from, thus "knowing" which character
# to ignore (add/remove) or accept (match).


## How the "Knowing" Happens in Code

# The algorithm is at a point (m, n) where the characters S1[m-1] and S2[n-1] 
# do not match. It knows the number in lookup[m][n] was copied from either the
#  cell above or the cell to the left. To figure out which one, it simply compares 
# their values:

# Case 1: lookup[m-1][n] (Above) is larger.
# The "Memory": The table's numbers tell us that the best path leading 
# to our current spot came from above.

# The Deduction: This means the path completely bypassed the cell to t
# he left. The only way to do that is by "ignoring" or "skipping over"
#  the character S1[m-1].

# The Conclusion: If the best common sequence was found by skipping a 
# character from the original string S1, that character must not exist
#  in the final common sequence. Therefore, it's a removal (-).

# Case 2: lookup[m][n-1] (Left) is larger or equal.
# The "Memory": The table's numbers show the best path came from the left.
# The Deduction: This path bypassed the cell above. This was achieved by 
# "ignoring" the character S2[n-1].
# The Conclusion: If the best common sequence was found by skipping a 
# character from the target string S2, that character must not exist 
# in the common sequence. To transform S1 into S2, this character 
# must be an addition (+).

# ------------------------------------------------------------------------------------


# Function to recursively display the differences between two Strings.
# This function BACKTRACKS through the `lookup` table built by `LCSLength`.
# It starts from the bottom-right corner and works its way to the top-left.
def diff(S1, S2, m, n, lookup):
 
	# --- Case 1: A Match ---
	# If the last characters of the current substrings match, they are part of the LCS.
	if m > 0 and n > 0 and S1[m - 1] == S2[n - 1]:
		# This is the simplest case. The path in our "maze" came from the diagonal.
		# We recursively call `diff` for the smaller problem before printing.
		diff(S1, S2, m - 1, n - 1, lookup)
		
		# After the recursive call returns, we print the matched character. This
		# post-order printing ensures the final output is in the correct sequence.
		print(" " + S1[m - 1], end='')
 
	# --- Case 2: An Addition in S2 ---
	# This branch is taken if the characters do not match. We must now consult our
	# "maze map" (the lookup table) to see which path was taken.
	#
	# WHY THIS CONDITION WORKS:
	# The logic `lookup[m][n-1] >= lookup[m-1][n]` asks: "Is the value from the LEFT
	# cell greater than or equal to the value from the AROVE cell?"
	# - If TRUE: The optimal path came from the LEFT. This means the algorithm chose to
	#   "ignore" the character from S2 (`S2[n-1]`) to achieve the best LCS score.
	# - CONCLUSION: As per our recipe analogy, ignoring a character from the "new recipe" (S2)
	#   means it's an ADDITION needed to transform S1 into S2.
	elif n > 0 and (m == 0 or lookup[m][n - 1] >= lookup[m - 1][n]):
 
		# Follow the path to the LEFT in the table.
		diff(S1, S2, m, n - 1, lookup)
		# After returning, print the current character from S2 as an addition.
		print(" +" + S2[n - 1], end='')
 
	# --- Case 3: A Removal from S1 ---
	# This is the only other possibility if the characters don't match.
	#
	# WHY THIS CONDITION WORKS:
	# This condition is met only if `lookup[m-1][n]` was strictly greater than
	# `lookup[m][n-1]`.
	# - If TRUE: The optimal path must have come from ABOVE. This means the algorithm chose to
	#   "ignore" the character from S1 (`S1[m-1]`).
	# - CONCLUSION: Ignoring a character from the "old recipe" (S1) means it was
	#   REMOVED to create S2.
	elif m > 0 and (n == 0 or lookup[m][n - 1] < lookup[m - 1][n]):
 
		# Follow the path UPWARDS in the table.
		diff(S1, S2, m - 1, n, lookup)
		# After returning, print the current character from S1 as a removal.
		print(" -" + S1[m - 1], end='')
 
 
 
# Function to fill the `lookup` table. This is the "map building" phase.
def LCSLength(S1, S2, m, n, lookup):
 
	# Base case: The LCS of any string with an empty string is 0.
	# This initializes the first column and row of the table to all 0s.
	for i in range(m + 1):
		lookup[i][0] = 0
	for j in range(n + 1):
		lookup[0][j] = 0
 
	# Fill the rest of the lookup table cell by cell.
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			# RULE 1: If characters match.
			if S1[i - 1] == S2[j - 1]:
				# The LCS is one character longer than the LCS of the strings without
				# these matching characters. We get this value from the diagonal cell.
				lookup[i][j] = lookup[i - 1][j - 1] + 1
			# RULE 2: If characters do not match.
			else:
				# The LCS is the best we can do by either ignoring S1's character
				# (taking value from ABOVE) or ignoring S2's character (taking
				# value from the LEFT). We take the maximum of these two options.
				lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
# --- Main driver code ---
 
S1 = "ARY"
S2 = "Aryan"
 
# This is a nested list comprehension. It creates a 2D list (a list of lists)
# representing our grid, initialized with zeros.
# The "for loop" equivalent would be:
#   lookup = []
#   for y in range(len(S1) + 1):
#       new_row = [0] * (len(S2) + 1)
#       lookup.append(new_row)
lookup = [[0 for x in range(len(S2) + 1)] for y in range(len(S1) + 1)]
 
# STEP 1: Build the map. Call the function to fill the lookup table with LCS lengths.
LCSLength(S1, S2, len(S1), len(S2), lookup)
 
'''
------------------------------------------------------------------------------------
THE COMPLETED `lookup` TABLE (THE MAP)

This is the table generated by the `LCSLength` function. The `diff` function
uses this data to find the path of differences.

Rows correspond to S1 ("ABCDFGHJQZ"). Columns correspond to S2 ("ABCDEFGIJKRXYZ").

      "" A B C D E F G I J  K  R  X  Y  Z
""    [0, 0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0]
A     [0, 1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1]
B     [0, 1,2,2,2,2,2,2,2,2, 2, 2, 2, 2, 2]
C     [0, 1,2,3,3,3,3,3,3,3, 3, 3, 3, 3, 3]
D     [0, 1,2,3,4,4,4,4,4,4, 4, 4, 4, 4, 4]
F     [0, 1,2,3,4,4,5,5,5,5, 5, 5, 5, 5, 5]
G     [0, 1,2,3,4,4,5,6,6,6, 6, 6, 6, 6, 6]
H     [0, 1,2,3,4,4,5,6,6,6, 6, 6, 6, 6, 6]
J     [0, 1,2,3,4,4,5,6,6,7, 7, 7, 7, 7, 7]
Q     [0, 1,2,3,4,4,5,6,6,7, 7, 7, 7, 7, 7]
Z     [0, 1,2,3,4,4,5,6,6,7, 7, 7, 7, 7, 8]
------------------------------------------------------------------------------------
'''

# STEP 2: Follow the map. Call `diff` to backtrack through the table and print.
diff(S1, S2, len(S1), len(S2), lookup)

# --- EXPECTED OUTPUT ---
# Based on the logic and the tie-breaking rule (`>=`), the output will be:
#  A B C -D +E F G -H +I J -Q +K +R +X +Y Z