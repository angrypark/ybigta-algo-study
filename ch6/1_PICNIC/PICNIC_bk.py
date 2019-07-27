from sys import stdin

C = int(stdin.readline().strip())
for i in range(C):
    n, _ = [int(x) for x in stdin.readline().strip().split()]
    pair = [int(x) for x in stdin.readline().strip().split()]
    friends = [[False for x in range(n)] for y in range(n)]

    for j in range(0, len(pair), 2):
        a, b = pair[j], pair[j+1]
        friends[a][b] = True
        friends[b][a] = True
    
    remain = list(x for x in range(n))
    def make_pair(remain, friends):
        if not remain:
            return 1
        a = remain[0]
        remain.remove(a)

        answer = 0
        for x, friend in enumerate(friends[a]):
            if friend and x in remain:
                answer += make_pair(list(set(remain) - set([x])), friends)
        return answer
    print(make_pair(remain, friends))