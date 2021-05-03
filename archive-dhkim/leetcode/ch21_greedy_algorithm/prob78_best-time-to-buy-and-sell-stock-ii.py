from typing import List

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
"""


class Solution:
    """
    runtime : 64 ms
    memory : 15.1 MB
    """
    def maxProfit(self, prices: List[int]) -> int:

        before = prices[0]
        profits = [0]

        for idx, price in enumerate(prices):

            if idx == 0:
                continue

            if before < price:
                profits.append(price - before)
            before = price

        return sum(profits)
