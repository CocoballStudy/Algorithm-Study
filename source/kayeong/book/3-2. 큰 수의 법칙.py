n, m, k = map(int, input().split())  # n,m,k 공백으로 구분해서 입력받기
data = list(map(int, input().split()))  # n개의 수 공백으로 구분해서 입력

data.sort()  # 입력받은 수 정렬

first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m != 0:
            result += first
            m -= 1
        else:
            break
    if m != 0:
        result += second
        m -= 1
    else:
        break

print(result)
