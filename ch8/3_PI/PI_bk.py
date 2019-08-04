import sys
from sys import stdin
sys.setrecursionlimit(10**6)

C = int(stdin.readline().strip())
for _ in range(C):
    string = stdin.readline().strip()
    cache = [-1 for x in range(len(string))]
    def classify(a, b):
        integers = [int(x) for x in string[a: b + 1]]
        if len(set(integers)) == 1:
            return 1
        
        increasing = True
        d = integers[0] - integers[1]
        for i in range(len(integers) - 1):
            if integers[i] - integers[i + 1] != d:
                increasing = False
        if increasing and abs(d) == 1:
            return 2
        
        alter = True
        for i in range(len(integers)):
            if integers[i] != integers[i % 2]:
                alter = False
        if alter:
            return 4
        
        if increasing:
            return 5
        return 10
        
    def memorize(begin):
        if begin >= len(cache): return 0
        if cache[begin] != -1: return cache[begin]
        
        cache[begin] = float('inf')
        for i in range(2, 5):
            if begin + i + 1 <= len(cache):
                cache[begin] = min(cache[begin], classify(begin, begin + i) + memorize(begin + i + 1))
        return cache[begin]

    print(memorize(0))