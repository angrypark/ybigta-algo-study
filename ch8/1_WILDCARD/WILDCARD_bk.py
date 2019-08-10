from sys import stdin

C = int(stdin.readline())

for _ in range(C):
    pattern = stdin.readline()
    n = int(stdin.readline())
    result_list = []
    for _ in range(n):
        string = stdin.readline()
        def match(i_wildcard, i_string):
            if i_wildcard == len(pattern):
                if i_string == len(string) or pattern[-1] == "*":
                    return True
            while i_wildcard < len(pattern) and i_string < len(string) and (pattern[i_wildcard] == "?" or pattern[i_wildcard] == string[i_string]):
                i_wildcard += 1
                i_string += 1
            
            if i_wildcard == len(pattern) and i_string == len(string):
                    return True
            if i_wildcard < len(pattern) and pattern[i_wildcard] == '*':
                for new_index in range(i_string, len(string)):
                    if match(i_wildcard + 1, new_index):
                        return True
            return False
        if match(0, 0):
            result_list.append(string)
    result_list.sort()
    for string in result_list:
        print(string)