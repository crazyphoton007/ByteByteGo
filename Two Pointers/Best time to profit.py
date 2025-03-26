# O(n)


def maxProfit(prices):
    left = 0
    right = 1
    maxP = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)

        else:
            left = right

        right += 1
    return maxP


if __name__ == '__main__':
    prices = [8, 2, 32, 12, 70, 12, 50]
    result = maxProfit(prices)
    print(result)






