from sys import stdin

C = int(stdin.readline())

for _ in range(C):
    N = int(stdin.readline())

    shifted = [int(x) for x in stdin.readline().split()]
    curr_arr = [x for x in range(1, N+1)]

    answer = []
    for i in range(N - 1, -1, -1):
        bigger = shifted[i]
        answer.append(curr_arr[-bigger-1])
        del curr_arr[-bigger-1]
    
    print(" ".join([str(x) for x in answer[::-1]]))