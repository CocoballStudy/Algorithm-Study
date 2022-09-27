n = int(input())
move = list(input().split())

x = 1
y = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dname = ["R", "L", "U", "D"]

for m in move:
    for i in range(len(dname)):
        if(m==dname[i]):
            if 0 < x+dx[i] <n:
                x+=dx[i]
            if 0 < y+dy[i] < n:
                y+=dy[i]
            # print(m, x, y)

print(x, y)