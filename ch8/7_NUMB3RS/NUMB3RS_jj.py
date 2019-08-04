from sys import stdin
from collections import defaultdict

def go(src, day, prob):
    if day >= d:
        v = Q.get(src)
        if v is not None:
            Q[src] += prob
        return
    candidates = G.get(src)
    if candidates:
        for dst in candidates:
            go(dst, day+1, prob*(1/len(candidates)))

C = int(stdin.readline())
for _ in range(C):
    n, d, p = [int(k) for k in stdin.readline().strip().split()]
    G = defaultdict(list)
    for i in range(n):
        for j, e in enumerate(stdin.readline().strip().split()):
            e = int(e)
            if e:
                G[i].append(j)
    t = int(stdin.readline())
    q_list = [int(k) for k in stdin.readline().strip().split()]
    Q = {q: 0.0 for q in q_list}
    go(p, 0, 1)
    res = ' '.join([str(Q[q]) for q in q_list])
    print(res)
