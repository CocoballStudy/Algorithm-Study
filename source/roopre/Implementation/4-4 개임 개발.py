"""
N X M 직사각형

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은
칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다.
단, 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력
0 북쪽
1 동쪽
2 남쪽
3 서쪽
"""


def get_left(direction):
    if direction == 0:
        return 3
    elif direction == 1:
        return 0
    elif direction == 2:
        return 1
    else:
        return 2


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x, y = map(int, input().split(' '))
    visit = [[False for i in range(y)] for j in range(x)]
    cur_x, cur_y, direction = map(int, input().split(' '))
    m = [list(map(int, input().split(' '))) for i in range(x)]
    ans = 0
    visit[cur_x][cur_y] = 1
    while True:
        # 1.현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
        # 회전부터 함
        flag = False
        for i in range(4):
            direction = get_left(direction)
            nx = cur_x + dx[direction]
            ny = cur_y + dy[direction]
            if x > nx >= 0 and y > ny >= 0:
                if m[nx][ny] == 0 and visit[nx][ny] == 0:
                    cur_x, cur_y = nx, ny
                    visit[nx][ny] = 1
                    ans += 1
                    flag = True
            if flag:
                break
            if i == 3 and flag == False:
                print(ans+1)
                exit(0)
