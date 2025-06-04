
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, pos, data):
        if pos == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            temp = self.head
            for i in range(pos - 1):
                if temp is None:
                    print("Position out of bounds")
                    return
                temp = temp.next
            if temp is None:
                print("Position out of bounds")
                return
            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def add_ll(self):
        temp = self.head
        sum = 0
        while temp:
            sum += temp.data
            temp = temp.next
        return sum

    def get_count(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def delete_start(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

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

    def delete_value(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next is None:
            print("Value not found")
            return
        temp.next = temp.next.next

    def delete_position(self, pos):
        if pos == 1:
            self.delete_start()
        else:
            temp = self.head
            for i in range(pos - 2):
                if temp is None or temp.next is None:
                    print("Position out of bounds")
                    return
                temp = temp.next
            if temp.next is None:
                print("Position out of bounds")
                return
            temp.next = temp.next.next

ll = LinkedList()
ll.insert_at_beginning(100)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.insert_at_beginning(50)
ll.display()
print("Sum of elements in linked list is")
ans = ll.add_ll()
print(ans)
ll.delete_position(5)
print("After deleting at position 5:")
ll.display()
