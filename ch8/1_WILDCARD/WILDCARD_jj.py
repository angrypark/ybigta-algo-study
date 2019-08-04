from sys import stdin

def match(i, j):
    result = cache[i][j]
    if result != -1:
        return result
    if (i < len(pattern) and j < len(s)) and (pattern[i] == "?" or pattern[i] == s[j]):
        cache[i][j] = match(i+1, j+1)
        return cache[i][j]
    if i == len(pattern):
        return j == len(s)
    if pattern[i] == "*":
        if match(i+1, j) or (j < len(s) and match(i, j+1)):
            return True
    return False

C = int(stdin.readline())
for _ in range(C):
    pattern = stdin.readline().strip()
    N = int(stdin.readline())
    for _ in range(N):
        s = stdin.readline().strip()
        cache = [[-1 for _ in range(101)] for _ in range(101)]
        if match(0, 0):
            print(s)
            