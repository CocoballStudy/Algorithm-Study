if __name__ == "__main__":
    n = int(input())
    cur = [1, 1]

    directions = list(input().split(' '))

    for d in directions:
        if d == 'R':
            if cur[1] + 1 > n:
                continue
            cur[1] += 1
        elif d == 'L':
            if cur[1] - 1 < 1:
                continue
            cur[1] -= 1
        elif d == 'U':
            if cur[0] - 1 < 1:
                continue
            cur[0] -= 1
        elif d == 'D':
            if cur[0] + 1 > n:
                continue
            cur[0] += 1
    print(cur[0], cur[1])
