strList = list(input())

answerCheckList=[]

quackList = ['q','u','a','c','k']

for s in strList:
    if s == 'q':
        if len(answerCheckList) == 0:
            answerCheckList.append(0)
        else:
            flag = False
            for current in range(len(answerCheckList)):
                if answerCheckList[current] == 4:
                    answerCheckList[current] = 0
                    flag = True
                    break
            if not flag:
                answerCheckList.append(0)

    else:
        tempIdx = quackList.index(s)
        flag = False
        for current in range(len(answerCheckList)):
            if answerCheckList[current] + 1 == tempIdx:
                answerCheckList[current] += 1
                flag = True
                break

        if not flag:
            print(-1)
            exit()


for i in answerCheckList:
    if i != 4:
        print(-1)
        exit()

print(len(answerCheckList))