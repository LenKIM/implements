#!/bin/python3

# 3P2 > nPr
# 1. DFS 이용
# 2 체크리스트 이용
# 3 외우자

def DFS(L):
    # 종료 조건
    if L == r:
        print(result)

    else:
        for i in range(len(n)):
            if checklist[i] == 0:
                result[L] = n[i]
                checklist[i] = 1
                DFS(L + 1)
                checklist[i] = 0


if __name__ == '__main__':
    n = [1, 2, 3]
    r = 2

    result = [0] * r  # [0,0]
    checklist = [0] * len(n)
    DFS(0)
