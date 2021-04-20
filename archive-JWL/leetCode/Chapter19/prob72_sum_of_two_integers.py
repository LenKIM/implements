class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        print(bin(a), bin(b))
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b)<< 1) & MASK
            print(bin(a), bin(b))

        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a

sol = Solution()
print(sol.getSum(3,5))