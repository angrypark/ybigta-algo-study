from sys import stdin
from collections import deque

class Generator:
    def __init__(self):
        self.seed = 1983
    def next(self):
        new_number = self.seed % 10000 + 1
        self.seed = (self.seed * 214013 + 2531011) % (2 ** 32)
        return new_number

C = int(stdin.readline())
for _ in range(C):
    g = Generator()
    K, N = [int(x) for x in stdin.readline().split()]
    queue = deque()
    curr_sum = 0
    answer = 0
    for _ in range(N):
        new_number = g.next()
        queue.append(new_number)

        curr_sum = curr_sum + new_number
        
        while curr_sum > K:
            head = queue.popleft()
            curr_sum -= head

        if curr_sum == K:
            answer += 1
    print(answer)


