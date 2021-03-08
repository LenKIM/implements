#!/bin/python3

def largestRectangle(h):
    stack = []
    idx = 0
    area = 0
    while idx < len(h):
        while stack and h[idx] < h[stack[-1]]:

            height = h[stack.pop()]
            if stack:
                w = idx - stack[-1] - 1
            else:
                w = idx
            area = max(area, height * w)

    while stack:
        height = h[stack.pop()]
        if stack:
            w = idx - stack[-1] - 1
        else:
            w = idx
        area = max(area, height * w)

    return area


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 5

    h = list(map(int, (1, 2, 3, 4, 5)))

    result = largestRectangle(h)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
