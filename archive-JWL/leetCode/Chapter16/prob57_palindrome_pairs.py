import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_idx=[]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def is_palindrome(self, word: str) ->bool:
        return word[::] == word[::-1]

    def insert(self, index, word)->None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word)-i]):
                node.palindrome_idx.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            if node.word_id >=0:
                if self.is_palindrome(word):
                    result.append([index,node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id>=0 and node.word_id != index:
            result.append([index, node.word_id])
        for palindrome_id in node.palindrome_idx:
            result.append([index,palindrome_id])

        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        result = []
        for i, word in enumerate(words):
            result.extend(trie.search(i,word))

        return result
# def palindromePairs(self, words: List[str]) -> List[List[int]]:
#     result = list()
#     tup_words = list(enumerate(words))
#     tup_list = list( itertools.permutations(tup_words,2))
#
#     for item in tup_list:
#         temp = item[0][1] + item[1][1]
#         if temp == temp[::-1]:
#             res = [item[0][0],item[1][0]]
#             result.append(res)
#     return result
