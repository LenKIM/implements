from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(list(word)))
            anagram_dict[sorted_word].append(word)

        return [v for k, v in anagram_dict.items()]
