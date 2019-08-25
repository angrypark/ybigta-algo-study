from sys import stdin

C = int(stdin.readline())

for _ in range(C):
    N = int(stdin.readline())
    preorder = [int(x) for x in stdin.readline().split()]
    inorder = [int(x) for x in stdin.readline().split()]
    def print_order(preorder, inorder):
        if not preorder or not inorder:
            return
        root = preorder[0]
        index = inorder.index(root)

        print_order(preorder[1:index+1], inorder[:index])
        print_order(preorder[index + 1:], inorder[index + 1:])

        print(root, end=' ')
    print_order(preorder, inorder)
    print()
    