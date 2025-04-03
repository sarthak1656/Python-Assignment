class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, pos, data):
        if pos < 1:
            print("Invalid position!")
            return
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 2):
            if not temp:
                print("Position out of range!")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def insert_before_element(self, target, data):
        if not self.head:
            print("List is empty!")
            return
        if self.head.data == target:
            self.insert_at_beginning(data)
            return
        temp = self.head
        while temp.next and temp.next.data != target:
            temp = temp.next
        if not temp.next:
            print("Element not found!")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def insert_after_element(self, target, data):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if not temp:
            print("Element not found!")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def search_element(self, key):
        temp = self.head
        pos = 1
        while temp:
            if temp.data == key:
                print(f"Element {key} found at position {pos}")
                return
            temp = temp.next
            pos += 1
        print("Element not found!")

    def display(self):
        if not self.head:
            print("List is empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def menu():
    ll = LinkedList()
    while True:
        print("\n1> Insert at beginning\n2> Insert at end\n3> Insert at a position\n4> Insert before an element")
        print("5> Insert after an element\n6> Display\n7> Search element\n8> Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            ll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            ll.insert_at_end(data)
        elif choice == 3:
            pos = int(input("Enter position: "))
            data = int(input("Enter data: "))
            ll.insert_at_position(pos, data)
        elif choice == 4:
            target = int(input("Enter element: "))
            data = int(input("Enter data: "))
            ll.insert_before_element(target, data)
        elif choice == 5:
            target = int(input("Enter element: "))
            data = int(input("Enter data: "))
            ll.insert_after_element(target, data)
        elif choice == 6:
            ll.display()
        elif choice == 7:
            key = int(input("Enter element to search: "))
            ll.search_element(key)
        elif choice == 8:
            break
        else:
            print("Invalid choice!")

menu()
