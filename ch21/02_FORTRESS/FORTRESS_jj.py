from sys import stdin


class Node:
    def __init__(self, x, y, r):
        self.bbox = (x-r, y-r, x+r, y+r)
        self.parent = None
        self.idx = 0
        self.visited = False
        self.children = list()

    def contains(self, other):
        if (self.bbox[0] < other.bbox[0]) and (self.bbox[1] < other.bbox[1]) and \
                (self.bbox[2] > other.bbox[2]) and (self.bbox[3] > other.bbox[3]):
            return True
        return False

    def __str__(self):
        x = (self.bbox[0]+self.bbox[2])//2
        y = (self.bbox[1]+self.bbox[3])//2
        r = (self.bbox[2]-self.bbox[0])//2
        return 'x: {} y: {} r: {}'.format(x, y, r)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        def insert_(n1, n2):
            if n1.contains(n2):
                if not n1.children:
                    n2.parent = n1
                    n2.index = len(n1.children)
                    n1.children.append(n2)
                else:
                    # go to the first children
                    insert_(n1.children[0], n2)

            elif n2.contains(n1):
                # no need to worry if parent is None (first circle contains all other circles)
                # replace n1's position with n2
                parent = n1.parent
                parent.children[n1.idx] = n2
                # set n2's index, parent, and children
                n2.idx = n1.idx
                n2.parent = parent
                n2.children.append(n1)
                # set n1's index and parent
                n1.parent = n2
                n1.idx = len(n2.children)

            else:
                # no need to worry if parent is None (first circle contains all other circles)
                parent = n1.parent
                # n1 is the last children
                if n1.idx >= len(parent.children) -1:
                    n2.idx = n1.idx + 1
                    n2.parent = parent
                    parent.children.append(n2)
                # n1 isn't the last -> go to the next sibling
                else:
                    insert_(parent.children[n1.idx+1], n2)

        if self.root is None:
            self.root = node
        else:
            insert_(self.root, node)

    def get_deepest(self):
        deepest = [None, 0]

        def traverse(node, depth):
            if not node.children:
                if depth >= deepest[1]:
                    deepest[1] = depth
                    deepest[0] = node
                return
            for ch in node.children:
                traverse(ch, depth+1)
        traverse(self.root, 0)
        return deepest[0]

    def get_max_traverse(self):
        max_cnt = [0]

        def traverse(node, cnt):
            if cnt >= max_cnt[0]:
                max_cnt[0] = cnt
            node.visited = True
            cnt += 1
            # go up, only if it has never gone down and unvisited
            if node.parent is not None:
                if not node.parent.visited:
                    traverse(node.parent, cnt)
            # go down only unvisited children
            if node.children:
                for ch in node.children:
                    if not ch.visited:
                        traverse(ch, cnt)

        if not self.root.children:
            return 0
        deepest = self.get_deepest()
        traverse(deepest, 0)
        return max_cnt[0]


C = int(stdin.readline().strip())
for _ in range(C):
    N = int(stdin.readline().strip())
    tree = Tree()
    for _ in range(N):
        x, y, r = [int(k) for k in stdin.readline().strip().split()]
        node = Node(x, y, r)
        tree.insert(node)
    print(tree.get_max_traverse())