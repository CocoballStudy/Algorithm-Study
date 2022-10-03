now = input()
row = int(now[1])
col = int(ord(now[0])) - int(ord('a')) + 1
# ord 함수 = 문자에 해당하는 유니코드 정수 반환
# chr 함수 = 정수에 해당하는 유니코드 문자 반황

steps = [(-2, -1), (2, -1), (-2, 1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

result = 0
for i in steps:
    if row+i[0] >= 1 and row+i[0] <= 8 and col+i[1] >= 1 and col+i[1] <= 8 :
        result += 1

print(result)