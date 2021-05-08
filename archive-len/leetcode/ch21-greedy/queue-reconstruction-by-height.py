from typing import List

"""
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

[내림차순 | 오름차순] 
0. [7,0] | [7,1], [6,1], [5,0], [5,2], [4,4]

1. [7,0], [6,1] | [7,1], [5,0], [5,2], [4,4]

2. [5,0], [7,0], [6,1] | [7,1], [5,2], [4,4]

3. [5,0], [7,0], [5,2], [6,1] | [7,1], [4,4]

4. [5,0], [7,0], [5,2], [6,1], [4,4] | [7,1]

[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

[7,0],[7,1],[6,1],[5,0] ...

[7,0],[6,1],[7,1],[5,0] ...

[5,0],[7,0],[6,1],[7,1] ...


1. 키가 큰순으로 정렬한다. | 두번째 수는 나보다 키가 크거나 같아야 한다.
2. 최적의 값을 찾는 것이 정답이다.
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sortedPeople = sorted(people, key=lambda a: (-a[0], a[1]))

        # 첫번째 값은 큰키는 앞에 오고 싶어하고,
        # 두번째 값은 작은 수가 앞에 와야 한다.
        # print(sortedPeople)
        result = []
        for idx, val in enumerate(sortedPeople):
            height = val[0]
            tallerNumber = val[1]  # 자신보다 키가 크거나 같은 경우의 횟수
            result.insert(tallerNumber, [height, tallerNumber])

        return result


Solution().reconstructQueue([[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])
