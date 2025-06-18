class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def findmin(node):
    while node.left:
        node = node.left
    return node

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.left.left = Node(2)

# Use the function
min_node = findmin(root)
print("Minimum value in BST:", min_node.data)