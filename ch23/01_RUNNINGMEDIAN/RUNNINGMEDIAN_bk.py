import bisect
from sys import stdin

C = int(stdin.readline())

for _ in range(C):
    N, a, b = [int(x) for x in stdin.readline().split()]
    num = 1983
    heap = []
    answer = 0
    for _ in range(N):
        bisect.insort(heap , num)
        answer += heap[(len(heap) + 1) // 2 - 1] % 20090711
        num = (num * a + b) % 20090711
    print(answer % 20090711)
