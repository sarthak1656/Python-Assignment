class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

top = None
def push(data):
    global top
    n = Node(data)
    if top == None:
        top = n
    else:
        n.next = top
        top = n

def pop():
    global top
    if top == None:
        print("Can not pop")
    else:
        print(top.data,"Popped")
        top = top.next