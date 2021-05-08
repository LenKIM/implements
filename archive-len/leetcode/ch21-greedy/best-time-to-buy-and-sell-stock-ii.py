from typing import List
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

낮을 때 사서, 높을 때 판다.

1,2,3,4,5

1,3,2,5,4
22 = 4
7 1 5 6 3 4
1 5 6 3 4 0
 
= 7
4 1 1
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        forwarded_price = prices[1:] + [0]
        sum = 0
        for price, front_price in zip(prices, forwarded_price):
            if price - front_price < 0:
                sum += price - front_price

        return abs(sum)


Solution().maxProfit([7,6,4,3,1])



