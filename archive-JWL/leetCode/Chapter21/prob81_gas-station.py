from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        fuel = 0

        for i in range(0,len(gas)):
            if gas[i] - cost[i] +  fuel >= 0:
                fuel += gas[i] - cost[i]
            else:
                start  = i + 1
                fuel = 0

        return start

sol = Solution()
gas = [3, 1, 1]
cost = [1, 2, 2]
sol.canCompleteCircuit(gas,cost)