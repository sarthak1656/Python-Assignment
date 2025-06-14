class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
start = end = None

def insertAtBeggining(data):
    global start , end
    n = Node(data)
    if start == None:
        start = end = n
    else:
        n.next = start
        start = n

def insertAtEnd(data):
    global start, end
    n = Node(data)
    if start == None:
        start = end = n
    else:
        end.next = n
        end = n
def countnode():
    t , c = start , 0
    while t:
        c += 1
        t = t.next
    return c

def insertAtPosition(position ,data):
    global start , end
    n = Node(data)
    if position == 1:
        if start == None:
            start = end = n
        else:
            n.next = start
            start = n
    elif position < countnode()+1:
        curr = prev = start
        i = 1
        while i < position:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = n
        n.next = curr

def found(elem):
    curr = start
    pos = 1
    while curr:
        if curr.data == elem:
            return pos
        curr = curr.next
        pos += 1
    return -1  

def insertAtElement(elem ,data):
    global start ,end
    n = Node(data)
    curr = prev = start
    if start.data == elem:
        n.next = start
        start = n
    else:
        while curr.data != elem:
            prev = curr
            curr = curr.next
        prev.next = n
        n.next = curr



