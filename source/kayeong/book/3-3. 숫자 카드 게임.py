n, m = map(int, input().split())

result = 0

for i in range(n): # 한 행씩 입력받기
    data = list(map(int, input().split()))  # m개의 수 공백으로 구분해서 입력
    min_value = 10001 # 입력 받은 범위가 1~10000 이니까
    for a in data:
        min_value = min(min_value, a) # 행에서 최솟값 찾기
    result = max(result, min_value) # 최솟값 중에서 최댓값 찾기

print(result)
