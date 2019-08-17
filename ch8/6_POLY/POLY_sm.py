# TODO: if number of polyomino is over 10,000,000 print out the remainder after dividing by 10,000,000
def polyomino(n):
    output = 0
    for i in range(1, n + 1):
        output += func(n, i)
    return output % 10000000


def placeable(n, k):
    return n + k - 1


def func(total, first_row):
    if cache[total][first_row] != -1:
        return cache[total][first_row]
    if total == first_row:
        return 1
    output = 0
    remaining = total - first_row
    for i in range(1, remaining + 1):
        output += (placeable(first_row, i) * func(remaining, i)) % 10000000
    cache[total][first_row] = output % 10000000
    return cache[total][first_row]


cache = [[-1 for i in range(101)] for j in range(101)]
num_test = int(input())
for _ in range(num_test):
    num_rect = int(input())
    print(polyomino(num_rect))
