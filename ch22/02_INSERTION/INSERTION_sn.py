C = int(input())
for _ in range(C):
    N = int(input())
    shift = list(map(int, input().split()))
    
    origin = list(range(1, N + 1))
    ret = []
    for s in shift[::-1]:
        x = origin.pop(len(origin) - s - 1)
        ret = [x] + ret
    
    print(' '.join(map(str, ret)))