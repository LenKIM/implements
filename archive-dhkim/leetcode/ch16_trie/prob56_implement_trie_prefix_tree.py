"""
https://leetcode.com/problems/implement-trie-prefix-tree
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.dic = dict()

    def __repr__(self):
        return f" {self.val} -> {list(self.dic.values())} "


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.root

        for s in word:
            if s in tmp.dic:
                tmp = tmp.dic[s]  # go next
            else:
                tmp.dic[s] = Node(s)  # insert
                tmp = tmp.dic[s]

        tmp.dic["EOF"] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.root

        for s in word:
            if s in tmp.dic:
                tmp = tmp.dic[s]
            else:
                return False

        if "EOF" in tmp.dic:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.root

        for s in prefix:
            if s in tmp.dic:
                tmp = tmp.dic[s]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
