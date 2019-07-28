from sys import stdin

C = int(stdin.readline().strip())
for _ in range(C):
    quad_tree = stdin.readline().strip()
    def reverse(sub_tree, index):
        index += 1
        head = sub_tree[index]
        if head == 'w' or head == 'b':
            return head, index
        
        upperleft, new_index = reverse(sub_tree, index)
        upperright, new_index = reverse(sub_tree, new_index)
        lowerleft, new_index = reverse(sub_tree, new_index)
        lowerright, new_index = reverse(sub_tree, new_index)

        return "x" + lowerleft + lowerright + upperleft + upperright, new_index
    
    print(reverse(quad_tree, -1)[0])