class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = list()
        tup_words = list(enumerate(words))
        tup_list = list( itertools.permutations(tup_words,2))

        for item in tup_list:
            temp = item[0][1] + item[1][1]
            if temp == temp[::-1]:
                res = [item[0][0],item[1][0]]
                result.append(res)
        return result
