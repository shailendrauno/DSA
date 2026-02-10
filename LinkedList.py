
class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None      



class LinkedList:
    def __init__(self):
        self.head = None      


    # ---------------- INSERT OPERATIONS ----------------

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)     # Create a new node
        new_node.next = self.head
        self.head = new_node


    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next     # Move to last node
        temp.next = new_node


    # Insert at a specific position (0-based index)
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    # ---------------- DELETE OPERATIONS ----------------

    # Delete from the beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next


    # Delete from the end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        # If only one node exists
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


    # Delete from a specific position (0-based index)
    def delete_from_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.delete_from_beginning()
            return

        temp = self.head
        for i in range(position - 1):
            if temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        temp.next = temp.next.next


    # ---------------- DISPLAY ----------------

    # Display the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_position(15, 1)

ll.display()

ll.delete_from_beginning()
ll.delete_from_end()
ll.delete_from_position(1)

ll.display()  