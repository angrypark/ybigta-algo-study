from sys import stdin

blocks = [[[0, 0], [1, 0], [0, 1]],
          [[0, 0], [0, 1], [1, 1]],
          [[0, 0], [1, 0], [1, 1]],
          [[0, 0], [1, 0], [1, -1]]]

def set_block(D, y, x, type, delta):
        # block x, y
        for i in range(3):
            ny = y + blocks[type][i][0]
            nx = x + blocks[type][i][1]
            is_valid = not(ny < 0 or ny >= H or nx < 0 or nx >= W)
            if is_valid:
                D[ny][nx] += delta
                is_valid = D[ny][nx] > 1
        return is_valid

def cover(D):
    x, y = -1, -1
    for i in range(H):
        for j in range(W):
            if D[i][j] == 0:
                y, x = i, j
                break
        if y != -1:
            break
    if y == -1:
        return 1
    ans = 0
    for type_ in range(4):
        if set_block(D, y, x, type_, 1):
            ans += cover(D)
        set_block(D, y, x, type_, -1)
    return ans

C = int(stdin.readline())
for _ in range(C):
    H, W = stdin.readline().split()
    H, W = int(H), int(W)
    D = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        elems = stdin.readline().strip()
        for j in range(W):
            D[i][j] = int(elems[j] == '#')
    print(cover(D))
        
