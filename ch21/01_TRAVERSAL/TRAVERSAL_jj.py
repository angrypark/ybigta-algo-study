from sys import stdin
from sys import maxsize
MAX_IDX = 128

def parse_tree(pre_subtree, in_subtree):
    if not pre_subtree:
        return
    parent = pre_subtree[0]
    split_idx = in_subtree.index(parent)
    # left
    parse_tree(pre_subtree[1:split_idx+1], in_subtree[:split_idx])
    # right
    parse_tree(pre_subtree[split_idx+1:], in_subtree[split_idx+1:])
    # print
    ANS[0] += str(parent) + ' '

C = int(stdin.readline().strip())
A = [0]
for i in range(C):
    N = int(stdin.readline().strip())
    preorder = [int(k) for k in stdin.readline().strip().split()]
    inorder = [int(k) for k in stdin.readline().strip().split()]
    tree = [0] * MAX_IDX
    ANS = ['']
    A[0] = i
    parse_tree(preorder, inorder)
    print(ANS[0][:-1])