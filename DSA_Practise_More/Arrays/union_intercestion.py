# You are given two arrays a[] and b[], return the Union of both the arrays in any order.

# The Union of two arrays is a collection of all distinct elements present in either of the arrays. 
# If an element appears more than once in one or both arrays, it should be included only once in the result.

# Note: Elements of a[] and b[] are not necessarily distinct.
# Note that, You can return the Union in any order but the driver code will print the result in sorted order only.

# Examples:

# Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
# Output: [1, 2, 3]
# Explanation: Union set of both the arrays will be 1, 2 and 3.

# Input: a[] = [1, 2, 3], b[] = [4, 5, 6] 
# Output: [1, 2, 3, 4, 5, 6]
# Explanation: Union set of both the arrays will be 1, 2, 3, 4, 5 and 6.

# Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
# Output: [1, 2]
# Explanation: Union set of both the arrays will be 1 and 2.

# Constraints:
# 1 ≤ a.size(), b.size() ≤ 10**6
# 0 ≤ a[i], b[i] ≤ 10**5


def union_intersection(arrA, arrB):
    
    # --- Constraint Checks ---
    if not (1 <= len(arrA) <= 10**6):
        raise ValueError("Array 'a' size out of allowed range (1 ≤ len(a) ≤ 10^6)")
    if not (1 <= len(arrB) <= 10**6):
        raise ValueError("Array 'b' size out of allowed range (1 ≤ len(b) ≤ 10^6)")

    # Check element range
    if any((x < 0 or x > 10**5) for x in arrA):
        raise ValueError("Elements of array 'a' must be between 0 and 10^5")
    if any((x < 0 or x > 10**5) for x in arrB):
        raise ValueError("Elements of array 'b' must be between 0 and 10^5")
    
    a = set(arrA)                    # O(n) time, O(n) space   [n = len(arrA)]
    b = set(arrB)                    # O(m) time, O(m) space   [m = len(arrB)]
    
    union_lst = list(a | b)          # O(n + m) time, O(n + m) space
                                     # | operator on sets is O(len(a) + len(b))
    
    inter_lst = list(a & b)          # O(min(n, m)) time, O(min(n, m)) space
                                     # & operator is O(size of smaller set)
    
    return union_lst, inter_lst      # O(1)

if __name__ == '__main__':
    arrA = [1, 2, 3]
    arrB = [3, 4, 5, 6] 
    u,n = union_intersection(arrA, arrB)


    print("union: \t", u, "intersection: \t", n)






# Python `set` – Complete Master Notes  
 


# ### 1. What is a `set` really?

# ```python
# s = {"apple", "banana", "orange"}
# ```

# This is **NOT** a list or array.  
# It is a **hash table** disguised as a collection.

# **Truth**:  
# A Python `set` = a `dict` where **values are thrown away**  
# ```python
# # Under the hood:
# {
#     "apple":  None,
#     "banana": None,
#     "orange": None
# }
# ```

# ---

# ### 2. Core Features (Memorize This Table)

# | Feature              | Value / Behavior                              |
# |----------------------|-----------------------------------------------|
# | Mutable?             | Yes (`set`) / No (`frozenset`)                |
# | Ordered?             | Yes → insertion order preserved (Python 3.7+) |
# | Duplicates           | Automatically removed                         |
# | Indexing             | Not allowed → `s[0]` → TypeError              |
# | Lookup speed         | O(1) average (blazing fast)                   |
# | Memory               | Higher than list (pre-allocates buckets)      |

# ---

# ### 3. How It Works – Step by Step (The Real Mechanism)

# ```
# You do:  s = {"cat", "dog"}

# 1. hash("cat")  →  8934242
# 2. 8934242 % table_size → say table_size=8 → remainder = 2
#    → store "cat" in bucket #2

# 3. hash("dog") → 12345678 % 8 = 6
#    → store "dog" in bucket #6

# 4. Now: "dog" in s ?
#    → hash("dog") → bucket 6 → found instantly!
# ```

# **This is why `in` is 300x faster than list!**

# ---

# ### 4. Table Size = Number of Buckets (Drawers)

# ```python
# empty_set = set()
# # Internally starts with 8 buckets (drawers)
# ```

