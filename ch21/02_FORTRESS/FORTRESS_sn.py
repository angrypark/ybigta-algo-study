class Node(object):
    def __init__(self):
        self.children = []
        

def get_distance(i, j):
    return ((loc[i][0] - loc[j][0]) ** 2 + (loc[i][1] - loc[j][1]) ** 2) ** 0.5


def is_enclosed(i, j):
    return (radius[i] > radius[j]) and (get_distance(i, j) < (radius[i] - radius[j]) ** 0.5)


def is_child(i, j):
    if not is_enclosed(i, j):
        return False
    for k in range(N):
        if (k not in [i, j]) and is_enclosed(i, k) and is_enclosed(k, j):
            return False
    return True


def get_height(node):
    """
    해당 node를 root로 하는 tree의 높이를 계산.
    그와 동시에 임의의 두 노드 사이의 거리의 최댓값을 계산.
    """
    global longest
    if not node.children:
        return 0
    
    heights = []
    for child in node.children:
        heights.append(get_height(child))
    
    heights.sort()
    if len(heights) >= 2:
        longest = max(longest, 2 + heights[-2] + heights[-1])
    
    return heights[-1] + 1


def get_tree(i):
    ret = Node()
    for j in range(3):
        if is_child(i, j):
            ret.children.append(get_tree(j))
    return ret


C = int(input())
for _ in range(C):
    N = int(input())
    loc, radius = [], []
    longest = 0
    
    for _ in range(N):
        tmp = list(map(int, input().split()))
        loc.append(tmp[:2])
        radius.append(tmp[2])
    
    for i in range(N):
        root = get_tree(i)
        longest = max(longest, get_height(root))
        
    print(longest)