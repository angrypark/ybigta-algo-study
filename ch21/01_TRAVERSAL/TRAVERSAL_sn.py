class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

        
def BinaryTree(preorders, inorders):
    if not preorders:
        return None
    node = Node(preorders[0])
    slice = inorders.index(preorders[0])
    node.left = BinaryTree(preorders[1:slice+1], inorders[0:slice])
    node.right = BinaryTree(preorders[slice+1:], inorders[slice+1:])
    return node

def postorder_traverse(node):
    if(node == None):
        return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    ret.append(str(node.key))
    

C = int(input())

for _ in range(C):
    N = int(input())
    preorders = list(map(int, input().split()))
    inorders = list(map(int, input().split()))
    ret = []
    
    root = BinaryTree(preorders, inorders)
    postorder_traverse(root)
    
    print(' '.join(ret))