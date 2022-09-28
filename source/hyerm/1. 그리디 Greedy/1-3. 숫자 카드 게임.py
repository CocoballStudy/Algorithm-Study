n, m = map(int, input().split())

result = 0

for i in range(n):
    rlist = list(map(int, input().split()))
    rlist.sort()
    if(rlist[0] > result):
        result=rlist[0]

print(result)