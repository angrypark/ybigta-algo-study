def signal_generator(N):
    answer = 1983
    yield 1984
    for _ in range(N):
        answer = (answer * 214013 + 2531011) % 4294967296
        yield answer % 10000 + 1
        
def solution(K, N):
    """합이 K, 연속된 N개의 숫자들"""
    ret, queue = 0, []
    sg = signal_generator(N)
    range_sum = 0
    
    for start in range(N):
        new_signal = next(sg)
        range_sum += new_signal
        queue.append(new_signal)
        
        while range_sum > K:
            range_sum -= queue[0]
            queue.pop(0)
        
        if range_sum == K:
            ret += 1
    return ret

C = int(input())

for _ in range(C):
    N, K = map(int, input().split())
    print(solution(N, K))
