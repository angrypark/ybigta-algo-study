C = int(input())

for _ in range(C):
    N, K = map(int, input().split())
    survivors = [i for i in range(2, N + 1)]
    die = 0
    while len(survivors) > 2:
        current = (K - 1) % len(survivors)
        die += current
        while die >= len(survivors):
            die -= len(survivors)
        del survivors[die]
    print(*sorted(survivors))