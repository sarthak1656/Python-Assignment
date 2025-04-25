class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insert_at_position(self, pos, data):
        if pos <= 0:
            print("Invalid position!")
            return
        if pos == 1:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        curr = self.head
        for _ in range(pos - 2):
            if not curr:
                print("Position out of bounds!")
                return
            curr = curr.next
        if not curr:
            print("Position out of bounds!")
            return
        new_node.next = curr.next
        if curr.next:
            curr.next.prev = new_node
        new_node.prev = curr
        curr.next = new_node

    def insert_before_element(self, target, data):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if not curr:
            print("Element not found!")
            return
        if curr == self.head:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr
        curr.prev = new_node

    def insert_after_element(self, target, data):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if not curr:
            print("Element not found!")
            return
        new_node = Node(data)
        new_node.next = curr.next
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr

    def display(self):
        curr = self.head
        if not curr:
            print("List is empty")
            return
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def search(self, data):
        curr = self.head
        pos = 1
        while curr:
            if curr.data == data:
                print(f"Element {data} found at position {pos}")
                return
            curr = curr.next
            pos += 1
        print("Element not found!")

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None

    def delete_at_position(self, pos):
        if pos <= 0 or not self.head:
            print("Invalid position or list is empty!")
            return
        if pos == 1:
            self.delete_at_beginning()
            return
        curr = self.head
        for _ in range(pos - 1):
            if not curr:
                print("Position out of bounds!")
                return
            curr = curr.next
        if not curr:
            print("Position out of bounds!")
            return
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev

    def delete_element(self, data):
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        if not curr:
            print("Element not found!")
            return
        if curr == self.head:
            self.delete_at_beginning()
            return
        if curr.next:
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next


def menu():
    dll = DoublyLinkedList()
    while True:
        print("""
1>insert at beginning
2>insert at end
3>insert at a position
4>insert before an element
5>insert after an element
6>display
7>search element
8>delete at beginning
9>delete at end
10>delete at position
11>delete element
12>exit
        """)
        choice = int(input("Enter choice: "))
        if choice == 1:
            dll.insert_at_beginning(int(input("Enter data: ")))
        elif choice == 2:
            dll.insert_at_end(int(input("Enter data: ")))
        elif choice == 3:
            pos = int(input("Enter position: "))
            data = int(input("Enter data: "))
            dll.insert_at_position(pos, data)
        elif choice == 4:
            target = int(input("Enter element: "))
            data = int(input("Enter data: "))
            dll.insert_before_element(target, data)
        elif choice == 5:
            target = int(input("Enter element: "))
            data = int(input("Enter data: "))
            dll.insert_after_element(target, data)
        elif choice == 6:
            print("The elements in the list are:")
            dll.display()
        elif choice == 7:
            dll.search(int(input("Enter element to search: ")))
        elif choice == 8:
            dll.delete_at_beginning()
        elif choice == 9:
            dll.delete_at_end()
        elif choice == 10:
            dll.delete_at_position(int(input("Enter position: ")))
        elif choice == 11:
            dll.delete_element(int(input("Enter element to delete: ")))
        elif choice == 12:
            print("Exiting program.")
            break
        else:
            print("Invalid choice!")

# Run the menu
menu()
