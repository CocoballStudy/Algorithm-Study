N = int(input())
directions = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D']

for i in directions:
    for j in range(len(moves)):
        if i == moves[j]:
            if x + dx[j] < 1 or x + dx[j] > N or y + dy[j] < 1 or y + dy[j] > N:
                continue
            else:
                x += dx[j]
                y += dy[j]

print(x, y)
