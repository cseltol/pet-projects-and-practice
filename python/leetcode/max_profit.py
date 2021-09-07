def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


def main():
    a1 = [7, 1, 5, 3, 6, 4]
    assert max_profit(a1) == 7
    print(f'Profit maximum is {max_profit(a1)}')
    a2 = [1, 2, 3, 4, 5]
    assert max_profit(a2) == 4
    print(f'Profit maximum is {max_profit(a2)}')
    a3 = [7, 6, 4, 3, 1]
    assert max_profit(a3) == 0
    print(f'Profit maximum is {max_profit(a3)}')


if __name__ == '__main__':
    main()
