changeMoney = int(input())

answer = -1
maxFiveCent = changeMoney // 5
for count in range(maxFiveCent+1):
    tempCount = count
    leftMoney = changeMoney - 5 * count
    if leftMoney % 2 == 0:
        tempCount += (leftMoney // 2)
        if answer == -1:
            answer = tempCount
        else:
            answer = min(answer, tempCount)

print(answer)

