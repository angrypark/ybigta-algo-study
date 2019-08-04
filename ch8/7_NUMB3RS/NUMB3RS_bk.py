from sys import stdin

C = int(stdin.readline())

for _ in range(C):
    N, D, P = [int(x) for x in stdin.readline().split()]
    adj = []
    for _ in range(N):
        adj.append([int(x) for x in stdin.readline().split()])
    cache = [[-1 for _ in range(D + 1)] for _ in range(N + 1)]
    def search(curr_city, day):
        if day == 0:
            if curr_city == P: return 1
            else: return 0
        
        if cache[curr_city][day] != -1:
            return cache[curr_city][day]
        
        cache[curr_city][day] = 0
        for city, connected in enumerate(adj[curr_city]):
            if connected:
                prop = 1 / sum(adj[city])
                cache[curr_city][day] += prop * search(city, day - 1)
        
        return cache[curr_city][day]

    stdin.readline()
    city_list = [int(x) for x in stdin.readline().split()]
    [print("%0.7f" % search(city, D), end=' ') for city in city_list]
    print()
        