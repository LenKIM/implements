#!/bin/python3


# Complete the largestRectangle function below.
# 직사각형은 가로 * 세로 이다.
# 시작 지점의 높이보다 낮으면 변곡점이 생긴 것이다.
# 이 때 곱을 통해 가장 큰 값을 찾자
def largestRectangle(heights):
    stack = []
    i = 0
    area = 0
    while i < len(heights):
        while stack and heights[i] < heights[stack[-1]]:
            hh = heights[stack.pop()]
            if stack:
                w = i - stack[-1] - 1
            else:
                w = i
            area = max(area, hh * w)
        stack.append(i)
        i += 1
    while stack:
        hh = heights[stack.pop()]
        if stack:
            w = i - stack[-1] - 1
        else:
            w = i
        area = max(area, hh * w)
    return area


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
