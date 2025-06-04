# Enter your code here
# linked list pass sum
class Node:
    def __init__(self,data):
        self.data=data       #creating class
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None     #starting point of linked list
        
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node      #inserting linked list
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node   # move the node
            
    def display(self):
        temp = self.head                 #display the linkedlist
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")
        
    def add_ll(self):
        temp=self.head
        sum=0
        while temp:                              #addingg linked list
            sum=sum+temp.data
            temp=temp.next
        return sum
    def getCount_11(self, head):
        count=0
        temp=head           #counting the elements
        while temp:
            count=count+1
            temp=temp.next
        return count
    def insert_start(self,data):
        new_node=Node(data)      #inserting the start
        new_node.next=self.head
        self.head=new_node
    def delete_start(self,data):
        self.head=self.head.next 
    def delete_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=none
        
ll=LinkedList()
ll.insert_end(100)
ll.delete_start(20)
ll.insert_end(30)
ll.insert_end(40)
ll.delete_end(50)
ll.display()
print("sum of elements in linked list is ")
ans=ll.add_ll()
print(ans)