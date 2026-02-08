class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doublyLL :
    def __init__(self):
        self.head = None

    def insertAtEnd (self, data):
        new_node = Node(data)

        if (self.head == None):
            self.head = new_node
            return
        temp = self.head
        while  temp.next != None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insertAtBig (self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertAtSP (self, data, index):
        if(index == 0):
            self.insertAtBig()
            return
        new_node = Node(data)
        temp = self.head
        for i in range ( index - 1):
            if temp is None:
                print("The index is out of bound")
                return
            temp = temp.next
            
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node

    def deleteAtLast(self):
        if (self.head is None):
            print("List is empty")
            return
        if (self.head.next is None):
            self.head = None
            return
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.prev.next = None
        
    

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end= " <--> ")
            temp = temp.next
        print("None")


dl = doublyLL()
dl.insertAtEnd(10)
dl.insertAtEnd(20)
dl.insertAtEnd(30)
dl.insertAtBig(5)
dl.insertAtBig(2)
dl.insertAtSP(50,5)
dl.deleteAtLast()
dl.display()