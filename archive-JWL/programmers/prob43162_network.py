def dfs(idx, computers, visited):
    visited[idx] = True
    for i, num in enumerate(computers[idx]):
        if num == 1 and visited[i] == False:
            dfs(i, computers, visited)


def solution(n, computers):
    answer = 0
    visited = []
    for i in range(n):
        visited.append(False)
    for i in range(n):
        if visited[i] == False:
            answer += 1
            print(visited)
            dfs(i, computers, visited)
    return answer