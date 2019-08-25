from sys import stdin

C = int(stdin.readline())

for _ in range(C):
    stack = []
    line = stdin.readline()
    for i, elem in enumerate(line):
        if elem == "(" or elem == "{" or elem == "[":
            stack.append(elem)
        elif stack:    
            if elem == ")" and stack[-1] == "(":
                stack.pop()
            elif elem == "}" and stack[-1] == "{":
                stack.pop()
            elif elem == "]" and stack[-1] == "[":
                stack.pop()
            else:
                break
        else:
            break
    if i == len(line) - 1 and not stack:
        print("YES")
    else:
        print("NO")