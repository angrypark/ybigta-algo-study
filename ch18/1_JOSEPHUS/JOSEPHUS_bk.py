from sys import stdin
from random import randint
C = int(stdin.readline())

for _ in range(C):
    N, K = [int(x) for x in stdin.readline().split()]
    lst = [x for x in range(2, N + 1)]
    point = 0
    while len(lst) > 2:
        curr_K = (K - 1) % len(lst)
        for _ in range(curr_K):
            point += 1
        while point >= len(lst):
            point -= len(lst)
        del lst[point]
    lst.sort()
    print(lst[0], lst[1])