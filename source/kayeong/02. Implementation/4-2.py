# 초 00~59 -> 03,13,23,30-39,43,53 = 15개씩 각 60개 = 15*60
# 분 00~59 -> 동일하게 15개씩 각 60개 존재
# 초, 분 둘 다 겹치는 경우 15가지는 빼줘야함 = 15*45
# 시 03, 13, 23 일 경우는 무조건 포함 = 60*60

N = int(input())
result = 0

if N < 3:
    result = (N+1)*(15*60 + 15*45)
elif N < 13:
    result = N*(15*60 + 15*45) + 60*60
elif N < 23:
    result = (N-1)*(15*60 + 15*45) + 2*60*60
else:
    result = (N-2)*(15*60 + 15*45) + 3*60*60

print(result)