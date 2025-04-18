class Queue:
    def __init__(self):
        self.queue = []
    def insert(self,data):
        if len(self.queue) >= 3:
            print("Queue is full")
            return
        self.queue.append(data)
        print(f"Inserted {data}")
    
    def delete(self):
        if not self.queue:
            print("Queue is empty")
            return
        return self.queue.pop(0)
    
    def front(self):
        if not self.queue:
            print("Queue is empty")
            return
        return self.queue[0]
    
    def display(self):
        print("Queue: ",self.queue)

q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.display()
q.delete()
q.display

