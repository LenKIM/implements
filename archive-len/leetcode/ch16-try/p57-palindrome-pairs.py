import collections
from typing import List

# ![](https://tva1.sinaimg.cn/large/008eGmZEgy1goq6bevwdfj30re0zedkn.jpg)

class TrieNode:
    def __init__(self):
        # 트리 만들기 위한
        self.children = collections.defaultdict(TrieNode)
        # 각 트리의 위치 기억
        self.word_id = -1
        # 자신이 펠린드론일 경우
        self.iamPalindrome_word_ids = []


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(abc):
        return abc[::] == abc[::-1]

    def insert(self, idx, word: str) -> None:
        node = self.root

        # 단어의 어절을 하나씩 돌면서 node 의 children 을 확인합니다.
        # 만약 있다면 타고 들어가고, 없으면 TrieNode 을 새롭게 만들기
        # 왜 Reversed 를 해야할까?
        # 각 트라이의 끝지점을 기억해야 한다.
        for i, char in enumerate(reversed(word)):

            # 만약 word 자체가 펠린드론일 경우, 해당되는 경우 root Node 에
            # word_idx 가 담기고 그렇지 않으면 각 Node[word-1] 에 word_idx 가 생겼을 것
            if self.is_palindrome(word[0: len(word) - i]):
                node.iamPalindrome_word_ids.append(idx)

            node = node.children[char]

        node.word_id = idx

    #
    def search(self, idx, word: str) -> List:
        node = self.root
        results = []

        while word:
            if node.word_id >= 0:
                # 세번째 판별 로직 ( 탐색 중, word_id 가 있는 Node 를 만나고, 나머지 word가 펠린드론 일 경우 )
                # (dcbc + d)
                if self.is_palindrome(word):
                    results.append([idx, node.word_id])

            if not word[0] in node.children:
                return results

            node = node.children[word[0]]

            word = word[1:]

        # 첫번째 ( reversed 된 단어와 다른 단어가 동일할 경우 )
        if node.word_id >= 0 and node.word_id != idx:
            results.append([idx, node.word_id])

        # 두번째 (끝까지 탐색한 뒤에 그곳에 palindrome_workd_ids 가 있을 경우)
        for word_id in node.iamPalindrome_word_ids:
            results.append([idx, word_id])

        return results


class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 트라이 생성
        trie = Trie()

        # idx, word 트라이 만들었음.
        for idx, word in enumerate(words):
            trie.insert(idx, word)

        result = []
        for idx, word in enumerate(words):
            result.extend(trie.search(idx, word))

        return result


solution = Solution()
pairs = solution.palindromePairs(["d", "cbbc dcddcd ", "dcbb", "dcbc", "cbbc", "bbcd"])
print(pairs)