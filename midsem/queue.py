# class Queue:
#     def __init__(self):
#         self.queue = []
#     def insert(self,data):
#         if len(self.queue) >= 3:
#             print("Queue is full")
#             return
#         self.queue.append(data)
#         print(f"Inserted {data}")
    
#     def delete(self):
#         if not self.queue:
#             print("Queue is empty")
#             return
#         return self.queue.pop(0)
    
#     def front(self):
#         if not self.queue:
#             print("Queue is empty")
#             return
#         return self.queue[0]
    
#     def display(self):
#         print("Queue: ",self.queue)

# q = Queue()
# q.insert(10)
# q.insert(20)
# q.insert(30)
# q.display()
# q.delete()
# q.display


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def insert(self,data):
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
            return
        else:
            self.rear.next = newNode
            self.rear = newNode
        print(f"Inserted: {data}")

    def delete(self):
        if not self.front:
            print("Queue is empty")
            return
        deleted = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return deleted
    def peek(self):
        if not self.front:
            print("Queue is empty")
            return
        return self.front.data
    def display(self):
        current = self.front
        while current:
            print(current.data , end=" => ")
            current = current.next
        print("None")
    
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)
q.display()
q.delete()
q.delete()
q.display()
        

 
    


