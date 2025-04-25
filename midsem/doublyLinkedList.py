class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self,data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        self.head = newNode

    def insertAtEnd(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        current = self.head
        while current.head:
            current = current.next
        current.next = newNode
        newNode.prev = current  
        
