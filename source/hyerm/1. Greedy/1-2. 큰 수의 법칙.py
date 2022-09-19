n, m, k = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()

result = 0

while(m>0):
    for _ in range(0,k):
        result+=nlist[n-1]
        m-=1
    result += nlist[n - 2]
    m -= 1

print(result)