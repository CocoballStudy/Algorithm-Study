position = list(input())
position[0] = ord(position[0])-96

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

count = 0

for i in range(0,8):
    x = position[0]+dx[i]
    y = int(position[1])+dy[i]
    if 1<=x and x<=8 and 1<=y and y<=8:
        count+=1

print(count)