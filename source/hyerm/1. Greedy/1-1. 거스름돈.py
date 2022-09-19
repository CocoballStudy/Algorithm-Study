n = int(input())
result = 0 #동전의 최소 개수

coins = [500,100,50,10]
for coin in coins:
    result += n//coin
    n = n%coin

print(result)