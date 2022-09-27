"""
1. 수평으로 두칸 이동 뒤 수직 한칸 이동
2. 수직으로 두칸 이동 뒤 수평 한칸 이동
"""

if __name__ == "__main__":
    cur = input()

    cur_x = ord(cur[0]) - ord('a')
    cur_y = int(cur[1]) - 1

    dx = [2, -2, 2, -2]
    dy = [1, 1, -1, -1]

    ans = 0
    for i in range(4):
        if 7 > cur_x + dx[i] >= 0 and 7 > cur_y + dy[i] >= 0:
            ans += 1

        if 7 > cur_x + dy[i] >= 0 and 7 > cur_y + dx[i] >= 0:
            ans += 1
    print(ans)