import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        map = {}
        result = 0
        for char in stones:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

        for char in jewels:
            if char in map:
                result += map[char]

        return result

    # defaultdict를 이용한 비교 생
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:

        map = collections.defaultdict(int)
        result = 0
        for char in stones:
            map[char] += 1

        for char in jewels:
            result += map[char]

        return result

    def numJewelsInStones3(self, jewels: str, stones: str) -> int:

        map = collections.Counter(stones)
        result = 0

        for char in jewels:
            result += map[char]

        return result

    def numJewelsInStones4(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
