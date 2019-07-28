from sys import stdin
C = int(stdin.readline())

def put():
    global string
    tree = []
    for _ in range(4):
        if not string:
            continue
        if string[0] == 'x':
            string = string[1:]
            node = put()
            tree.append(node)
        else:
            tree.append(string[0])
            string = string[1:]
    return tree

def restruct(tree):
    for i in range(4):
        if i < 2:
            tmp = tree[i+2]
            tree[i+2] = tree[i]
            tree[i] = tmp
        if isinstance(tree[i], list):
            restruct(tree[i])
    return tree
    
def tree2str(tree, s):
    for i in range(4):
        if isinstance(tree[i], list):
            s = tree2str(tree[i], s+'x')
        else:
            s += tree[i]
    return s
for _ in range(C):
    string = stdin.readline().strip()
    
    if string.startswith('x'):
        tree = put()[0]
        restruct(tree)
        print(tree2str(tree, 'x'))
    else:
        print(string)
    
        
