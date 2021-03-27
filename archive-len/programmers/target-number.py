# https://programmers.co.kr/learn/courses/30/lessons/43165


# def solution(numbers: List, target: int):
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
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)

def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

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