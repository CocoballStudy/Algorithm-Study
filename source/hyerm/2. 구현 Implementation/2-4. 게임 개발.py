# 코딩중

while True:
    for i in range(10):
        print(i)
    break

n, m = map(int, input().split())  # n*m 사이즈 맵
a, b, d = map(int, input().split())  # 현재좌표 (a,b) 바라보는 방향 d

dlist = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
print(dlist[0][0])
print(dlist[0][1])

info = []
for _ in range(m):
    info.append(list(map(int, input().split())))

print(info)

while True:
    for _ in range(4):
        md = (d + 1) % 4
        ma = dlist[md][0]
        mb = dlist[md][1]
        print(info[ma][mb])


