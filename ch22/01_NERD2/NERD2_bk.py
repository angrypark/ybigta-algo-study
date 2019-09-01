from sys import stdin
import bisect

C = int(stdin.readline())

for _ in range(C):
    attn = []
    N = int(stdin.readline())
    num = 0
    for _ in range(N):
        p, q = [int(x) for x in stdin.readline().split()]
        
        index = bisect.bisect(attn, [p, q])
        if index == len(attn) or q > attn[index][1]:
            attn.insert(index, [p, q])
            index -= 1
            while index >= 0:
                if attn[index][1] > q:
                    break

                if attn[index][1] < q:
                    del attn[index]
                else:
                    index -= 1
        num += len(attn)
    print(num)