def CoinChange(totalNum, coins):
    N = totalNum
    coins.sort()
    index = len(coins) - 1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N -= coinValue
        if N < coinValue:
            index -= 1
        if N == 0:
            break

CoinChange(201, [1, 2, 5, 20, 50, 100])
  