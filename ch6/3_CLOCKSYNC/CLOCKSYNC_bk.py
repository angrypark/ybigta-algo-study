from sys import stdin

INF = 9999
SWITCHES = {
    0: (0, 1, 2),
    1: (3, 7, 9, 11),
    2: (4, 10, 14, 15),
    3: (0, 4, 5, 6, 7),
    4: (6, 7, 8, 10, 12),
    5: (0, 2, 14, 15),
    6: (3, 14, 15),
    7: (4, 5, 7, 14, 15),
    8: (1, 2, 3, 4, 5),
    9: (3, 4, 5, 9, 13)
}
C = int(stdin.readline().strip())

for _ in range(C):
    clocks = [int(x) for x in stdin.readline().strip().split()]

    def is_aligned(clocks):
        if len(set(clocks)) == 1 and 12 in set(clocks):
            return True
        else:
            return False

    def push(clocks, switch):
        for clock in SWITCHES[switch]:
            if clocks[clock] < 12:
                clocks[clock] += 3
            else:
                clocks[clock] = 3

    def solve(clocks, switch):
        if switch == len(SWITCHES):
            if is_aligned(clocks): 
                return 0
            else:
                return INF
        
        answer = INF
        for count in range(4):
            answer = min(answer, count + solve(clocks, switch + 1))
            push(clocks, switch)
        return answer
    
    answer = solve(clocks, 0)
    if answer == INF:
        answer = -1
    print(answer)