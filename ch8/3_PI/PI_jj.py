from sys import stdin, maxsize

INF = maxsize
C = int(stdin.readline().strip())

def score(i, size):
    s = S[i:i+size]
    if s == s[0]*len(s):
        return 1
    is_cumul = True
    for i in range(2, len(s)):
        if int(s[i]) - int(s[i-1]) != int(s[i-1]) - int(s[i-2]):
            False
            break
    if is_cumul:
        if int(s[1])-int(s[0]) == 1 or int(s[1])-int(s[0]) == -1:
            return 2
        return 5

    is_alt = True
    for i in range(1, len(s)):
        if int(s[i]) != int(s[i%2]):
            is_alt = False
    if is_alt:
        return 4
    return 10

def memorize(srt_idx):
    if srt_idx == len(S):
        return 0
    ret = cache[srt_idx]
    if ret != -1:
        return ret
    ret = INF
    for i in range(3, 6):
        if srt_idx + i <= len(S):
            ret = cache[srt_idx] = min(ret, memorize(srt_idx + i) + score(srt_idx, i))
    return ret
for _ in range(C):
    S = stdin.readline().strip()
    cache = [-1 for _ in range(10002)]
    print(memorize(0))