#User function Template for python3

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        count=0
        temp=head
        while temp:
            count=count+1
            temp=temp.next
        return count
        