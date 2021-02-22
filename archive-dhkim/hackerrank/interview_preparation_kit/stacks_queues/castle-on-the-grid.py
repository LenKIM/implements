#!/bin/python3

"""
https://www.hackerrank.com/challenges/castle-on-the-grid/problem
"""

import math
import os
import random
import re
import sys


# 매트릭스 탐색 문제를 재귀로 풀지 말 것. (recursion 한계 초과로 오류남)
# 무난하게 큐를 사용하여 BFS로 풀자
# BFS의 경우, 무한루프가 생기지 않도록 중복 방문을 막는 것이 중요한데, 이 문제는 방문한 "방향"을 고려하여 중복 방문을 막아야 함

def minimumMoves(grid, startX, startY, goalX, goalY):
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # piece's x, y, direction, move_cnt
    queue = [(startX, startY, -1, 1)]

    visit_matrix = dict()  # x_y_dir -> move_cnt

    minium_move = -1

    # BFS
    while queue:
        # 큐의 맨 앞 확인
        p_x, p_y, p_direction, p_cnt = queue.pop(0)

        # 목적지 도달한 경우, minium_move 갱신
        if p_x == goalX and p_y == goalY:
            minium_move = p_cnt if minium_move == -1 else min(minium_move, p_cnt)
            continue

        for i in range(4):

            nextX = p_x + direct[i][0]
            nextY = p_y + direct[i][1]
            nextM = p_cnt if p_direction == -1 or p_direction == i else p_cnt + 1
            position = f"{nextX}_{nextY}"
            visit_key = f"{nextX}_{nextY}_{i}"

            if visit_key in visit_matrix and visit_matrix[visit_key] <= nextM:
                continue

            # 현재 move 횟수가 이미 minium_move 갱신값을 넘어섰다면 이후론 탐색할 필요가 없음
            if minium_move != -1 and nextM >= minium_move:
                continue

            # 주위 공간 중 유효한 곳을 큐에 입력
            if 0 <= nextX < len(grid) and 0 <= nextY < len(grid[0]) and grid[nextX][nextY] != 'X':
                queue.append((nextX, nextY, i, nextM))
                visit_matrix[visit_key] = nextM

    return minium_move


# sys.setrecursionlimit(1000)

# # Complete the minimumMoves function below.
# def minimumMoves_recursion(grid, startX, startY, goalX, goalY):
#
#
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#     res = [-1]
#
#     def dfs(x, y, now_direction, move_cnt):
#         # 그리드 범위 넘어설 경우
#         if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
#             return
#
#         # X벽인 경우
#         if grid[x][y] == 'X':
#             return
#
#         # 목적지에 도달한 경우
#         if x == goalX and y == goalY:
#             # 결과 갱신
#             if res[0] == -1:
#                 res[0] = move_cnt
#             else:
#                 res[0] = min(res[0], move_cnt)
#             return
#
#         # 가망이 없어
#         if res[0] != -1 and move_cnt > res[0]:
#             return
#
#         # 경로 탐색 DFS
#         for i in range(4):
#             next_move = move_cnt
#
#             # 시작점이 아닐 경우
#             if now_direction != -1:
#                 # 역주행 금지
#                 if abs(now_direction - i) == 2:
#                     continue
#                 # 방향이 꺾일 때에만 move_cnt + 1
#                 next_move = move_cnt + 1 if i != now_direction else move_cnt
#
#             dfs(x + directions[i][0], y + directions[i][1], i, next_move)
#
#     dfs(startX, startY, -1, 1)
#
#     return res[0]
#


if __name__ == '__main__':

#     input_str = """10
# .X..XX...X
# X.........
# .X.......X
# ..........
# ........X.
# .X...XXX..
# .....X..XX
# .....X.X..
# ..........
# .....X..XX
# 9 1 9 6"""
    input_str = """40
...X......XX.X...........XX....X.XX.....
.X..............X...XX..X...X........X.X
......X....X....X.........X...........X.
.X.X.X..X........X.....X.X...X.....X..X.
....X.X.X...X..........X..........X.....
..X......X....X....X...X....X.X.X....XX.
...X....X.......X..XXX.......X.X.....X..
...X.X.........X.X....X...X.........X...
XXXX..X......X.XX......X.X......XX.X..XX
.X........X....X.X......X..X....XX....X.
...X.X..X.X.....X...X....X..X....X......
....XX.X.....X.XX.X...X.X.....X.X.......
.X.X.X..............X.....XX..X.........
..X...............X......X........XX...X
.X......X...X.XXXX.....XX...........X..X
...X....XX....X...XX.X..X..X..X.....X..X
...X...X.X.....X.....X.....XXXX.........
X.....XX..X.............X.XX.X.XXX......
.....X.X..X..........X.X..X...X.X......X
...X.....X..X.............X......X..X..X
........X.....................X....X.X..
..........X.....XXX...XX.X..............
........X..X..........X.XXXX..X.........
..X..X...X.......XX...X.....X...XXX..X..
.X.......X..............X....X...X....X.
.................X.....X......X.....X...
.......X.X.XX..X.XXX.X.....X..........X.
X..X......X..............X..X.X.......X.
X........X.....X.....X....XX.......XX...
X.....X.................X.....X..X...XXX
XXX..X..X.X.XX..X....X.....XXX..X......X
..........X.....X.....XX................
..X.........X..X.........X...X.....X....
.X.X....X...XX....X...............X.....
.X....X....XX.XX........X..X............
X...X.X................XX......X..X.....
..X.X.......X.X..X.....XX.........X..X..
........................X..X.XX..X......
........X..X.X.....X.....X......X.......
.X..X....X.X......XX....................
34 28 16 8"""

    lines = input_str.split("\n")

    n = int(lines[0])
    grid = lines[1:n+1]

    startX, startY, goalX, goalY = [int(a) for a in lines[-1].split(" ")]

    print(f">> n: {n}")
    print(f">> grid: \n{grid}")
    print(f">> startX: {startX}")
    print(f">> startY: {startY}")
    print(f">> goalX: {goalX}")
    print(f">> goalY: {goalY}")

    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(f">> result: {result}")
