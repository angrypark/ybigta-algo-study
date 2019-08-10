from sys import stdin
DIV = 1000000007

C = int(stdin.readline())
for _ in range(C):
    N = int(stdin.readline())
    D = [0 for _ in range(N+1)]
    T = [0 for _ in range(N+1)]
    D[1] = 1
    D[2] = 2
    T[1] = 1
    T[2] = 2
    if N>2:
        T[3] = 1
        T[4] = 3
    for i in range(3, N+1):
        D[i] = D[i-1] + D[i-2]
        if i > 4:
            T[i] = T[i-4] + T[i-2]
    print((D[N]-T[N]) % DIV)
