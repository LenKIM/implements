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
