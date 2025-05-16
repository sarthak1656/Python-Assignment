class StaticQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def insert(self, item):
        if len(self.queue) < self.size:
            self.queue.append(item)
        else:
            print("Queue Overflow")

    def delete(self):
        if self.queue:
            print("Deleted element is", self.queue.pop(0))
        else:
            print("Queue Underflow")

    def front(self):
        if self.queue:
            print("Element at the front is", self.queue[0])
        else:
            print("Queue is empty")

    def display(self):
        if self.queue:
            print("Queue is:")
            print(" ".join(self.queue))
        else:
            print("Queue is empty")

class DynamicQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)

    def delete(self):
        if self.queue:
            print("Deleted element is", self.queue.pop(0))
        else:
            print("Queue Underflow")

    def front(self):
        if self.queue:
            print("Element at the front is", self.queue[0])
        else:
            print("Queue is empty")

    def display(self):
        if self.queue:
            print("Queue is:")
            print(" ".join(self.queue))
        else:
            print("Queue is empty")

def run_queue(queue_type):
    while True:
        print("\n1.Insert\n2.Delete\n3.Display element at the front\n4.Display all elements of the queue\n5.Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Input the element for adding in queue: ")
            queue_type.insert(item)
        elif choice == 2:
            queue_type.delete()
        elif choice == 3:
            queue_type.front()
        elif choice == 4:
            queue_type.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

# MAIN MENU FOR QUEUES
print("1. Static Queue\n2. Dynamic Queue")
option = int(input("Choose Queue type: "))
if option == 1:
    size = int(input("Enter size of Static Queue: "))
    queue = StaticQueue(size)
elif option == 2:
    queue = DynamicQueue()
else:
    print("Invalid option")
    exit()

run_queue(queue)


# 1. Static Queue
# 2. Dynamic Queue
# Choose Queue type: 1
# Enter size of Static Queue: 5

# 1.Insert
# 2.Delete
# 3.Display element at the front
# 4.Display all elements of the queue
# 5.Quit
# Enter your choice: 1
# Input the element for adding in queue: 10

# 1.Insert
# 2.Delete
# 3.Display element at the front
# 4.Display all elements of the queue
# 5.Quit
# Enter your choice: 1
# Input the element for adding in queue: 20

# 1.Insert
# 2.Delete
# 3.Display element at the front
# 4.Display all elements of the queue
# 5.Quit
# Enter your choice: 4
# Queue is:
# 10 20

# 1.Insert
# 2.Delete
# 3.Display element at the front
# 4.Display all elements of the queue
# 5.Quit
# Enter your choice: 5
