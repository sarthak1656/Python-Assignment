class ExprNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(c):
    return c in "+-*/"

def construct_tree(postfix):
    stack = []
    for char in postfix:
        node = ExprNode(char)
        if is_operator(char):
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack.pop()

def inorder_expr(root):
    if root:
        if is_operator(root.value):
            print("(", end="")
        inorder_expr(root.left)
        print(root.value, end="")
        inorder_expr(root.right)
        if is_operator(root.value):
            print(")", end="")

postfix_expr = "ab+ef*g*-"
root_expr = construct_tree(postfix_expr)
print("\nInorder of Expression Tree:")
inorder_expr(root_expr)
