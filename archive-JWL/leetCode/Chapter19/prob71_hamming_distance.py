class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res, temp = 0, x^y
        while temp>0:
            if temp & 1 == 1:
                res+=1
            temp = temp>>1
        return res