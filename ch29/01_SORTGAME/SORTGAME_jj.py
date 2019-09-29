from sys import stdin
from collections import deque, Counter


def reverse_sublist(s,start,end):
    ret = str(s)
    ret = ret[:start]+ret[start:end+1][::-1]+ret[end+1:]
    return ret

distance = dict()
def preCalc(n):
    global distance
    perm = '01234567'[:n]

    q = deque()
    q.append(perm)
    distance[perm] = 0

    while(len(q)):
        here = q.popleft()
        cost = distance[here]
        for i in range(n):
            for j in range(i+1, n):
                rvs_list = reverse_sublist(here, i, j)
                if not rvs_list in distance:
                    distance[rvs_list] = cost+1
                    q.append(rvs_list)


def rank(lst):
    s = sorted(lst)
    return ''.join([str(s.index(k)) for k in lst])

def solve(input):
    preCalc(len(input))
    return distance[rank(input)]

C = int(stdin.readline())
counter = Counter()
arr_list = list()
for _ in range(C):
    n = int(stdin.readline())
    arr = [int(k) for k in stdin.readline().strip().split(' ')]
    arr = rank(arr)
    arr_list.append(arr)
    counter[n] = n


for i in counter:
    preCalc(i)

for arr in arr_list:
    print(distance[arr])