class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

start = end = None

def insertAtBegin(data):
    global start , end
    n = Node(data)
    if start == None:
        start = end = n
    else:
        n.next = start
        start = n

def insertAtEnd(data):
    global start , end
    n = Node(data)
    if start == None:
        start = end = n
    else:
        end.next = n
        end = n

def countNode():
    t , c = start , 0
    while t:
        c += 1
        t = t.next
    return c

def insertAtPos(pos , data):
    global start , end
    n = Node(data)
    if pos == 1:
        if start == None:
            start = end = n
        else:
            n.next = start
            start = n
    elif pos < countNode() + 1:
        curr = prev = start
        i = 0
        if i < pos :
            prev = curr
            curr = curr.next
        prev.next =  n
        n.next = curr
    else:
        print("Position not found")

def found(elem):
    curr = start
    while curr:
        if curr.data == elem:
            return True
        curr = curr.next
    return False

def insertAtElem(elem , data):
    global start , end
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

def deleteAtBegin():
    global start , end
    if start == None:
        print("Delete not possible")
    else:
        start = start.next

def deleteAtEnd():
    curr = prev = start
    while curr:
        prev = curr
        curr = curr.next
    prev.next = None

def deleteAtPos(p):
    global start
    curr = prev = start
    if p > countNode():
        print("Position not found")
    elif p == 1:
        start = start.next
    else:
        i = 1
        if i < p:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = curr.next

def deleteElem(elem):
    global start , end
    curr = prev = start
    if start.data == elem:
        start = start.next
    else:
        while curr.data != elem:
            prev = curr
            curr = curr.next
        prev.next = curr.next


def printNode():
    curr = start
    while curr:
        print(curr.data , end="=>")
        curr = curr.next
    print("None")
    

insertAtBegin(10)
insertAtBegin(20)
insertAtEnd(30)
insertAtPos(2, 40)
insertAtElem(10, 40)
print(found(40))
printNode()



