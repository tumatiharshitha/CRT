
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Added prev attribute

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)
dll.insert_at_beginning(40)
dll.insert_at_beginning(50)
dll.delete_end()
dll.display()
