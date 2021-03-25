def solution(numbers, target):
    answer = 0

    if len(numbers) == 0:
        if target == 0:
            return 1
        else:
            return 0

    for i, num in enumerate(numbers):
        answer += solution(numbers[:i] + numbers[i + 1:], target - num)
        answer += solution(numbers[:i] + numbers[i + 1:], target + num)

    return answer