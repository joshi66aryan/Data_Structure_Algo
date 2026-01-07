# Stock Buy and Sell – Max 2 Transactions Allowed

# In the stock market, a person buys a stock and sells it on some future date. 
# Given the stock prices of n days in an array prices[ ]. Find out the maximum 
# profit a person can make in at most 2 transactions. A transaction is equivalent 
# to (buying + selling) of a stock and a new transaction can start only when the 
# previous transaction has been completed.

# Examples: 

# Input:   prices[] = [10, 22, 5, 75, 65, 80]
# Output:  87
# Explanation: Buy at 10, sell at 22, profit = 22 - 10 = 12 
#             Buy at 5 and sell at 80, total profit = 12 + (80 - 5) = 87

# Input:   prices[] = [100, 30, 15, 10, 8, 25, 80]
# Output:  72
# Explanation: Only one transaction needed here. Buy at price 8 and sell at 80.

# Input:   prices[] = [90, 80, 70, 60, 50]
# Output:  0
# Explanation: Not possible to earn.

def maxProfit(prices):
    # If the list is too small, no profit is possible
    if not prices or len(prices) < 2:
        return 0

    # ------------------------------------------------------------------
    # We maintain FOUR variables using DP (Kadane-like optimization):
    #
    # buy1  -> Best (lowest) price for the 1st buy
    # sell1 -> Best profit after the 1st sell
    #
    # buy2  -> Best effective price for the 2nd buy 
    #          (price - profit from first sell)
    #
    # sell2 -> Best total profit after the 2nd sell
    # ------------------------------------------------------------------
    
    buy1 = float('inf')
    sell1 = 0
    buy2 = float('inf')
    sell2 = 0

    # ---------------------------------------------------------------
    # Example used in explanation:
    # prices = [10, 22, 5, 75, 65, 80]
    # ---------------------------------------------------------------

    for price in prices:

        # ---------------------------------------------------------------
        # 1) FIRST BUY: we want the minimum price so far
        # ---------------------------------------------------------------
        buy1 = min(buy1, price)

        # ---------------------------------------------------------------
        # 2) FIRST SELL: maximize profit => price - buy1
        # ---------------------------------------------------------------
        sell1 = max(sell1, price - buy1)

        # ---------------------------------------------------------------
        # 3) SECOND BUY: effective cost = price - profit from sell1
        #    Why? Because sell1 profit reduces the real cost of buying again
        # ---------------------------------------------------------------
        buy2 = min(buy2, price - sell1)

        # ---------------------------------------------------------------
        # 4) SECOND SELL: maximize profit => price - buy2
        # ---------------------------------------------------------------
        sell2 = max(sell2, price - buy2)

        # ---------------------------------------------------------------
        # COMMENT THE ITERATIONS FOR THE EXAMPLE 
        # ---------------------------------------------------------------
        # Example: prices = [10, 22, 5, 75, 65, 80]
        #
        # Iteration 1: price = 10
        #   buy1  = min(inf,10) = 10
        #   sell1 = max(0, 10-10=0) = 0
        #   buy2  = min(inf, 10-0=10) = 10
        #   sell2 = max(0, 10-10=0) = 0
        #
        # Iteration 2: price = 22
        #   buy1  = min(10,22) = 10
        #   sell1 = max(0, 22-10=12) = 12      # first profit found
        #   buy2  = min(10, 22-12=10) = 10     # same as before
        #   sell2 = max(0, 22-10=12) = 12
        #
        # Iteration 3: price = 5
        #   buy1  = min(10,5) = 5              # cheaper 1st buy
        #   sell1 = max(12, 5-5=0) = 12
        #   buy2  = min(10, 5-12=-7) = -7       # negative means "very good" 2nd buy
        #   sell2 = max(12, 5-(-7)=12) = 12
        #
        # Iteration 4: price = 75
        #   buy1  = min(5,75)=5
        #   sell1 = max(12, 75-5=70) = 70       # huge first profit
        #   buy2  = min(-7, 75-70=5) = -7       # still best
        #   sell2 = max(12, 75-(-7)=82) = 82    # 2nd sell profit
        #
        # Iteration 5: price = 65
        #   buy1  = min(5,65)=5
        #   sell1 = max(70, 65-5=60) = 70
        #   buy2  = min(-7, 65-70=-5) = -7
        #   sell2 = max(82, 65-(-7)=72) = 82
        #
        # Iteration 6: price = 80
        #   buy1  = min(5,80)=5
        #   sell1 = max(70, 80-5=75) = 75
        #   buy2  = min(-7, 80-75=5) = -7
        #   sell2 = max(82, 80-(-7)=87) = 87    # FINAL ANSWER
        # ---------------------------------------------------------------

    # Final maximum profit after at most 2 transactions
    return sell2


if __name__ == '__main__':
    arr = [10, 22, 5, 75, 65, 80]
    ans = maxProfit(arr)
    print("The answer is:",ans)