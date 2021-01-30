from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            if i == 0:
                continue

            if prices[i - 1] > prices[i]:
                min_price = min(min_price, prices[i])

            elif prices[i - 1] < prices[i]:
                profit = prices[i] - min_price
                max_profit = max(max_profit, profit)

        return max_profit
