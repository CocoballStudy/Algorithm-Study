'''
내 힘으로 구글링도 하지 않고 직접 푼 첫 골드문제 (아마도)
3시간 정도 풀었고 빡구현이라서 어려운 스킬은 없었지만
구현문제는 빨리 푸는 연습을 해야겠다는 점을 느낌

keypoint 1> KeyError가 발생함
- 파이썬을 한지는 얼마 안되긴 했지만 진짜 처음보는 에러였다..
구글링해보니까 딕셔너리를 사용할 때 없는 인덱스를 접근하면 나는 오류.
근데 일단 값이 없을리가 없없다.. 그래서 계속 반례를 찾아보니까..

주변에 친구가 없고 빈자리도 없는 경우를 미쳐 생각지도 못했다.
그래서 저 점을 조건문으로 제약을 주니 답이 나왔다..
항상 예외를 생각하는 습관을 갖자..

- 백준 21608 회고 완-
'''
N = int(input())

# 항상 첫 시작은 (2,2)
array = [[0 for col in range(N)] for row in range(N)]
studentDict = {}
steps = [[0,1],[1,0],[0,-1],[-1,0]]

for i in range(N*N):
    inputList = list(map(int, input().split()))

    # 학생 만족도를 구하기 위해서 미리 저장해두는 리스트
    studentDict[inputList[0]] = []
    for j in range(1,5):
        studentDict[inputList[0]].append(inputList[j])

    likeStudentList = studentDict[inputList[0]]
    tempArray = [[[0,0] for col in range(N)] for row in range(N)]

    # 배열을 돌면서 현 상황에서의 가장 최적의 공간 찾기
    for k in range(N):
        for l in range(N):
            # 상하좌우 체크
            tempEmpty = 0
            tempLikeFriend = 0
            if array[k][l] == 0:
                for step in steps:
                    dx = k + step[0]
                    dy = l + step[1]
                    if 0 <= dx < N and 0 <= dy < N:
                        if array[dx][dy] == 0:
                            tempEmpty+= 1
                        elif array[dx][dy] in likeStudentList:
                            tempLikeFriend += 1
                tempArray[k][l] = [tempEmpty,tempLikeFriend]
            else:
                tempArray[k][l] = [-1,-1]

    # 답이 될 수 있는 후보
    candidateIndex=[]
    change = True
    currentMax = 0

    # 1번 조건이 될 수 있는
    for k in range(N):
        for l in range(N):
            if tempArray[k][l][1] >= 0:
                if tempArray[k][l][1] > currentMax:
                    if array[k][l] == 0:
                        candidateIndex.clear()
                        change = False
                        candidateIndex.append([k,l])
                        currentMax = tempArray[k][l][1]
                elif tempArray[k][l][1] == currentMax:
                    if array[k][l] == 0:
                        candidateIndex.append([k,l])

    # # 만약 아무값도 갱신 안되어있다면 이건 비어있는 것이라서 1,1에 넣기
    if currentMax == 0 and not change: # 틀리면 여기를 봐야함
        array[1][1] = inputList[0]

    # 만약 배열의 길이가 1이라면 이걸로 값 넣고 끝 -> 1번 종료
    elif len(candidateIndex) == 1:
        array[candidateIndex[0][0]][candidateIndex[0][1]] = inputList[0]

    # 배열의 길이가 2이상이면 2번 조건으로 고고
    else:
        # 2번 조건 고고링
        answerIndexList = []
        answerMax = 0
        for m,n in candidateIndex:
            if tempArray[m][n][0] > answerMax:
                if array[m][n] == 0:
                    answerIndexList.clear()
                    answerIndexList.append([m, n])
                    answerMax = tempArray[m][n][0]
            elif tempArray[m][n][0] == answerMax:
                if array[m][n] == 0:
                    answerIndexList.append([m, n])

        # 만약 2번 조건의 길이가 1이라면 값 넣고 종료
        if len(answerIndexList) == 1:
            array[answerIndexList[0][0]][answerIndexList[0][1]] = inputList[0]

        # 그게 아니라면 맨 앞에 있는 인덱스에 넣기
        else:
            answerIndexList.sort(key=lambda x:x[0])
            array[answerIndexList[0][0]][answerIndexList[0][1]] = inputList[0]


answerArray = [[0 for col in range(N)] for row in range(N)]
for i in range(N):
    for j in range(N):
        stdList = studentDict[array[i][j]]
        tempAnswer = 0
        for step in steps:
            dx = i + step[0]
            dy = j + step[1]
            if 0 <= dx < N and 0 <= dy < N:
                if array[dx][dy] in stdList:
                    tempAnswer+=1
        answerArray[i][j] = tempAnswer

result = 0
for i in range(N):
    for j in range(N):
        if answerArray[i][j] == 0:
            result += 0
        elif answerArray[i][j] == 1:
            result += 1
        elif answerArray[i][j] == 2:
            result += 10
        elif answerArray[i][j] == 3:
            result += 100
        elif answerArray[i][j] == 4:
            result += 1000

print(result)