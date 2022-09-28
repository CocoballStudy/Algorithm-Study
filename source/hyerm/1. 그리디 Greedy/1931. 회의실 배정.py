n = int(input())

time = list()
for _ in range(0,n):
    time.append(list(map(int, input().split())))
    time.sort()
    print(time)

result = 0
