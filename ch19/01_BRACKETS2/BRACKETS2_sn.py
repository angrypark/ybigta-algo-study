match_dict = {')': '(', '}': '{', ']': '['}

def is_matched(text):
    brackets = []
    for s in text:
        if s in ['(', '{', '[']:
            brackets.append(s)
        if s in [')', '}', ']']:
            if not brackets:
                return False
            if brackets[-1] != match_dict[s]:
                return False
            brackets.pop(-1)
    return not brackets

C = int(input())

for _ in range(C):
    text = input() 
    if is_matched(text):
        print('YES')
    else:
        print('NO')