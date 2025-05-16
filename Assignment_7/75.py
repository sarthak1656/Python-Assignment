class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return BSTNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

def search(root, key):
    if not root:
        print(f"{key} not found")
        return None
    if root.key == key:
        print(f"{key} found")
        return root
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def remove(root, key):
    if not root:
        return root
    if key < root.key:
        root.left = remove(root.left, key)
    elif key > root.key:
        root.right = remove(root.right, key)
    else:
        # Node with one or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # Node with two children
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = remove(root.right, temp.key)
    return root

# Main driver
if __name__ == "__main__":
    root = None
    keys = [20, 8, 22, 4, 12, 10, 14]
    for key in keys:
        root = insert(root, key)

    print("Inorder traversal of the binary search tree is:")
    inorder(root)
    print()
    search(root, 222)
    search(root, 22)
    root = remove(root, 4)
    inorder(root)
