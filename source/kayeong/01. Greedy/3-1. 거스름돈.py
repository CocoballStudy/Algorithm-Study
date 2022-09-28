n = int(input())
count = 0
coins = [500, 100, 50, 10]  # 숫자 큰 동전부터 저장

for coin in coins:  # 동전 종류 큰것부터 확인
    count += n // coin
    # // : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
    n %= coin

print("결과 : ", count)