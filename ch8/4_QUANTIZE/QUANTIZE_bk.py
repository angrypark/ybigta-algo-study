from sys import stdin

C = int(stdin.readline())
for _ in range(C):
    _, s = [int(x) for x in stdin.readline().split()]
    numbers = [int(x) for x in stdin.readline().split()]
    numbers.sort()

    cache = [[-1 for _ in range(s+1)] for _ in range(len(numbers)+1)]
    """def min_err(a, b):
        mean = round(sum(numbers[a:b+1]) / len(numbers[a:b+1]))
        return sum([(x - mean) ** 2 for x in numbers[a:b+1]])
    """
    pSum = [0 for _ in range(len(numbers) + 1)]
    pSqSum = [0 for _ in range(len(numbers) + 1)]
    pSum[0] = numbers[0]
    pSqSum[0] = numbers[0] ** 2
    for i in range(1, len(numbers)):
        pSum[i] = pSum[i - 1] + numbers[i]
        pSqSum[i] = pSqSum[i - 1] + numbers[i] ** 2
    def min_err(a, b):
        if a == 0:
            x = pSum[b]
            y = pSqSum[b]
        else:
            x = pSum[b] - pSum[a - 1]
            y = pSqSum[b] - pSqSum[a - 1]
        
        m = int(0.5 + x / (b - a + 1))
        return y - 2 * m * x + m * m * (b - a + 1)
    def quantize(start, len_set):
        if start == len(numbers): return 0
        if len_set == 0: return 987654321
        if cache[start][len_set] != -1:
            return cache[start][len_set]
        
        cache[start][len_set] = 987654321
        for i in range(start, len(numbers)):
            cache[start][len_set] = min(min_err(start, i) + quantize(i + 1, len_set - 1), cache[start][len_set])
        
        return cache[start][len_set]
    print(quantize(0, s))