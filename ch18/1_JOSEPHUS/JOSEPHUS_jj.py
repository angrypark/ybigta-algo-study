from sys import stdin

class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

    def __str__(self):
        return str(self.data)

class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def remove(self):
        if self.size > 1:
            prev = self.head.prev
            next = self.head.next
            prev.next = next
            next.prev = prev
            self.head = next
        else:
            self.head = None
        self.size -= 1

    def iter(self, k):
        for _ in range(k):
            self.head = self.head.next

    def append(self, node):
        if not self.size:
            self.head = node
            self.head.prev = node
            self.head.next = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
        self.size += 1

    def __str__(self):
        s = '['
        n = self.head
        for _ in range(self.size):
            s += str(n)
            s += ', '
            n = n.next
        s += ']'
        return s

C = int(stdin.readline())
for _ in range(C):
    N, K = [int(k) for k in stdin.readline().strip().split()]
    circ_list = List()
    for i in range(1, N+1):
        node = Node(i)
        circ_list.append(node)
    while circ_list.size > 2:
        circ_list.remove()
        circ_list.iter(K-1)
    a = circ_list.head.data
    b = circ_list.head.next.data
    print(a, b)