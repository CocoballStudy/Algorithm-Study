str = list(input())


answer = ''

tempXcount = 0
for i in range(len(str)):
    if str[i] == 'X':
        tempXcount += 1
    else:
        if tempXcount != 0:
            AAAACount = tempXcount // 4
            tempXcount = tempXcount % 4
            BBCount = tempXcount // 2
            tempXcount = tempXcount % 2

            if tempXcount != 0:
                print(-1)
                exit()
            else:
                for i in range(AAAACount):
                    answer += 'AAAA'
                for i in range(BBCount):
                    answer += 'BB'
        tempXcount = 0
        answer += '.'


if tempXcount != 0:
    AAAACount = tempXcount // 4
    tempXcount = tempXcount % 4
    BBCount = tempXcount // 2
    tempXcount = tempXcount % 2

    if tempXcount != 0:
        print(-1)
        exit()
    else:
        for i in range(AAAACount):
            answer += 'AAAA'
        for i in range(BBCount):
            answer += 'BB'

print(answer)