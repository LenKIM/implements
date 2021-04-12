"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cdict = dict()
        max_size = 0

        for idx, c in enumerate(s):
            if c in cdict:
                pre_idx = cdict[c]
                cdict = {s[tmp_idx]: tmp_idx for tmp_idx in range(pre_idx + 1, idx + 1)}
            else:
                cdict[c] = idx

            max_size = max(max_size, len(cdict))

        return max_size

    # 슬라이딩 윈도우 사용, 더 빠르게 개선된 버전
    def lengthOfLongestSubstring_another(self, s: str) -> int:
        # 예외처리
        if not s:
            return 0

        max_window = 1
        for idx, c in enumerate(s):
            while idx + max_window < len(s) and max_window + 1 == len(set(s[idx: idx+max_window+1])):
                print(s[idx: idx+max_window+1])
                max_window += 1

        return max_window


if __name__ == "__main__":
    solution = Solution()
    res = solution.lengthOfLongestSubstring_another("pwwkew")
    print(res)
