'''
0 ~ 9 자물쇠

비밀번호 4개
1. 서로 다른 숫자
2. 곱하거나 더해서 220가 되는 숫자
비밀번호가 되는 모든 후보를 고르시오

순열(permutation)
'''


def DFS(L):

    # 종료조건
    if L == r:
        print(result)
    else:
        for i in range(len(n)):
            if checklist[i] == 0:
                result[L] = n[i]

                checklist[i] = 1
                DFS(L+1)
                checklist[i] = 0


if __name__ == '__main__':
    # 9P4
    # 1324
    # 2413 위치가 연관되어 있을 경우. 수열
    # DFS 와 체크리스트 를 사용한다.

    n = [1,2,3]
    r = 3

    result = [0] * r

    checklist= [0] * len(n)

    DFS(0)




