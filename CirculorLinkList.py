class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CirdoublyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return

        last = self.head.prev

        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node

    def insertAtBig(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return

        last = self.head.prev

        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node
        self.head = new_node

    def insertAtSP(self, data, index):
        if index == 0:
            self.insertAtBig(data)
            return

        if self.head is None:
            print("List is empty")
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(index - 1):
            temp = temp.next
            if temp == self.head:
                print("Index out of range")
                return

        next_node = temp.next

        temp.next = new_node
        new_node.prev = temp
        new_node.next = next_node
        next_node.prev = new_node

    def deleteAtLast(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        last = self.head.prev
        new_last = last.prev

        new_last.next = self.head
        self.head.prev = new_last

    def deleteAtBig(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        last = self.head.prev
        new_head = self.head.next

        last.next = new_head
        new_head.prev = last
        self.head = new_head

    def deleteAtSP(self, idx):
        if self.head is None:
            print("List is empty")
            return

        if idx == 0:
            self.deleteAtBig()
            return

        temp = self.head

        for _ in range(idx):
            temp = temp.next
            if temp == self.head:
                print("Index out of range")
                return

        prev_node = temp.prev
        next_node = temp.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

cl = CirdoublyLL()
cl.insertAtSP(2, 72)
cl.insertAtBig(20)
cl.insertAtBig(30)
cl.insertAtBig(40)
cl.insertAtBig(50)
cl.insertAtBig(60)
cl.insertAtEnd(70)
cl.display()
