# Binary Tree
#error: def order_tree(root) need to inorder_traversal(node.left) first . on line 13 should be +1 not +2
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(root, level=0):
    if root is None:
        return

    print_tree(root.right, level + 2)
    print("    " * level + str(root.value))
    print_tree(root.left, level + 1)

def add_node(root, value):
    if root is None:
         return Node(value)
    else:
        if value < root.value:
            root.left = add_node(root.left, value)
        else:
            root.right = add_node(root.right, value)
        return root
def order_tree(root):
    ordered_values = []
    def inorder_traversal(node):
        if node is None:
            return

        inorder_traversal(node.right)
        ordered_values.append(node.value)
        inorder_traversal(node.left)

    inorder_traversal(root)
    return ordered_values

def generate_binary_tree():
    root = Node(23)
    add_node(root, 13)
    add_node(root, 34)
    add_node(root, -11)
    add_node(root, 4)
    return root

tree = generate_binary_tree()
print_tree(tree)
print(order_tree(tree))