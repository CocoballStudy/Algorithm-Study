# 빠르게 끝나는 회의일수록 더 많은 회의가 진행될 수 있다
# -> 1. "끝나는 시간"이 빠른 순서대로 정렬
# 회의 사이의 시간은 최소화해야 더 많은 회의가 진행될 수 있다
# -> 2. "시작하는 시간"이 빠른 순서대로 정렬

n = int(input())

meetings = []
for i in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))  # sort 의 정렬 기준 = 종료시간->시작시간

count = 1
end_time = meetings[0][1]
for i in range(1, n):
    if meetings[i][0] >= end_time:
        count += 1
        end_time = meetings[i][1]

print(count)