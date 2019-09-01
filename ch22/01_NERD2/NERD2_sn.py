def is_dominated(A):
    right = [x for x in loc if x[0] > A[0]]
    if not right:
        return False
    return sorted(right, key=lambda x: x[0])[0][1] > A[1]


def remove_dominated(A):
    """A에 지배당하는 점들을 지운다"""
    global loc
    loc = [x for x in loc if (x[0] >= A[0]) or (x[1] >= A[1])]
    
    
def register(A):
    global loc, ret
    if is_dominated(A):
        return
    loc.append(A)
    remove_dominated(A)
    ret += len(loc)
    
    
C = int(input())
for _ in range(C):
    N = int(input())
    ret = 0
    loc = []
    
    for _ in range(N):
        A = list(map(int, input().split()))
        register(A)
        
    print(ret)
    