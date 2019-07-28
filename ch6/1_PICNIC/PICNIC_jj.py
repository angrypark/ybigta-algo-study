from collections import defaultdict
from sys import stdin
from copy import deepcopy


def mark(i, matched):
    matched = deepcopy(matched)
    matched[i] = True
    return matched
C = int(stdin.readline())
for _ in range(C):
    n, m = stdin.readline().split()
    n, m = int(n), int(m)
    lst = stdin.readline().split()
    D = defaultdict(list)
    for idx in range(m):
        i, j = int(lst[idx*2]), int(lst[idx*2+1])
        if i > j:
            i, j = j, i
        D[i].append(j)
    matched = [False for _ in range(n)]
    answer = [0]
    def match(i, matched):
        if i >= n:
            return
        if sum(matched) == n:
            answer[0] += 1
            return
        if matched[i]:
            match(i+1, matched)
            return
        matched[i] = True
        for j in D[i]: 
            if matched[j]:
                continue
            match(i+1, mark(j, matched))
    match(0, matched)
    print(answer[0])
