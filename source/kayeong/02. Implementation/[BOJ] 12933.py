sound = input()
quack = ['q', 'u', 'a', 'c', 'k']
flag = [False] * len(sound)
result = 0
index = 0  # quack 인덱스 저장하는 변수
array = []

if len(sound) < 5:
    print(-1)
else:
    for a in range(len(sound)):
        if sound[a] == 'q' and not flag[a]:
            first = True  # 처음 방문하는 q 는 첫번째로 표시
            for i in range(len(sound)):
                if quack[index] == sound[i] and not flag[i]:
                    print(sound[i])
                    flag[i] = True
                    if sound[i] == 'k':
                        if first:
                            result += 1
                            first = False  # quack 하나 만들었으니까 first 는 다시 false
                        index = 0  # quack 다시 돌아야하니까 인덱스도 다시 초기화
                        continue
                    index += 1

if result == 0 or not all(flag):
    print(-1)
else:
    print(result)
