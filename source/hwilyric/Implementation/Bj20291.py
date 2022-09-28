N = int(input())
fileDic = {}
for i in range(N):
    fileExtension = list(input().split('.'))[1]

    if fileExtension in fileDic:
        fileDic[fileExtension] += 1
    else:
        fileDic[fileExtension] = 1

extensionList = list(fileDic.keys())
extensionList.sort()
for e in extensionList:
    print(e + ' ' + str(fileDic[e]))