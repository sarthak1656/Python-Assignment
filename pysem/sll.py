class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
start = end = None

def insertAtBeginning(data):
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


def insertAtPosition(position , data):
    global start , end
    n = Node(data)
    if position == 1:
        if start == None:
            start = end = n
        else:
            n.next = start
            start = n
            
    elif position < countNode()+1:
        curr = prev = start
        i = 1
        if i < position:
            curr = prev
            curr = curr.next
            i += 1
        prev.next = n
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
    global start 
    if start == None:
        print("Deletion is not possible")
    else:
        start = start.next

def deleteAtEnd():
    curr = prev = start
    while curr.next:
        prev = curr
        curr = curr.next
    prev.next = None

def deleteAtPos(p):
    global start
    curr = prev = start
    if p > countNode():
        print("Position not Found")
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
    global start,end
    curr = prev = start
    if start.data == elem:
        start = start.next
    else:
        while curr.data != elem:
            prev = curr
            curr = curr.next
        prev.next = curr.ne

def printList():
    curr = start
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


insertAtBeginning(30)
insertAtBeginning(20)
insertAtEnd(40)
insertAtPosition(2, 25)
insertAtElem(40, 35)

printList()
