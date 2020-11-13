# 가장 흔한 문자
# https://leetcode.com/problems/most-common-word/
import re
from collections import Counter
from typing import List


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
  x = re.sub(r'[^\w]', ' ', paragraph)
  res = []
  for p in x.lower().split():
    if p not in banned:
      res.append(p)
  c = Counter(res)
  return c.most_common(1)[0][0]


if __name__ == '__main__':
  word = mostCommonWord(
    "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])

  print(word)
