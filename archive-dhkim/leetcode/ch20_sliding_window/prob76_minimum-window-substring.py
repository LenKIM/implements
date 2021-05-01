from collections import Counter

"""
https://leetcode.com/problems/minimum-window-substring
"""


class Solution:
    """
    O(n) 안에 슬라이딩 윈도우 중에서도 주어진 문자열들을 지정 횟수만큼 가지는 최소 윈도우를 찾는 문제
    투 포인터로 푸는 방향 생각하기
    답안 참조했으니 나중에 다시 풀어보기
    """
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        missing = len(t)

        left_idx = start_idx = end_idx = 0

        for right_idx, v in enumerate(s, 1):

            if need[v] > 0:
                missing -= 1
            need[v] -= 1

            if missing == 0:

                # 윈도우 왼쪽이 불필요한 문자가 아닐때까지 왼쪽을 전진
                while left_idx < right_idx and need[s[left_idx]] < 0:
                    need[s[left_idx]] += 1
                    left_idx += 1

                # 짧은 구간 갱신
                if end_idx == 0 or end_idx - start_idx >= right_idx - left_idx:
                    start_idx = left_idx
                    end_idx = right_idx

                # 왼쪽을 강제 1보 전진
                need[s[left_idx]] += 1
                left_idx += 1
                missing += 1

        return s[start_idx: end_idx]
