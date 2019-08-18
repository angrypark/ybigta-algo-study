from sys import stdin

C = int(stdin.readline().strip())

for _ in range(C):
    members = [1 if x == "M" else 0 for x in stdin.readline().strip()]
    fans = [1 if x == "M" else 0 for x in stdin.readline().strip()]

    def func(A, B):
        if len(A) > len(B):
            return func(B, A)
        
        start_A = 0
        answer = 0
        while True:
            if start_A + len(A) > len(B):
                return answer
            else:
                curr_B = B[start_A:start_A + len(A)]
                hug = [1 if (curr_B[i] == 1) and (A[i] == 1) else 0 for i in range(len(A))]
                if sum(hug) == 0:
                    answer += 1
                start_A += 1
    
    print(func(members, fans))