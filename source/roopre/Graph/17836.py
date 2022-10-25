import sys

def dfs(cur, visit, castle, t, count):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    if not (0 <= cur[0] < len(castle)) or not (0 <= cur[1] < len(castle[0])):
        return
    if count >= visit[cur[0]][cur[1]]:
        return
    if count > t:
        return

    visit[cur[0]][cur[1]] = count

    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]

        if 0 <= nx < len(castle) and 0 <= ny < len(castle[0]) and castle[nx][ny] != 1:
            dfs((nx, ny), visit, castle, t, count + 1)


if __name__ == "__main__":
    n, m, t = map(int, input().split())
    castle = [[] for i in range(n)]

    visit = [[n * m for i in range(m)] for j in range(n)]
    for i in range(n):
        castle[i] = list(map(int, sys.stdin.readline().split()))
        for j in range(len(castle[i])):
            if castle[i][j] == 2:
                lx = i
                ly = j

    dfs((0, 0), visit, castle, t, 0)
    # 공주까지 최소 거리 (검 안쓰고)
    toPrincess = visit[n - 1][m - 1]
    # 검까지 최소 거리
    lDistance = visit[lx][ly]
    # 검쓰고 검으로부터 공주 거리 알아내기
    visit = [[n * m for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            castle[i][j] = 0
    dfs((lx, ly), visit, castle, t, 0)

    sword_to_princess = visit[n-1][m-1]

    if lDistance == n*m and toPrincess == n*m:
        print("Fail")
        exit(0)
    if lDistance + sword_to_princess < toPrincess:
        print(lDistance + sword_to_princess)
    else:
        print(toPrincess)