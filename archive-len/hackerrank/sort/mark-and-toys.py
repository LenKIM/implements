#!/bin/python3


# Complete the maximumToys function below.
def maximumToys(prices, k):
    _sum = 0
    cnt = 0

    prices.sort()

    if len(prices) <= 1:
        return len(prices)

    for price in prices:
        if _sum + price < k:
            _sum = _sum + price
            cnt = cnt + 1
    return cnt
