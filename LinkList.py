class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def print(self):
        while self:
            print(self.val, "->")
            self = self.next


class LinkList:
    head = 0

    def __init__(self):
        self.head = None

    def insert(self, pos, num):
        node = Node(num)
        aft = self.head
        pre = None
        i = 0
        while aft and i < pos:
            pre = aft
            aft = aft.next
            i = i + 1
        if pre:
            pre.next = node
        node.next = aft

    def create(self, arr):
        self.head = Node(arr[0])
        p = self.head
        for i in arr[1:]:
            p.next = Node(i)
            p = p.next
