class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(index, 0)
        if index == 0:
            self.addAtHead(val)
            return
        previous = self.head
        for _ in range(index - 1):
            previous = previous.next
        previous.next = Node(val, previous.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            previous = self.head
            for _ in range(index - 1):
                previous = previous.next
            previous.next = previous.next.next
        self.size -= 1
