n = int(input())
line = list(map(int, input().split()))
result = 0
temp = 0
line.sort()

for i in line:
    temp += i
    result += temp

print(result)
