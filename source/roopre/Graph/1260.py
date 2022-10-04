if __name__ == "__main__":
    n, m, v = map(int, input().split(' '))

    connect = [[False for i in range(n + 1)] for j in range(n + 1)]

    dfs_visit = [False for i in range(n + 1)]
    bfs_visit = [False for i in range(n + 1)]

    for _ in range(m):
        t1, t2 = map(int, input().split(' '))
        connect[t1][t2] = True
        connect[t2][t1] = True

    # dfs 시작 -> 큐
    dfs = [v]
    dfs_visit[v] = True
    dfs_result = [v]
    while len(dfs) != 0:
        s = dfs.pop()
        for i in reversed(range(1, n + 1)):
            if connect[i][s] and not dfs_visit[i]:
                dfs.append(i)
                dfs_visit[i] = True
                dfs_result.append(i)

    bfs = [v]
    bfs_visit[v] = True
    bfs_result = [v]
    while len(bfs) != 0:
        s = bfs.pop(0)
        for i in range(1, n + 1):
            if connect[i][s] and not bfs_visit[i]:
                bfs.append(i)
                bfs_visit[i] = True
                bfs_result.append(i)
    print(dfs_result)
    print(bfs_result)

