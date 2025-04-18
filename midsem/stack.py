# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self,data):
#         self.stack.append(data)
#         print(f"Pushed {data}")
    
#     def pop(self):
#         if not self.stack:
#             print("Stack is empty")
#             return
#         popped = self.stack.pop()
#         return popped
    
#     def peek(self):
#         if not self.stack:
#             print("Stack is empty")
#             return
#         return self.stack[-1]
#     def display(self):
#         print("Stack: ",self.stack)

# s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.display()
# s.pop()
# s.display()


# Stack using linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    
    def push (self , data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        print(f"Pushed {data}")

    def pop(self):
        if not self.top:
            print("Stack is empty")
            return
        popped = self.top.data
        self.top = self.top.next
        return popped
    def peek(self):
        if not self.top:
            print("Stack is empty")
            return
        return self.top.data
    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.pop()
s.display()
    
        