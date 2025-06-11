class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


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
        print(root.data,end=" ")
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

print("Binary Tree Traversals:")
inorder(n1)
print()
preorder(n1)
print()
postorder(n1)

# Binary Tree Traversals:
# 30 20 10 50 
# 10 20 30 50 
# 30 20 50 10 

