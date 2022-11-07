if __name__ == "__main__":
    n, m = map(int, input().split())
    l = [[] for i in range(n)]
    for i in range(n):
        l[i] = list(input())

    q = []
    visit = [[False for i in range(m)] for j in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    q.append((0, 0))
    count = 0
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and l[i][j] == '0':
                q = [(i,j)]
                count+=1
                while len(q) != 0:
                    t = q.pop()
                    for d in range(4):
                        nx = t[0] + dx[d]
                        ny = t[1] + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and l[nx][ny] == '0':
                            q.append((nx,ny))
                            visit[nx][ny] = True
    print(count)



