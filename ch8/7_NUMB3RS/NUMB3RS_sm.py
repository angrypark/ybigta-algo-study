def vector_mult(A, B, i, j):
    output = 0
    for k in range(len(A[i])):
        output += A[i][k] * B[k][j]
    return output


def dot(A, B):
    assert len(A[0]) == len(B)
    output = [[-1 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            output[i][j] = vector_mult(A, B, i, j)
    return output


num_test = int(input())
for _ in range(num_test):
    N, D, start = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(N)]
    p = [[x / sum(l[i]) for x in l[i]] for i in range(len(l))]
    m = [[0 for i in range(len(l[0]))] for j in range(len(l))]
    m[start][start] = 1
    for i in range(D):
        m = dot(m, p)
    prob = m[start]
    input()
    idx = list(map(int, input().split()))
    answer = [str(prob[i]) for i in idx]
    print(' '.join(answer))
