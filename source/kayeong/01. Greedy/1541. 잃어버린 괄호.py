# 마이너스 기호를 만날 때 가장 큰 수를 빼야함
# -> 마이너스 기호를 만날 때 다음 마이너스까지, 다음 마이너스가 없는 경우 끝까지 모든 수를 더해서 한번에 빼기

arr = input().split('-') # - 기준으로 쪼개기
result = 0

for i in arr[0].split('+'): # arr[0] = 맨 처음 ~ - 연산 나오기 전까지의 숫자들
    result += int(i) # 모두 더하기
for i in arr[1:]: # 이후는 모두 빼줘야 하는 숫자들
    for j in i.split('+'): # 앞에 + 붙은 숫자들이 있으니까 + 기준으로 쪼개기
        result -= int(j) # 모두 빼주기

print(result)