# **Visual:**
# ```
# +---+---+---+---+---+---+---+---+
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |   ← table_size = 8
# +---+---+---+---+---+---+---+---+
#                 ↑           ↑
#               "cat"       "dog"
# ```

# - Starts at 8  
# - Grows to 32, 128, 512... when ~66% full  
# - Uses **open addressing** + **Robin Hood hashing** (Python 3.6+)

# ---

# ### 5. The Two Magic Methods (MOST IMPORTANT)

# ```python
# __hash__()   → returns int → "Which bucket?"
# __eq__()     → returns bool → "Are you the same object?"
# ```

# **Why both?** Because of **collisions**!

# ```python
# hash("apple")  % 8 → 5
# hash("banana") % 8 → 5    ← SAME bucket!
# ```

# Now bucket 5 has two items.

# When you check `"apple" in s`:
# 1. Go to bucket 5
# 2. Compare with `__eq__` → finds the right one

# **Without `__eq__` → wrong results!**

# ---

# ### 6. What Can Go Inside a Set?

# | Allowed? | Type              | Reason |
# |---------|-------------------|--------|
# | Yes     | `int`, `str`, `tuple`, `frozenset` | Immutable + hashable |
# | No      | `list`, `dict`, `set`              | Mutable → unhashable |
# | Yes     | Custom objects    | If you define `__hash__` + `__eq__` |

# **Example: Custom class in set**
# ```python
# class User:
#     def __init__(self, id):
#         self.id = id
#     def __hash__(self):
#         return hash(self.id)
#     def __eq__(self, other):
#         return self.id == other.id

# u1 = User(42)
# u2 = User(42)
# s = {u1}
# print(u2 in s)  # → True!
# ```

# ---

# ### 7. Performance Comparison (Real Numbers)

# ```python
# # 1 million items
# data = list(range(1_000_000))
# s = set(data)

# Operation           | List       | Set
# ------------------- |----------- |--------
# 999999 in x         | 15,000 μs  | 0.05 μs   ← **300,000x faster!**
# add item            | O(1)       | O(1)
# remove item         | O(n)       | O(1)
# ```

# **Rule**: Use `set` when you do **>100 membership tests**

# ---

# ### 8. Most Useful Set Operations

# ```python
# a = {1,2,3,4}
# b = {3,4,5,6}

# a | b   → {1,2,3,4,5,6}     union
# a & b   → {3,4}             intersection
# a - b   → {1,2}             difference
# a ^ b   → {1,2,5,6}         symmetric difference

# a.issubset(b)        → False
# a <= b               → False (subset or equal)
# a < b                → proper subset
# ```

# ---

# ### 9. Pro One-Liners

# ```python
# # 1. Remove duplicates (keep order) – Python 3.7+
# unique = list(dict.fromkeys(my_list))

# # 2. Remove duplicates (fastest)
# unique = list(set(my_list))

# # 3. Find common items in 3 lists
# common = set(l1) & set(l2) & set(l3)

# # 4. Items in a but not b
# only_a = set(a) - set(b)
# ```

# ---

# ### 10. Common Interview Questions & Answers

# **Q:** Why is `set` faster than `list` for `in`?  
# **A:** Hash table → O(1) vs O(n) linear scan

# **Q:** Can you store a list in a set?  
# **A:** No → lists are mutable → unhashable

# **Q:** How to make your class work in a set?  
# **A:** Implement `__hash__()` and `__eq__()` using immutable fields

# **Q:** Is set order guaranteed?  
# **A:** Yes, insertion order preserved since Python 3.7 (official since 3.8)

# **Q:** What's the initial table size?  
# **A:** 8 buckets (even for empty set)

# ---

# ### Final Drawing to Remember Forever

# ```
# TABLE SIZE = 8
# ┌───┬───┬───┬───┬───┬───┬───┬───┐
# │   │   │   │   │   │ A │   │ B │
# └───┴───┴───┴───┴───┴───┴───┴───┘
#     0   1   2   3   4   5   6   7

# "apple"  → hash → bucket 5
# "banana" → hash → bucket 5 → collision!
# → __eq__() decides which one matches
# ```

# ---

# ### Golden Rule (Tattoo this)

# > **"Have I seen this before?" → Use a `set`**

# ---

# **You now know `set` better than 98% of Python developers.**  
# Print this → stick on wall → thank me later

# *Saved as `python_set_master_notes.pdf` in your brain forever.*