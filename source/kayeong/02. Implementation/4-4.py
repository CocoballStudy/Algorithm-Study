n, m = map(int, input().split())  # 맵 크기 n x m
a, b, d = map(int, input().split())  # (a, b) 좌표에서 d 방향을 보고 서있는 캐릭터

array = []  # 맵 정보 저장할 배열 생성
for i in range(n):  # 행 n개 입력 받기
    array.append(list(map(int, input().split())))

directions = [0, 1, 2, 3]

dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]

count = 1  # 시작할때 한 칸 방문했으니까 count 1 로 시작
check = 0  # 회전 횟수


def turn():  # 왼쪽으로 회전
    global d
    d -= 1
    if d == -1:
        d = 3


while True:
    turn()
    nx = a + dx[d]
    ny = b + dx[d]

    if array[nx][ny] == 0:
        a = nx
        b = ny
        count += 1
        check = 0
        array[nx][ny] = 1  # 방문한 곳 다시 방문 못하게 1로 표시
        continue
    else:
        check += 1

    if check == 4:
        nx = a - dx[d]
        ny = b - dx[d]

        if array[nx][ny] == 0:
            a = nx
            b = ny
    else:
        break

    check = 0

print(count)
