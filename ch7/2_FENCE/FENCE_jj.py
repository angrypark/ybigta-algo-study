from sys import stdin

def area(i, j, min_):
    min_ = min((F[i], F[j], min_))
    return min_ * (j - i + 1), min_

C = int(stdin.readline())
for _ in range(C):
    N = int(stdin.readline())
    F = [int(k) for k in stdin.readline().split()]
    i = N//2 - 1
    j = i + 1
    
    MAX_AREA = [0]
    def fill(i, j, min_):
        area_, min_ = area(i, j, min_)
        if area_ > MAX_AREA[0]:
            MAX_AREA[0] = area_
        if i > 0 and j < N-1:
            if F[i-1] > F[j-1]:
                fill(i-1, j, min_)
            else:
                fill(i, j+1, min_)
        elif i > 0:
            fill(i-1, j, min_)
        elif j < N-1:
            fill(i, j+1, min_)
    fill(i, j, 20000)
    print(MAX_AREA[0])