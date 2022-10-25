def convert(n,k):
    i = 0
    ans = ""
    while k**i <= n:
        i+=1
    for j in reversed(range(0,i)):
        if n >= (k**j):
            ans += str(int(n/(k**j)))
            n = n - int(n/(k**j))*(k**j)
        else:
            ans += "0"
    return ans
def solution(n, k):
    cv = convert(n, k)
    q = ""
    count = 0
    check = prime_check()
    for i in range(len(cv)):
        if cv[i] == '0':
            if q != "" and check[int(q)]:

                count += 1
            q = ""
        else:
            q += cv[i]

    if q != "" and check[int(q)]:
        count += 1
    return count
def prime_check():
    MAX_NUM = 1000000
    check = [True for i in range(MAX_NUM)]
    check[0] = False
    check[1] = False
    for i in range(2, (MAX_NUM // 2)):
        if check[i]:
            for j in range(2, MAX_NUM // i):
                check[i * j] = False

    return check
if __name__ == "__main__":
    solution(437674,3)