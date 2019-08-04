from sys import stdin, maxsize
INF = maxsize

def split(idx, num_group):
    if idx >= N:
        return 0
    if num_group == 0:
        return INF
    ret = spl_cache[idx][num_group]
    if ret != -1:
        return ret
    ret = INF
    for size in range(1, N-idx+1):
        ret = spl_cache[idx][num_group] = min(ret, min_err(idx, size), split(idx+size, num_group-1))
    return ret

def min_err(idx, size):
    ret = min_cache[idx][size]
    if ret != -1:
        return ret
    m = round(sum(V[idx:idx+size]) / size)
    ret = min_cache[idx][size] =  sum( (V[i] - m)**2 for i in range(idx, idx+size) )
    return ret
    
C = int(stdin.readline().strip())
for _ in range(C):
    N, S = [int(k) for k in stdin.readline().strip().split()]
    V = sorted([int(k) for k in stdin.readline().strip().split()])
    spl_cache = [[-1 for _ in range(S+1)] for _ in range(N+1)]
    min_cache = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    print(split(0, S))
