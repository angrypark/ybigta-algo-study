from sys import stdin

C = int(stdin.readline())
cache = [-1 for x in range(101)]
cache[0], cache[1], cache[2] = 1, 1, 2
def memo(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    if cache[n] != -1:
        return cache[n]
    
    cache[n] = (memo(n - 1) + memo(n - 2))
    return cache[n]

for _ in range(C):
    n = int(stdin.readline())
    if n % 2 == 0:
        print((memo(n) - cache[n // 2] - cache[n // 2 - 1]) % 1000000007)
    else:
        print((memo(n) - cache[(n-1) // 2]) % 1000000007)
        