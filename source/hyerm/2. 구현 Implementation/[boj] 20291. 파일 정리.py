result = []

n = int(input())

for _ in range(0, n):
    result.append(list(input().split("."))[1])

result.sort()

tname = result[0]
count = 0
for r in result:
    if(tname==r):
        count += 1
    else:
        print(tname, count)
        tname = r
        count = 1
print(tname, count)
