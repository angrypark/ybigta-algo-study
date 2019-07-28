from sys import stdin
from copy import deepcopy

BLOCK_DY = ((0, 0, 1), (0, 0, 1), (0, 1, 1), (0, 1, 1))
BLOCK_DX = ((0, 1, 0), (0, 1, 1), (0, 0, 1), (0, -1, 0))

C = int(stdin.readline().strip())

for _ in range(C):
    H, W = [int(x) for x in stdin.readline().strip().split()]
    world = []
    for _ in range(H):
        world.append([1 if x == "#" else 0 for x in stdin.readline().strip()])

    def fill_world(world):
        def set_world(world, y, x, case, delta):       
            def is_valid(world, y, x):
                if y < 0 or x < 0 or y >= H or x >= W:
                    return False
                else:
                    return True
            
            flag = True
            for i in range(3):
                new_y = y + BLOCK_DY[case][i]
                new_x = x + BLOCK_DX[case][i]
                if not is_valid(world, new_y, new_x):
                    flag = False
                else:
                    world[new_y][new_x] += delta
                    if world[new_y][new_x] > 1:
                        flag = False
            return flag
        
        def start(world):
            for y, line in enumerate(world):
                for x, point in enumerate(line):
                    if point == 0:
                        return y, x
            return -1, -1

        y, x = start(world)
        if y == -1:
            return 1

        answer = 0
        for case in range(4):
            if set_world(world, y, x, case, 1):
                answer += fill_world(world)
            set_world(world, y, x, case, -1)
        return answer
    print(fill_world(world))