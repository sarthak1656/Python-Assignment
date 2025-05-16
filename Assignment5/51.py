class StaticStack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            print("Stack Overflow")

    def pop(self):
        if self.stack:
            print("Popped item is:", self.stack.pop())
        else:
            print("Stack Underflow")

    def top(self):
        if self.stack:
            print("Item at the top is:", self.stack[-1])
        else:
            print("Stack Underflow")

    def display(self):
        if self.stack:
            print("Stack elements:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty")

class DynamicStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            print("Popped item is:", self.stack.pop())
        else:
            print("Stack Underflow")

    def top(self):
        if self.stack:
            print("Item at the top is:", self.stack[-1])
        else:
            print("Stack Underflow")

    def display(self):
        if self.stack:
            print("Stack elements:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty")

def run_stack(stack_type):
    while True:
        print("\n1.Push\n2.Pop\n3.Display the top element\n4.Display all stack elements\n5.Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter the item to be pushed: ")
            stack_type.push(item)
        elif choice == 2:
            stack_type.pop()
        elif choice == 3:
            stack_type.top()
        elif choice == 4:
            stack_type.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

# MAIN MENU FOR STACKS
print("1. Static Stack\n2. Dynamic Stack")
option = int(input("Choose Stack type: "))
if option == 1:
    size = int(input("Enter size of Static Stack: "))
    stack = StaticStack(size)
elif option == 2:
    stack = DynamicStack()
else:
    print("Invalid option")
    exit()

run_stack(stack)

 
# 1. Static Stack
# 2. Dynamic Stack
# Choose Stack type: 1
# Enter size of Static Stack: 5

# 1.Push
# 2.Pop
# 3.Display the top element
# 4.Display all stack elements
# 5.Quit
# Enter your choice: 1
# Enter the item to be pushed: 10

# 1.Push
# 2.Pop
# 3.Display the top element
# 4.Display all stack elements
# 5.Quit
# Enter your choice: 1
# Enter the item to be pushed: 20

# 1.Push
# 2.Pop
# 3.Display the top element
# 4.Display all stack elements
# 5.Quit
# Enter your choice: 1
# Enter the item to be pushed: 30

# 1.Push
# 2.Pop
# 3.Display the top element
# 4.Display all stack elements
# 5.Quit
# Enter your choice: 3
# Item at the top is: 30

# 1.Push
# 2.Pop
# 3.Display the top element
# 4.Display all stack elements
# 5.Quit
# Enter your choice: 4
# Stack elements:
# 30
# 20
# 10

# 1.Push
# 2.Pop
# 3.Display the top element
# 4.Display all stack elements
# 5.Quit
# Enter your choice: 2
# Popped item is: 30

# 1.Push
# 2.Pop
# 3.Display the top element
# 4.Display all stack elements
# 5.Quit
# Enter your choice: 3
# Item at the top is: 20

# 1.Push
# 2.Pop
# 3.Display the top element
# 4.Display all stack elements
# 5.Quit
# Enter your choice: 5
