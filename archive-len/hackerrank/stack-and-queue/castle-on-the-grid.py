# https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

# !/bin/python3


# 10
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
# 9 1 9 6
# Complete the minimumMoves function below.
import collections


def minimumMoves(grid, startX, startY, goalX, goalY):
    if (startX, startY) == (goalX, goalY):
        return 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 왼쪽, 위, 오른쪽, 아래
    # directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    height_len = len(grid)
    wight_len = len(grid[0])

    queue = collections.deque()
    start_point = (startX, startY)
    distances = [[-1] * len(grid) for _ in range(len(grid))]
    distances[startX][startY] = 0
    queue.append(start_point)

    def getTotalDirectionPoints(grid, point, distances):
        point_list = []

        for direction in directions:

            temp_x = point[0] + direction[0]
            temp_y = point[1] + direction[1]

            while height_len > temp_x >= 0 \
                    and wight_len > temp_y >= 0 and \
                    grid[temp_x][temp_y] != 'X' and \
                    distances[temp_x][temp_y] == -1:

                point_val_tuple = (temp_x, temp_y)
                point_list.append(point_val_tuple)
                temp_x = temp_x + direction[0]
                temp_y = temp_y + direction[1]

        return point_list

    while queue:
        cur_point = queue.pop()

        distance = distances[cur_point[0]][cur_point[1]]
        points = getTotalDirectionPoints(grid, cur_point, distances)

        for point in points:
            if (point[0], point[1]) == (goalX, goalY):
                return distance + 1
            distances[point[0]][point[1]] = distance + 1
            queue.appendleft(point)
        # if points is not None:
        #     return points
    return -1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
