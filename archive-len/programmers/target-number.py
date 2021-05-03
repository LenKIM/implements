# https://programmers.co.kr/learn/courses/30/lessons/43165

import itertools
from typing import List


# def solution(numbers: List, target:int):
#     answer = 0
#
#     i = sum(numbers)
#     if i == target:
#         return 1
#
#     def oper(numbers, target, idx=0):
#         if idx < len(numbers):
#             numbers[idx] *= 1
#             oper(numbers, target, idx+1)
#
#             numbers[idx] *= -1
#             oper(numbers, target, idx+1)
#         elif sum(numbers) == target:
#             nonlocal answer
#             answer += 1
#     oper(numbers,target)
#     return answer



#     ganswer = 0
#
#     def dfs(num, tar, idx):
#         if len(num) > idx:
#             numbers[idx] *= 1
#             dfs(num, tar, idx+1)
#
#             numbers[idx] *= -1
#             dfs(num, tar, idx+1)
#         else:
#             if sum(num) == tar:
#                 nonlocal answer
#                 answer = answer + 1
#
#
#     dfs(numbers, target, 0)
#     return answer


#https://docs.python.org/ko/3/library/itertools.html


# def solution(numbers: List, target: int):
#     l = [(x, -x) for x in numbers] # 튜폴로 (1,-1) (2,-2) ...
#     product = itertools.product(*l, repeat=1)
#     print(list(product))
#     # product1 = itertools.product('ABCD', repeat=4)
#     # print(list(product1))
#     s = list(map(sum, product))
#     return s.count(target)

# def solution(numbers, target):
#     if not numbers and target == 0:
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         numbers_ = target - numbers[0]
#         target_numbers_ = target + numbers[0]
#
#         return solution(numbers[1:], numbers_) \
#                + solution(numbers[1:], target_numbers_)

def solution2(numbers, target):
    answer = 0

    def dfs(idx, acc):

        if idx == len(numbers):
            if acc == target:
                return 1
            else:
                return 0

        pos = dfs(idx + 1, acc + numbers[idx])
        nag = dfs(idx + 1, acc - numbers[idx])
        return pos + nag

    answer = dfs(0, 0)

    return answer

i = solution2([1, 2, 3], 3)
print(i)