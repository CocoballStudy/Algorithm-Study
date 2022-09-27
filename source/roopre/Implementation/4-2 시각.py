if __name__ == "__main__":
    s = 0
    ans = 0
    hh = int(input())

    cur_h = 0
    cur_m = 0
    cur_s = 0

    while not (cur_h == hh and cur_m == 59 and cur_s == 59):
        cur_s += 1
        if cur_s >= 60:
            cur_s = 0
            cur_m += 1
        if cur_m >= 60:
            cur_m = 0
            cur_h += 1

        if (str(cur_h)+str(cur_m)+str(cur_s)).count('3') > 0:
            ans += 1

    print(ans)
