class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")
    def insertAtBeginning(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def insertAtEnd(self,data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        current = self.head # imp
        while current.next:
            current = current.next
        current.next = newNode
    def insertAtPosition(self , data ,pos):
        if pos == 0:
            self.insertAtBeginning(data)
            return
        newNode = Node(data)
        current = self.head
        for i in range(pos - 1):
            if not current:
                print("Position out of range")
                return
            current = current.next
        newNode.next = current.next
        current.next = newNode
    def insertBeforeElement(self , data ,target):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == target:
            self.insertAtBeginning(data)
            return
        current = self.head
        while current.next and current.next.data != target:
            current = current.next
        if current.next is None:
            print("Element not found")
            return
        newNode = Node(data)
        newNode.next = current.next
        current.next = newNode
    def insertAfterElement(self , data ,target):
        current = self.head
        while current and current.data != target:
            current = current.next
        if not current:
            print("Element not found")
            return
        newNode = Node(data)
        newNode.next = current.next
        current.next = newNode
    
    def deleteAtBeginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
    
    def deleteAtEnd(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    def deleteAtPosition(self,pos):
        if not self.head:
            print("List is empty")
            return
        if pos == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(pos - 1):
            if not current.next:
                print("Position out of range")
                return
            current = current.next
        current.next = current.next.next
        
    def deleteElement(self,target):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != target:
            current = current.next
        if not current.next:
            print("Element not found")
            return
        current.next = current.next.next
    def searchByElement(self,target):
        current = self.head
        pos = 0
        while current:
            if current.data == target:
                print(f"Element {target} found in {pos}.")
                return
            current = current.next
            pos += 1
        print("Element not found")

                

    

    