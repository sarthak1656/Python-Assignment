class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = NotImplemented
        
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(50)


n1.left = n2
n1.right = n4
n2.left = n3


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')


def menu():
    while True:
        print("\nBinary Tree Traversal Menu")
        print("1. Inorder Traversal")
        print("2. Preorder Traversal")
        print("3. Postorder Traversal")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("Inorder Traversal:")
            inorder(n1)
            print()
        elif choice == '2':
            print("Preorder Traversal:")
            preorder(n1)
            print()
        elif choice == '3':
            print("Postorder Traversal:")
            postorder(n1)
            print()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and ")
menu()
