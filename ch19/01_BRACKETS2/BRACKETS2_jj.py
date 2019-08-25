from sys import stdin

OPEN = '([{'
PAIR = {')':'(', '}':'{', ']':'['}

C = int(stdin.readline())
for _ in range(C):
    line = stdin.readline().strip()
    D = []
    is_valid = True and line
    for s in line:
        if s in OPEN:
            D.append(s)
        elif len(D) <= 0 or PAIR[s] != D.pop():
            is_valid = False
            break
    if D or not is_valid:
        print('NO')
    else:
        print('YES')

