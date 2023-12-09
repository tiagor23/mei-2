# AVL Tree
#error: right rotate and left rotate not needed. The update_height need to be before the balance_factor. the added height is 1 too much on line 17. 
class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return node.height

def update_height(node):
    if node is not None:
        node.height = 1 + max(height(node.left), height(node.right)) + 1 

def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # Duplicate keys are not allowed
    
    
    balance = balance_factor(root)
    update_height(root)
    

    # Left Heavy
    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # Right Heavy
    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)
    
    return root
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=' ')
        inorder_traversal(root.right)
        
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left or root.right:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

def main():
    root = None
    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]

    for key in keys:
        root = insert(root, key)   
    print("Inorder Traversal of AVL Tree:")
    inorder_traversal(root)
    left_rotate(root.left)
    right_rotate(root.left)
    print("\n")
    print_tree(root)
if __name__ == "__main__":
    main()
