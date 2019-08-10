from sys import stdin, maxsize

NEG = -1 * maxsize
def jlis(i1, i2):
    result = cache[i1+1][i2+1]
    if result != -1:
        return result
    e1 = NEG if i1 == -1 else a1[i1]
    e2 = NEG if i2 == -1 else a2[i2]
    m = max(e1, e2)
    for i in range(i1+1, n1):
        if m < a1[i]:
            result = max(result, jlis(i, i2)+1)
    for i in range(i2+1, n2):
        if m < a2[i]:
            result = max(result, jlis(i1, i)+1)
    return result

C = int(stdin.readline().strip())
for _ in range(C):
    n1, n2 = [int(k) for k in stdin.readline().strip().split()]
    a1 = [int(k) for k in stdin.readline().strip().split()]
    a2 = [int(k) for k in stdin.readline().strip().split()]
    cache = [[-1 for _ in range(101)] for _ in range(101)]
    print(jlis(0, 0))