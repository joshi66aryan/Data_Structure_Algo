# Factorials of large numbers
# Difficulty: Medium 
# Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

# Examples:

# Input: n = 5
# Output: [1, 2, 0]
# Explanation: 5! = 1*2*3*4*5 = 120

# Input: n = 10
# Output: [3, 6, 2, 8, 8, 0, 0]
# Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800

# Input: n = 1
# Output: [1]
# Explanation: 1! = 1 

# Constraints:
# 1 ≤ n ≤ 103


def factorial_digits(n):
    """
    Computes n! and returns the digits as a list.
    
    Time Complexity:  O(n * d)  
        d = number of digits in n!
    Space Complexity: O(d)
    """

    # Start with 1 because 0! = 1! = 1
    digits = [1]   
    # Example (n = 5): digits starts as [1]

    for num in range(2, n + 1):
        # Example loop order (n = 5): num = 2, 3, 4, 5
        carry = 0

        # Multiply each digit by num
        for i in range(len(digits)):
            prod = digits[i] * num + carry

            # Example for n = 5:
            # Step num=2: digits = [1] → 1*2 = 2 → digits = [2]
            # Step num=3: digits = [2] → 2*3 = 6 → digits = [6]
            # Step num=4: digits = [6] → 6*4 = 24 → store 4, carry 2
            #             (digits becomes [4], carry=2)


            # % → Remainder (Modulo)
            #     Gives the units digit after multiplication
            #     python a % b = remainder when a is divided by b
            #
            #     Example: python
                #     24 % 10 → 4
                #     57 % 10 → 7
                #     10 % 10 → 0


            # // → Integer Division (Floor Division)
                # Gives how many tens to carry over
                # pythona // b = how many times b fits completely into a
                #
                # Example: python
                    # 24 // 10 → 2
                    # 57 // 10 → 5
                    # 10 // 10 → 1
                    # 8  // 10 → 0

            digits[i] = prod % 10       # store the new digit
            carry = prod // 10          # update carry

        # Add leftover carry as new digits
        while carry > 0:
            # Example (num = 4):
            # carry = 2 → append 2 → digits = [4, 2] (which means 24)
            #
            # Example (num = 5):
            # before multiplying: digits = [4, 2]
            # multiply:
            # 4*5 = 20 → store 0, carry 2
            # 2*5 = 10 + 2 = 12 → store 2, carry 1
            # append 1 → digits = [0, 2, 1]   (represents 120)

            digits.append(carry % 10)
            carry //= 10

    # digits are stored in reverse order → reverse back
    # Example: [0, 2, 1] → [1, 2, 0]
    return digits[::-1]



if __name__ == '__main__': 
    x = int(input("Enter a number to get factorial"))
    arr = factorial_digits(x)
    print("number contributed to the factorial",arr)
