
# Zero One Knapsack in Python

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# top - down approach
def zoKnapsack(items, capacity, currentIndex, tempDict):

    dictKey = str(currentIndex)+str(capacity)
    if capacity <=0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    
    elif dictKey in tempDict:
        return tempDict[dictKey]
    
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1, tempDict)
        profit2 = zoKnapsack(items, capacity, currentIndex+1, tempDict)
        tempDict[dictKey] = max(profit1, profit2)
        return tempDict[dictKey]
    else:
        return 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zoKnapsack(items, 7, 0, {}))

# bottom - up approach

def zoKnapsackBU(profits, weights, capacity):
    if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return 0
    numberOfRows = len(profits) + 1
    dp = [[None for i in range(capacity+2)] for j in range(numberOfRows)]
    for i in range(numberOfRows):
        dp[i][0] = 0
    for i in range(capacity+1):
        dp[numberOfRows-1][i] = 0
    for row in range(numberOfRows-2, -1, -1):
        for column in range(1,capacity+1):
            profit1 = 0
            profit2 = 0
            if weights[row] <= column:
                profit1 = profits[row] + dp[row + 1][column - weights[row]]
            profit2 = dp[row + 1][column]
            dp[row][column] = max(profit1, profit2)
    return dp[0][capacity]