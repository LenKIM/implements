from typing import List

"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/
"""


class Solution:
    # 나이브한 풀이법 : O(n^3) 시간복잡도 - deprecated
    def findLength_naive(self, A: List[int], B: List[int]) -> int:
        B_c2idx = dict()
        for idx, b in enumerate(B):
            if b in B_c2idx:
                B_c2idx[b].append(idx)
            else:
                B_c2idx[b] = [idx]

        res_list = []

        for idx_a, char_a in enumerate(A):
            if char_a in B_c2idx:
                for idx_b in B_c2idx[char_a]:
                    tmp_a, tmp_b = idx_a, idx_b

                    while tmp_a + 1 < len(A) and tmp_b + 1 < len(B) and A[tmp_a + 1] == B[tmp_b + 1]:
                        tmp_a += 1
                        tmp_b += 1

                    print(A[idx_a: tmp_a + 1])

                    res_list = max(res_list, A[idx_a: tmp_a + 1], key=len)

        return len(res_list)

    # 2차원 매트릭스를 이용하여 O(n^2)으로 푸는 방법
    def findLength(self, A: List[int], B: List[int]):

        matrix = [[0 for _ in range(len(B))] for _ in range(len(A))]

        max_seq = 0

        for idx_a, a in enumerate(A):
            for idx_b, b in enumerate(B):
                if a == b:
                    seq_num = matrix[idx_a - 1][idx_b - 1] + 1 if idx_a > 0 and idx_b > 0 else 1
                    matrix[idx_a][idx_b] = seq_num
                    max_seq = max(max_seq, seq_num)

        return max_seq


"""
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
"""
