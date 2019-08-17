def func(n, k):
    l = [str(i) for i in range(2, n + 1)]
    pos = 0
    while len(l) > 2:
        pos = (pos + k - 1) % len(l)
        l.remove(l[pos])
    print(' '.join(l))


num_test = int(input())
for _ in range(num_test):
    num_people, skip = map(int, input().split())
    func(num_people, skip)
