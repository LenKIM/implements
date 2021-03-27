def dfs(numbers, target, sum_items, idx):
    answer = 0

    if len(numbers) <= idx:
        if target == sum_items:
            return 1
        else:
            return 0

    answer += dfs(numbers, target, sum_items + numbers[idx], idx + 1)
    answer += dfs(numbers, target, sum_items - numbers[idx], idx + 1)

    return answer


def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)

    return answer