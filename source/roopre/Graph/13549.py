def search(count, cur, k, visit):
    print(cur)
    if cur > 100000:
        return
    if visit[cur] < count:
        return
    else:
        visit[cur] = count
        if cur == k:
            return
        if cur - 1 >= 0:
            search(count + 1, cur - 1, k, visit)
        if cur != 0:
            search(count, 2 * cur, k, visit)
        search(count + 1, cur + 1, k, visit)


if __name__ == "__main__":
    n, k = map(int, input().split())

    visit = [100000 for i in range(100001)]

    search(0, n, k, visit)
    print(visit[k])
