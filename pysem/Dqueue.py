class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

front = rear = None

def insert(data):
    global front , rear
    n = Node(data)
    if front == None:
        front = rear = n
    else:
        rear.next = n
        rear = n
    
def delete():
    global front ,rear
    if front == None:
        print("Can not delete")
    elif front.next == None:
        print(front.data)
        front = rear = None
    else:
        print(front.data)
        front = front.next 
        