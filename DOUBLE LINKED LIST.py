class Node:
    def __init__(self,prv,next,data):
        self.next=None
        self.data=data
         self.prv=None
class DoubleLinkedList:
    
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        new_node=Node(None,None,data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prv=new_node
            self.head=new_node
    def delete_beginning(self):
        self.head=self.head.next
        self.head.prv=None
    def delete_end(self):
        if self.head.next is None:      
            self.head=None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
            temp.prv.next=None 
    def display(self):
        temp=self.head
        while temp:
            print(temp,data,end="->")
            temp=temp.next
        print("None") 
        

                    

       
