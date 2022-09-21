"""
입력 : 시작시간 끝나는 시간
회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
"""
from functools import cmp_to_key


def myCompare(time1, time2):
    if time1[1] > time2[1]:
        return 1

    elif time1[1] == time2[1]:
        if time1[0] > time2[0]:
            return 1
        else:
            return -1
    return -1


if __name__ == '__main__':
    n = int(input())
    meetings = []
    answer = 0

    for i in range(n):
        start, end = map(int, input().split(' '))
        meetings.append([start, end])

    meetings = sorted(meetings, key=cmp_to_key(myCompare))
    print(meetings)

    lastMeeting = meetings[0]
    answer += 1

    for i in range(1, len(meetings)):
        if meetings[i][0] >= lastMeeting[1]:
            lastMeeting = meetings[i]
            answer += 1

    #print(meetings)
    print(answer)
