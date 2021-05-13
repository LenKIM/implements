from typing import List

"""
https://leetcode.com/problems/gas-station/

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start

    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     for start in range(len(gas)):
    #         fuel = 0
    #         for i in range(start, len(gas) + start):
    #             index = i % len(gas)
    #
    #             can_travel = True
    #             if gas[index] + fuel < cost[index]:
    #                 can_travel = False
    #                 break
    #             else:
    #                 fuel += gas[index] - cost[index]
    #         if can_travel:
    #             return start
    #     return -1
