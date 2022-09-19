from functools import cmp_to_key
import heapq
import sys

def myCompare(study1, study2):
    if study1[0] > study2[0]:
        return 1
    if study1[0] == study2[0] and study1[1] > study2[1]:
        return 1
    return -1




if __name__ == "__main__":

    #n = int(input())
    n = int(sys.stdin.readline())
    study = []
    room = []

    for i in range(n):
        study.append(list(map(int, sys.stdin.readline().split(' '))))

    study = sorted(study, key=cmp_to_key(myCompare))
    #study = sorted(study, key=lambda x : (x[0],x[1]))
    #print(study)

    room.append(study[0][1])
    heapq.heapify(room)

    for i in range(1, len(study)):
        tmp = []
        if room[0] > study[i][0]:
            heapq.heappush(room, study[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room, study[i][1])

    print(len(room))
