from sys import stdin

C = int(stdin.readline())
for _ in range(C):
    stdin.readline()
    A = [int(x) for x in stdin.readline().split()]
    B = [int(x) for x in stdin.readline().split()]

    cache = [[-1 for _ in range(101)] for _ in range(101)]
    def find(i_A, i_B):
        if cache[i_A][i_B] != -1:
            return cache[i_A][i_B]
        
        cache[i_A][i_B] = 2
        a = float('-inf') if i_A == -1 else A[i_A]
        b = float('-inf') if i_B == -1 else B[i_B]
        curr_max = max(a, b)

        for i in range(i_A + 1, len(A)):
            if curr_max < A[i]:
                cache[i_A][i_B] = max(cache[i_A][i_B], find(i, i_B) + 1)
        for i in range(i_B + 1, len(B)):
            if curr_max < B[i]:
                cache[i_A][i_B] = max(cache[i_A][i_B], find(i_A, i) + 1)
        return cache[i_A][i_B]
    print(find(-1, -1) - 2)