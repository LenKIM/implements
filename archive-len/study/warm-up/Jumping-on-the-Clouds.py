#!/bin/python3

# 연속 번호 구름으로 시작하는 새로운 모바일 게임이 있습니다. 구름 중 일부는 뇌우이고 다른 구름은 적운입니다.
# 플레이어는 현재 구름의 수와 같은 숫자를 가진 적운 구름 위에 점프 할 수 있습니다.
# 또는 . 플레이어는 천둥 머리를 피해야합니다.
# 시작 위치에서 마지막 구름으로 점프하는 데 필요한 최소 점프 수를 결정합니다.
# 게임에서이기는 것은 언제나 가능합니다.
# 각 게임에 대해 번호가 매겨진 일련의 구름을 얻습니다.  그들이 안전하거나  피해야하는 경우.

import os


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    result = 0
    start_idx = 0
    for i in range(len(c)):
        if c[i] != 0:
            continue

        start_idx = i
        break

    end_idx = len(c) - 1
    while start_idx != end_idx:
        if start_idx + 2 <= end_idx and c[start_idx + 2] != 1:
            start_idx += 2
            result += 1
        elif start_idx + 1 <= end_idx and c[start_idx + 1] != 1:
            start_idx += 1
            result += 1

    return result



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 6
    # 7
    #
    c = [0, 0, 0, 1, 0, 0]

    result = jumpingOnClouds(c)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
