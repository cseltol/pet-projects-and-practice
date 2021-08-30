def max_profit(prices):
    min = prices[0]
    for i in range(len(prices)):
        if prices[i] < min:
            min = prices[i]
    max = prices[0]
    for i in range(len(prices)):
        if prices[i] > max:
            max = prices[i]
    return max - min
